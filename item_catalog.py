import __init__
from flask import Flask, render_template, request
from flask import redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy import desc
from sqlalchemy.orm import sessionmaker
from database_setup import Base
from model.user import User
from model.category import Category
from model.item import  Item
from flask import session as login_session
import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests
import routehandlers

app = Flask(__name__)

CLIENT_ID = json.loads(
    open('client_secret.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Item Catalog Application"


engine = create_engine('sqlite:///category_items.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase +
                                  string.digits) for x in xrange(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state)


# method that allows user to login to the app using google credentials
@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secret.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(
            json.dumps('Current user is already connected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()
    data = json.loads(answer.txt)

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']
    # ADD PROVIDER TO LOGIN SESSION
    login_session['provider'] = 'google'

    # see if user exists, if it doesn't make a new one
    user_id = getUserID(data["email"])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius:'
    output += '150px;-webkit-border-radius: 150px;'
    output += '-moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    print "done!"
    return output


# method that allows the user to login using his facebook credentials
@app.route('/fbconnect', methods=['POST'])
def fcbkconnect():
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    access_token = request.data
    print "access token received %s " % access_token

    app_id = json.loads(open('fb_client_secrets.json', 'r').read())[
        'web']['app_id']
    app_secret = json.loads(
        open('fb_client_secrets.json', 'r').read())['web']['app_secret']
    url = 'https://graph.facebook.com/oauth/access_token?grant_type'
    url += 'fb_exchange_token&client_id=%s&client_secret='
    URL += '%s&fb_exchange_token=%s' % (app_id, app_secret, access_token)
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]

    # Use token to get user info from API
    userinfo_url = "https://graph.facebook.com/v2.8/me"
    '''
        Due to the formatting for the result from the server token exchange
        we have to split the token first on commas and select the first
        index which gives us the key : value for the server access token
        then we split it on colons to pull out the actual token value
        and replace the remaining quotes with nothing so that it can
        be used directly in the graph api calls
    '''
    token = result.split(',')[0].split(':')[1].replace('"', '')
    url = 'https://graph.facebook.com/v2.8/me?'
    url += 'access_token=%s&fields=name,id,email' % token
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]
    # print "url sent for API access:%s"% url
    # print "API JSON result: %s" % result
    data = json.loads(result)
    login_session['provider'] = 'facebook'
    login_session['username'] = data["name"]
    login_session['email'] = data["email"]
    login_session['facebook_id'] = data["id"]

    # The token must be stored in the login_session in order to properly logout
    login_session['access_token'] = token

    # Get user picture
    url = 'https://graph.facebook.com/v2.8/me/picture?access_token'
    url += '=%s&redirect=0&height=200&width=200' % token
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]
    data = json.loads(result)

    login_session['picture'] = data["data"]["url"]

    # see if user exists
    user_id = getUserID(login_session['email'])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']

    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius:'
    output += '150px;-webkit-border-radius: 150px;'
    output += '-moz-border-radius: 150px;"> '

    flash("Now logged in as %s" % login_session['username'])
    return output


# method thats disconnects user that is logged using facebook
@app.route('/fbdisconnect')
def fcbkdisconnect():
    facebook_id = login_session['facebook_id']
    # The access token must me included to successfully logout
    access_token = login_session['access_token']
    url = 'https://graph.facebook.com/%s/permissions?'
    url += 'access_token=%s' % (facebook_id, access_token)
    h = httplib2.Http()
    result = h.request(url, 'DELETE')[1]
    flash('You have been logged out!')
    return redirect(url_for('firstPage'))


# method to delete user's session
@app.route('/disconnect')
def disconnect():
    login_session.clear()
    flash('You have been logged out!')
    return redirect(url_for('firstPage'))


# User Helper Functions
# method that creates user in the database using email and password
@app.route('/register', methods=['GET', 'POST'])
def createUserWithPass():
    if request.method == 'POST':
        user_exist = getUserID(request.form['email'])
        if not user_exist:
            n_user = User(name=request.form['name'],
                          email=request.form['email'],
                          passw=request.form['password'])
            session.add(n_user)
            session.commit()
            userwp = session.query(User).filter_by(email=n_user.email).one()
            login_session['username'] = userwp.name
            login_session['email'] = userwp.email
            login_session['user_id'] = userwp.id
            flash('Registration success!')
            return redirect(url_for('firstPage'))
        else:
            return render_template('register.html')
    else:
        return render_template('register.html')


# method that allows user to login using email and password
@app.route('/login', methods=['GET', 'POST'])
def loginUserWithPass():
    if request.method == 'POST':
        user_id = getUserID(request.form['email'])
        if user_id:
            c_user = getUserInfo(user_id)
            login_session['username'] = c_user.name
            login_session['email'] = c_user.passw
            login_session['user_id'] = c_user.id
            flash('You have been logged in with success!')
            return redirect(url_for('firstPage'))
        else:
            return render_template('login.html', STATE=state)
    else:
        return render_template('login.html', STATE=state)


def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None


@app.route('/', methods=['GET', 'POST'])
def firstPage():
    all_category = session.query(Category).all()
    if 'username' not in login_session:
        return render_template('../templates/p_index.html', categories=all_category)
    else:
        return render_template('index.html', categories=all_category)


# method for JSON endpoint for all items of a category in the catalog.
@app.route('/category/<int:category_id>/item/JSON')
def CategoryItemJSON(category_id):
    category = session.query(Category).filter_by(id=category_id).one()
    items = session.query(Item).filter_by(
        category_id=category_id).all()
    return jsonify(Items=[i.serialize for i in items])


# method for JSON endpoint for an arbitrary category in the catalog.
@app.route('/category/<int:category_id>/JSON')
def categoryCategoryJSON(category_id):
    Item = session.query(Category).filter_by(id=category_id).one()
    return jsonify(Category=ICategory.serialize)


# method for JSON endpoint for an arbitrary item in the catalog.
@app.route('/category/<int:category_id>/item/<int:item_id>/JSON')
def itemItemJSON(category_id, item_id):
    Item = session.query(Item).filter_by(id=item_id).one()
    return jsonify(Item=Item.serialize)


# method for JSON endpoint for all categories in the catalog.
@app.route('/category/JSON')
def categoryJSON():
    category = session.query(Category).all()
    return jsonify(category=[r.serialize for r in category])


# Show all category
@app.route('/')
def showCategories():
    category = session.query(Category).all()
    return render_template('category.html', category=category)


# Create a new category
@app.route('/category/new/', methods=['GET', 'POST'])
def newCategory():
    if request.method == 'POST':
        newCategory = Category(name=request.form['name'])
        session.add(newCategory)
        session.commit()
        return redirect(url_for('showCategories'))
    else:
        return render_template('newCategory.html')


# Edit a category
@app.route('/category/<int:category_id>/edit/', methods=['GET', 'POST'])
def editCategory(category_id):
    editedCategory = session.query(
        Category).filter_by(id=category_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedCategory.name = request.form['name']
            flash('Category %s has been successfuly edited!' %
                  editedCategory.name)
            return redirect(url_for('showCategories'))
    else:
        return render_template(
            'editCategory.html', category=editedCategory)


# method to delete a category
@app.route('/category/<int:category_id>/delete/', methods=['GET', 'POST'])
def deleteCategory(category_id):
    categoryToDelete = session.query(
        Category).filter_by(id=category_id).one()
    cat_name = categoryToDelete.name
    if request.method == 'POST':
        session.delete(categoryToDelete)
        session.commit()
        flash('Category %s has been successfuly deleted!' % cat_name)
        return redirect(
            url_for('showCategories', category_id=category_id))
    else:
        return render_template(
            'deleteCategory.html', category=categoryToDelete)


# Show a category item
@app.route('/category/<int:category_id>/')
@app.route('/category/<int:category_id>/item/')
def showItem(category_id):
    cat = session.query(Category).filter_by(id=category_id).one()
    items = session.query(Item).filter_by(
        category_id=category_id).all()
    if 'username' not in login_session:
        return render_template('publicitems.html', items=items, category=cat)
    else:
        return render_template('items.html', items=items, category=cat)


# Create a new item
@app.route(
    '/category/<int:category_id>/item/new/', methods=['GET', 'POST'])
def newItem(category_id):
    if request.method == 'POST':
        newItem = Item(name=request.form['name'], description=request.form[
                           'description'], price=request.form['price'],
                       category_id=category_id)
        session.add(newItem)
        session.commit()
        flash('Item %s has been successfuly created!' % newItem.name)
        return redirect(url_for('showItem', category_id=category_id))
    else:
        return render_template('newitem.html', category_id=category_id)

    return render_template('newItem.html', category=category)
    # return 'This page is for making a new item item for category %s'
    # %category_id


# Edit a item item
@app.route('/category/<int:category_id>/item/<int:item_id>/edit',
           methods=['GET', 'POST'])
def editItem(category_id, item_id):
    editedItem = session.query(Item).filter_by(id=item_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
        if request.form['description']:
            editedItem.description = request.form['name']
        editedItem.price = request.form['price']

        session.add(editedItem)
        session.commit()
        flash('Item %s has been successfuly edited!' % editedItem.name)
        return redirect(url_for('showItem', category_id=category_id))
    else:

        return render_template(
            'edititem.html', category_id=category_id,
            item_id=item_id, item=editedItem)


# Delete a item item
@app.route('/category/<int:category_id>/item/<int:item_id>/delete',
           methods=['GET', 'POST'])
def deleteItem(category_id, item_id):
    itemToDelete = session.query(Item).filter_by(id=item_id).one()
    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        flash('Item %s has been successfuly deleted!' % itemToDelete.name)
        return redirect(url_for('showItem', category_id=category_id))
    else:
        return render_template('deleteItem.html', item=itemToDelete)


# method that displays the login page

if __name__ == '__main__':
    app.debug = True
    app.secret_key = 'super secret key'
    app.run(host='0.0.0.0', port=8000)
