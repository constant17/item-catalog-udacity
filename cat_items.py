
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import json
from database_setup import Category, User, Base, Item

engine = create_engine('sqlite:///category_items.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# User
a_user = User(name="Constant", email="constantpagoui@gmail.com", passw="lcp12316")

session.add(a_user)
session.commit()

#
category_json = json.loads("""{
    "all_categories": [
    {
        "name" : "Soccer"
	},
    {
 	"name" : "Basketball"
        },
    {
 	"name" : "Rugby"
	},
    {
 	"name" : "Football"
	},
    {
 	"name" : "Tennis"
	},
    {
 	"name" : "Rock Climbing"
	},
    {
 	"name" : "Frisbee"
	},
    {
 	"name":"Box"
	},
    {"name":"sex"}
    ]
    }""")
items_json = json.loads("""{
    "categorie1_items": [
    {
        "name" : "Shinguards", 
	"description" : "Nike J Guard Soccer Shin Guards"+
                    "are designed to add an extra layer of protection without"+
                    "hindering your mobility on the field. With a lightweight,"+
                    "low-profile design, you will obtain the protection"+
                    "you need without being weighed down. Perfect for strikers"+
                    "who rely on speed ..",
        "price":"45"
    },
    {
        "name" : "Pop up soccer goal", 
	"description" : "This pop-up goal will have you playing soccer"+
            " in seconds! The FORZA Flash is ideal for both kids playing in the back yard alongside senior ",
        "price" : "26.99"
    },
    {
        "name" : "Quickster Soccer Trainer",
        "description" : "With the Quickster soccer trainer, you can master"+
		    "the first touch by receiving passes in the air and on the ground.  Maximize your reps"+
		    "from all angles with the unique net design that offers realizsting in-game experience at home",
        "price" : "119.99"
    },
    {
	"name" : "Free Quick Mannequin - Junior 5ft 4in",
	"description" : "Bend it like Beckham with these free quick mannequins!",
        "price" : "74.99"
    },
    {
        "name" : "Bison ScoreMore Corner Kick Training Aid",
        "description" : "Practice makes perfect and this set of 4 velcro-on bright",
        "price" : "74.49"
    },
    {
	"name" : "Soccer Practice vests",
	"description" : "100% Polyester mesh, one size fits most;"+
                    " Enclosed sides for better durability Loose fit waist eliminates ride up",
        "price" : "3.45"
    },
    {
	"name" : "Mikasa soccer balls",
	"description" : "Deluxe Cushioned Cover ; 2 Ply Butyl Bladder"+
                    " Best Club or Practice Ball",
        "price" : "8.09"
        },
    {
        "name" : "Soccer Goal Net",
	"description" : "Epic 8 x 24 x 3 x 8 Soccer Goal Net (White)"+
		    " 1 Net Only, Goal Not Included"+
		    " Rope type: 3MM-Twisted; Material: Polyethylene; Mesh: 5 c",
        "price" : "44.99"
    },
    {
    	"name" : "Nike Mercurial Superfly",
	"description" : "Soccer shoes",
        "price" : "200"
	},
    {
    	"name":"Nike Mercurial Superfly",
	"description":"Soccer shoes",
        "price":"200"
        },
      ]
    }""")

items_j = json,loads("""{
    "categorie2_items": [
    {
        "name" : "Spalding NBA Street Phantom Basketball",

        "description" : "Spalding NBA Street Phantom 29.5 (size 7) has"
		    +"a premium outdoor cover designed for both outdoor and indoor use. The Soft Grip "
		    +"technology provides maximum grip & control, optimal outdoor performance and superior durability.",
        "price" : "7.99"
    },
    {
        "name" : "Backboard and Basketball Hoop",
        "description" : "The Lifetime Backboard and Rim Combo has a clear, "+
                    "shatter-guard basketball backboard. It has an all-weather design to withstand the elements. Made from steel and polyethylene ",
        "price" : "136.99"
    },
    {
        "name" : "Boys' Core Basketball Shorts",
        "description" : "The Boys' Core Knit Short from C9 Champion features wicking fabric"+
		    "and a semi-fit to make this short great for activities or daily wear",
        "price" : "15"
    },
    {
	"name" : "Men's inferno basketball shoes ",
        "description" : "Get set up with the basketball look with the Inferno from Champion."+
		    " It features a mesh upper, laces for good fit, ankle pull tab for easy on/easy off",
        "price" : "29.99"
    },
    {
        "name" : "Girls' Core Basketball Shorts",
        "description"  :  "The Girls' Core Knit Short from C9 Champion features wicking fabric"+
                "and a semi-fit to make this short great for activities or daily wear",
        "price" : "14"
    },
    {
	"name" : "Nike Elite Basketball socks",
        "description" : "The Nike Elite Basketball Crew Sock features Midfoot Compression"+
                 "Fit that helps keep socks and cushioning in place. Footstrike cushioning. "+
                 "Clearly defined pattern is closely aligned to pressure patterns on the feet. Dri-fit fabric",
        "price" : "13.99"
        }
    ]
    }""")
	
for e in category_json['all_categories']:
    cat = Category(
        name = str(e['name']),
	user = a_user
	)
    session.add(category)
    session.commit()
    if e == 0:
        for i in items_json['category1_items']:
            itemm = Item(
                name = str(i['name']),
                description = str(i['description']),
                price = str(i['price']),
                user = a_user,
                category = cat)
            session.add(itemm)
            session.commit()
    elif e == 1:
        for i in items_j['category2_items']:
            item2 = Item(
                name = str(i['name']),
                description = str(i['description']),
                price = str(i['price']),
                category = cat)
            session.add(item2)
            session.comit()
    
