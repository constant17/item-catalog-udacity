
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

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
user = User(name="Constant", email="constantpagoui@gmail.com")

session.add(user)
session.commit()

# 
categorie1 = Category(name="Soccer")

session.add(categorie1)
session.commit()

item1 = Item(name="Shinguards", description="Nike J Guard Soccer Shin Guards"+
                    "are designed to add an extra layer of protection without"+
                    "hindering your mobility on the field. With a lightweight,"+
                    "low-profile design, you will obtain the protection"+
                    "you need without being weighed down. Perfect for strikers"+
                    "who rely on speed ..", category=categorie1)

session.add(item1)
session.commit()


item2 = Item(name="Pop up soccer goal", description="This pop-up goal will have you playing soccer"+
					" in seconds! The FORZA Flash is ideal for both kids playing in the back yard alongside senior ",
                      price="26.99", category=categorie1)

session.add(item2)
session.commit()

item3 = Item(name="Quickster Soccer Trainer", description="With the Quickster soccer trainer, you can master"+
				  "the first touch by receiving passes in the air and on the ground.  Maximize your reps"+
				  "from all angles with the unique net design that offers realizsting in-game experience at home",
                      price="119.99", category=categorie1)

session.add(item3)
session.commit()

Item4 = Item(name="Free Quick Mannequin - Junior 5ft 4in", description="Bend it like Beckham with these free quick mannequins!",
                    price="74.99", category=categorie1)

session.add(Item4)
session.commit()

Item5 = Item(name="Bison ScoreMore Corner Kick Training Aid", description="Practice makes perfect and this set of 4 velcro-on bright",
                     price="74.49", category=categorie1)

session.add(Item5)
session.commit()

Item6 = Item(name="Soccer Practice vests", description="100% Polyester mesh, one size fits most;"+
				  " Enclosed sides for better durability Loose fit waist eliminates ride up",
                      price="3.45", category=categorie1)

session.add(Item6)
session.commit()

Item7 = Item(name="Mikasa soccer balls", description="Deluxe Cushioned Cover ; 2 Ply Butyl Bladder"+
					" Best Club or Practice Ball",
                      price="8.09", category=categorie1)

session.add(Item7)
session.commit()

Item8 = Item(name="Soccer Goal Net", description="Epic 8 x 24 x 3 x 8 Soccer Goal Net (White)"+
				  " 1 Net Only, Goal Not Included"+
				  " Rope type: 3MM-Twisted; Material: Polyethylene; Mesh: 5 c",
                     price="44.99", category=categorie1)

session.add(Item8)
session.commit()

Item9 = Item(name="Nike Mercurial Superfly", description="Soccer shoes",
                     price="200", category=categorie1)

session.add(Item9)
session.commit()


# Menu for Super Stir Fry
categorie2 = Category(name="Basketball")

session.add(categorie2)
session.commit()


Item1 = Item(name="Spalding NBA Street Phantom Basketball", description="Spalding NBA Street Phantom 29.5 (size 7) has"
				 +"a premium outdoor cover designed for both outdoor and indoor use. The Soft Grip "
				 +"technology provides maximum grip & control, optimal outdoor performance and superior durability.",
                     price="7.99",  category=categorie2)

session.add(Item1)
session.commit()

Item2 = Item(
    name="Backboard and Basketball Hoop", description="The Lifetime Backboard and Rim Combo has a clear, "+
    "shatter-guard basketball backboard. It has an all-weather design to withstand the elements. Made from steel and polyethylene ", price="136.99", category=categorie2)

session.add(Item2)
session.commit()

Item3 = Item(name="Boys' Core Basketball Shorts", description="The Boys' Core Knit Short from C9 Champion features wicking fabric"+
				"and a semi-fit to make this short great for activities or daily wear",
                     price="15",  category=categorie2)

session.add(Item3)
session.commit()

Item4 = Item(name="Men's inferno basketball shoes ", description="Get set up with the basketball look with the Inferno from Champion."+
				  " It features a mesh upper, laces for good fit, ankle pull tab for easy on/easy off",
                     price="29.99", category=categorie2)

session.add(Item4)
session.commit()

Item5 = Item(name="Girls' Core Basketball Shorts", description="The Girls' Core Knit Short from C9 Champion features wicking fabric"+
				"and a semi-fit to make this short great for activities or daily wear",
                     price="14",  category=categorie2)

