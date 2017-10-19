
#  Item Catalog Application 



To launch the program,

1. Make sure that you have python installed on your computer
2. Make sure that you have psycopg2 library installed
3. Make sure that you're in the right directory and run database_setup.py file by typing
   `python database_setup.py` in order to create the database and tables for the application
4. Then, populate the application's database by running the file lotofitems.py following the 
   same procedure to run a python code. 
5. Open the file item_catalog.py with IDLE (Right-click
   on the file and choose "Open with IDLE")
   and Click on "Run" from the menu bar in the IDLE then choose "Run Module" option.
6. Or if you have git bash terminal and a virtual machine on your computer, 
   make sure that your are in the program's directory and launch it from the
   terminal by typing `python item_catalog.py` 
7. The program should launch and display the port number on which the applicat is running.
8. Open your web browser and type the URL address: localhost:port_number to open the application
9. You should see the application running displaying some categories
10. Click on `login` to go to the login page and login using Google or Facebook credentials 
	Or register in the application by clicking on the link `Register` on the login page
11. Once You are logged in, you can add, edit or delete an item or a category.
12.	To view JSON endpoint for categories or items data, enter the following URL:
	*	`localhost:port_number/category/<int:category_id>/item/JSON` to display
		JSON endpoint for all items of a category in the catalog
	*	`localhost:port_number/category/<int:category_id>/JSON` to display
		JSON endpoint for an arbitrary category in the catalog
	*	`localhost:port_number/category/<int:category_id>/item/<int:item_id>/JSON` 
		to display JSON endpoint for an arbitrary item in the catalog
	*	`localhost:port_number//category/JSON` to display
		JSON endpoint for all categories in the catalog.
13. You can log out from the application by clicking on the `Log out` link that is
	on the right corner of the application's bar.
	
	
	Enjoy browsing, editing and creating items from different categories!!!
