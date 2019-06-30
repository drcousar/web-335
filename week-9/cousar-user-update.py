#============================================
# Title:  Assignment 9.3
# Author: Don Cousar
# Date:   29 June 2019
# Description: Updating and Deleting Documents
#===========================================
# Imports

from pymongo import MongoClient
import pprint
import datetime

# Connect to local MongoDB
client = MongoClient('localhost', 27017)

print(client)

# Select db
db = client.web335

# Update User Email
db.users.update_one(
    {"employee_id": "0000008"},
    {
        "$set": {
            "email": "drcousar@my365.bellevue.edu"
        }
    }
)

# Query user
pprint.pprint(db.users.find_one({"employee_id": "0000008"}))