session.add(Item5)
session.commit()

Item6 = Item(name="Nike Elite Basketball socks", description="The Nike Elite Basketball Crew Sock features Midfoot Compression"+
             "Fit that helps keep socks and cushioning in place. Footstrike cushioning. Clearly defined pattern is closely aligned to pressure patterns on the feet. Dri-fit fabric",
                     price="13.99", category=categorie2)

session.add(Item6)
session.commit()


# Menu for Panda Garden
categorie1 = Category(name="Baseball")

session.add(categorie1)
session.commit()


Item1 = Item(name="Baseball Cross Necklace", description="he official seller of Five Tool products brings you Five Tool's signature baseball cross",
                     price="8.99",  category=categorie1)

session.add(Item1)
session.commit()

Item2 = Item(name="Bullet ball", description="Improve your abilities with the SKLZ Bullet Ball. It accurately measures velocities up to 120 mph",
                     price="25.99", category=categorie1)

session.add(Item2)
session.commit()

Item3 = Item(name="Baseball wood bat", description="Every Marucci bat is cut, calibrated, balanced, buffed and lacquered by hand."+
             "Marucci uses top grade Maple billets cut from selected, naturally grown trees in Pennsylvania forests.",
                     price="79.95", category=categorie1)

session.add(Item3)
session.commit()

Item4 = Item(name="Ryan Blaney New Era Hat", description="New Era gives you a new look that is ready to keep up with the speed of Ryan Blaney at every turn",
                     price="6.99", category=categorie1)

session.add(Item4)
session.commit()

Item2 = Item(name="Premium Pro Fielder gloves", description="Selected Style: 11.5in Worn on Left Hand",
                     price="69.99", category=categorie1)

session.add(Item2)
session.commit()


# Menu for Thyme for that
categorie1 = Category(name="Football ")

session.add(categorie1)
session.commit()


Item1 = Item(name="Tres Leches Cake", description="Rich, luscious sponge cake soaked in sweet milk and topped with vanilla bean whipped cream and strawberries.",
                     price="2.99", category=categorie1)

session.add(Item1)
session.commit()

Item2 = Item(name="Mushroom risotto", description="Portabello mushrooms in a creamy risotto",
                     price="5.99",  category=categorie1)

session.add(Item2)
session.commit()

Item3 = Item(name="Honey Boba Shaved Snow", description="Milk snow layered with honey boba, jasmine tea jelly, grass jelly, caramel, cream, and freshly made mochi",
                     price="4.50", category=categorie1)

session.add(Item3)
session.commit()

Item4 = Item(name="Cauliflower Manchurian", description="Golden fried cauliflower florets in a midly spiced soya,"+
             "garlic sauce cooked with fresh cilantro, celery, chilies,ginger & green onions",
                     price="6.95", category=categorie1)

session.add(Item4)
session.commit()

Item5 = Item(name="Aloo Gobi Burrito", description="Vegan goodness. Burrito filled with rice, garbanzo beans, curry sauce,"+
                                             "potatoes (aloo), fried cauliflower (gobi) and chutney. Nom Nom",
                     price="7.95",  category=categorie1)

session.add(Item5)
session.commit()

Item2 = Item(name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     price="6.80",  category=categorie1)

session.add(Item2)
session.commit()


# Menu for Tony's Bistro
categorie1 = Category(name="Tennis ")

session.add(categorie1)
session.commit()


Item1 = Item(name="Shellfish Tower", description="Lobster, shrimp, sea snails, crawfish, stacked into a delicious tower",
                     price="13.95",  category=categorie1)

session.add(Item1)
session.commit()

Item22 = Item(name="Chicken and Rice", description="Chicken... and rice",
                     price="4.95", category=categorie1)

session.add(Item22)
session.commit()

Item32 = Item(name="Mom's Spaghetti", description="Spaghetti with some incredible tomato sauce made by mom",
                     price="6.95", category=categorie1)

session.add(Item32)
session.commit()

Item42 = Item(name="Choc Full O\' Mint (Smitten\'s Fresh Mint Chip ice cream)",
                     description="Milk, cream, salt, ..., Liquid nitrogen magic", price="3.95", category=categorie1)

session.add(Item4)
session.commit()

