
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

# Data Modeling with Postgres for Sparkify

This project is designed to help the company Sparkify analyze the data they have been collecting on songs and user activity on their music streaming app, it aims at helping the company undertand what songs their users are listening and get other relevant information on their users activity.

## Dataset available

**Song Dataset**

The first dataset is a subset of real data from the Million Song Dataset. Each file is in JSON format and contains metadata about a song and the artist of that song. The files are partitioned by the first three letters of each song's track ID. For example, here are filepaths to two files in this dataset.

    `song_data/A/B/C/TRABCEI128F424C983.json`
    `song_data/A/A/B/TRAABJL12903CDCF1A.json`
And below is an example of what a single song file, `TRAABJL12903CDCF1A.json`, looks like.

``{"num_songs": 1, "artist_id": "ARJIE2Y1187B994AB7", "artist_latitude": null, "artist_longitude": null, "artist_location": "", "artist_name": "Line Renaud", "song_id": "SOUPIRU12A6D4FA1E1", "title": "Der Kleine Dompfaff", "duration": 152.92036, "year": 0}``

**Log Dataset**

The second dataset consists of log files in JSON format generated by this event simulator based on the songs in the dataset above. These simulate activity logs from a music streaming app based on specified configurations.

The log files in the dataset are partitioned by year and month. For example, here are filepaths to two files in this dataset.

`log_data/2018/11/2018-11-12-events.json`
`log_data/2018/11/2018-11-13-events.json`

## Setup Instructions and Steps to follow

The project includes the following files:
1. test.ipynb displays the first few rows of each table to let you check your database.
2. create_tables.py drops and creates your tables. Run this file to reset the tables.
3. etl.ipynb reads and processes a single file from song_data and log_data and loads the data into the tables. This notebook contains detailed instructions on the ETL process for each of the tables.
4. etl.py reads and processes files from song_data and log_data and loads them into the tables.
5. sql_queries.py contains all sql queries, and is imported into the last three files above.
    
**Requirements**

1. Make sure you have Jupyter notebook, python and sql server installed on your computer.
2. The following python libraries `pip`, `psycopg2`, `panda`, `glob` are required to run the program.

## Program execution
In order to successfully run this project, below are the steps to follow:

1. Open test.ipynb and execute each line in sequential order.
2. Run the first line to load sql extension.
3. Run the next line which runs create_tables.py in order to create the database and tables
4. The next line will run etl.py to process the data and populate the tables
5. Connect to the database by running the next line and execute rest of the queries to analyze data from the database.

## Schema Design

**Fact Table**
1. **songplays** - records in log data associated with song plays i.e. records with page `NextSong`
    Attributes: `songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent`
    
**Dimension Tables**
1. **users** - users in the app 
    Attributes: `user_id, first_name, last_name, gender, level`
2. **songs** - songs in music database
    Attributes: `song_id, title, artist_id, year, duration`
3. **artists** - artists in music database
    Attributes: `artist_id, name, location, latitude, longitude`
4. **time** - timestamps of records in songplays broken down into specific units
    Attributes: `start_time, hour, day, week, month, year, weekday`
    
## Purpose of this database

The database sparkifydb enables Sparkify analysts to get relevant information on their users activities. It contains the following databases: `songplays, users, songs, artists,` and `time`. These table contain information that has been processed from the raw data collected from the app into files. Then, the processed info has been transferred to the tables in the appropriate formats in order to enable analysts to write queries and access the information they need directly.
Fact Table

1. Database Schema design and ETL Pipeline

    The database is organized into fact and dimension tables in order to simplify queries. The fact table `songplays` contains records processed from log data associated with song plays, and the it has the following fields or columns:
```songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent```.
    The dimension tables are ```users, songs, artists,``` and ```time```, and organized as follow:
`users` table: ```user_id, first_name, last_name, gender, level```
`songs` table: ```song_id, title, artist_id, year, duration```
`artists` table: ```artist_id, name, location, latitude, longitude```
`time` table: ```start_time, hour, day, week, month, year, weekday```
    The fact table ```songplays``` is related to others table through keys such as ```song_id, artist_id, user_id, start_time```, this allows analysts to retrieve additional information from other tables using the keys when needed. For example if an analyst needs to know what song was listened by a given user at a given day using the songplay table, the key ```song_id``` can be used to retrieve the song name from the ```songs``` table, ```user_id``` to retrieve the user name and ```star_time``` the day. 
    The ETL Pipeline extracts data from the source folders and files ```data/...``` of the app, transforms the raw data according to the tables schema described above and loads it into datatype that correspond the given table schema. This avoids having to deal with unnecessary data such as ```method```, ```registration```, etc that do not help achieve the analytical goal which is to know what songs users are listening to. 
    
3. Example queries and results for song play analysis

    Query to know list of songs and artists listened by women in the month of november.
       ``` %sql SELECT name AS Artist, title AS song FROM ((songplays JOIN users ON songplays.user_id = users.user_id) JOIN artists ON songplays.artist_id = artists.artist_id) JOIN songs ON songplays.song_id = songs.song_id WHERE gender='F' AND month = 11 GROUP BY(Artist, Song) ```
    #### Result

|Artist|Song|
|------|------|
|Marc Shaiman|City Slickers|
|------|------|



