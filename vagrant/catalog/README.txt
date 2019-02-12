# catalog


Project Title 
catalog Project (Star Trek Universe)


Description
This app implements a category-item hierarchy using the Star Trek (The Next Generation) universe to represent species as categories
and species members as items. This app allows for Create Update and Delete of species members.  The update/delete/create functionality
requires login using the Google Oauth provider.  The create/delete/update functionality also preserves separate user spaces, and only allows
item creators to edit and delete those items. 


App Structure
URL's for seeing all species/members:
http://localhost:8000/species/
JSON representation of the catalog including all species and users:
http://localhost:8000/species.json
URL for seeing members associated with a  certain species (example):
http://localhost:8000/El-Aurians/Members/
URL for individual member:
http://localhost:8000/El-Aurians/Gouda/
URL for adding a new member:
http://localhost:8000/newmember/
URL for editing a member:
http://localhost:8000/Ko%27ar/edit
URL for deleting a member:
http://localhost:8000/Ko%27ar/delete


Getting Started
Step 1) create schema and data records in catalog.db (see Prerequisites section below)
Step 2) run 'python application.py'
Step 3) navigate browser to localhost:8000


Prerequisites
Step 1) run 'python database_setup.py'
Step 2) run 'python database_populate.py'


Built With
Python 2.7.12
styles.css  and other code samples adapted from Udacity restaurant application


Authors
Andrei Badulescu


References used for character (member) descriptions
https://www.cbr.com/star-trek-characters-ranking/
http://www.startrek.com/database_article/locutus
https://memory-alpha.fandom.com/wiki/El-Aurian