Item5 = Item(name="Tonkatsu Ramen", description="Noodles in a delicious pork-based broth with a soft-boiled egg",
                     price="7.95", category=categorie1)

session.add(Item5)
session.commit()


# Menu for Andala's
categorie1 = Category(name="Rock Climbing")

session.add(categorie1)
session.commit()


Item1 = Item(name="Lamb Curry", description="Slow cook that thang in a pool of tomatoes, onions and alllll those tasty Indian spices. Mmmm.",
                     price="9.95",  category=categorie1)

session.add(Item1)
session.commit()

Item2 = Item(name="Chicken Marsala", description="Chicken cooked in Marsala wine sauce with mushrooms",
                     price="7.95", category=categorie1)

session.add(Item2)
session.commit()

Item3 = Item(name="Potstickers", description="Delicious chicken and veggies encapsulated in fried dough.",
                     price="6.50", category=categorie1)

session.add(Item3)
session.commit()

Item4 = Item(name="Nigiri Sampler", description="Maguro, Sake, Hamachi, Unagi, Uni, TORO!",
                     price="6.75", category=categorie1)

session.add(Item4)
session.commit()

item21 = Item(name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     price="7.00", category=categorie1)

session.add(item21)
session.commit()


# Menu for Auntie Ann's
categorie1 = Category(name="Frisbee ")

session.add(categorie1)
session.commit()

Item9 = Item(name="Chicken Fried Steak", description="Fresh battered sirloin steak fried and smothered with cream gravy",
                     price="8.99",  category=categorie1)

session.add(Item9)
session.commit()


Item1 = Item(name="Boysenberry Sorbet", description="An unsettlingly huge amount of ripe"+
             "berries turned into frozen (and seedless) awesomeness",
                     price="2.99", category=categorie1)

session.add(Item1)
session.commit()

Item2 = Item(name="Broiled salmon", description="Salmon fillet marinated with fresh herbs and broiled hot & fast",
                     price="10.95", category=categorie1)

session.add(Item2)
session.commit()

Item3 = Item(name="Morels on toast (seasonal)", description="Wild morel mushrooms fried in butter, served on herbed toast slices",
                     price="7.50", category=categorie1)

session.add(Item3)
session.commit()

Item4 = Item(name="Tandoori Chicken", description="Chicken marinated in yoghurt and seasoned with a spicy"+
             "mix(chilli, tamarind among others) and slow cooked in a cylindrical clay or metal"+
             "oven which gets its heat from burning charcoal.",
                     price="8.95",  category=categorie1)

session.add(Item4)
session.commit()

Item2 = Item(name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     price="9.50",  category=categorie1)

session.add(Item2)
session.commit()

Item10 = Item(name="Spinach Ice Cream", description="vanilla ice cream made with organic spinach leaves",
                      price="1.99",  category=categorie1)

session.add(Item10)
session.commit()


# Menu for Cocina Y Amor
categorie1 = Category(name="Boxe ")

session.add(categorie1)
session.commit()


Item1 = Item(name="Super Burrito Al Pastor", description="Marinated Pork, Rice, Beans, Avocado, Cilantro, Salsa, Tortilla",
                     price="5.95", category=categorie1)

session.add(Item1)
session.commit()

Item2 = Item(name="Cachapa", description="Golden brown, corn-based Venezuelan pancake; usually stuffed with queso telita or queso de mano, and possibly lechon. ",
                     price="7.99", category=categorie1)

session.add(Item2)
session.commit()


categorie1 = Category(name="Racing")
session.add(categorie1)
session.commit()

Item1 = Item(name="Chantrelle Toast", description="Crispy Toast with Sesame Seeds slathered with buttery chantrelle mushrooms",
                     price="5.95", category=categorie1)

session.add(Item1)
session.commit

Item1 = Item(name="Guanciale Chawanmushi", description="Japanese egg custard served hot with spicey Italian Pork Jowl (guanciale)",
                     price="6.95",  category=categorie1)

session.add(Item1)
session.commit()


Item1 = Item(name="Lemon Curd Ice Cream Sandwich", description="Lemon Curd Ice Cream Sandwich on a chocolate macaron with cardamom meringue and cashews",
                     price="4.25",  category=categorie1)

session.add(Item1)
session.commit()


print "added items!"
