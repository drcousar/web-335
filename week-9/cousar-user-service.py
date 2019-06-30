#============================================
# Title:  Assignment 9.2
# Author: Don Cousar
# Date:   29 June 2019
# Description: Querying and Creating Documents
#===========================================
# Imports

from pymongo import MongoClient
import pprint
import datetime

# Connect to local MongoDB
client = MongoClient('localhost', 27017)

print(client)

db = client.web335

user = {

    "first_name": "Claude",
    "last_name": "Debussy",
    "email": "cdebussy@me.com",
    "employee_id": "0000008",
    "date_created": datetime.datetime.utcnow()

}

# Insert User
user_id = db.users.insert_one(user).inserted_id

# Print insert statement
print(user_id)

# Query user
pprint.pprint(db.users.find_one({"employee_id": "0000008"}))