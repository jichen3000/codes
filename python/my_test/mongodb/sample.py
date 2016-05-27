from pymongo import MongoClient

# import 
# mongoimport --db test --collection restaurants --drop --file primer-dataset.json

# default is your localhost
client = MongoClient()
# client = MongoClient("mongodb://localhosts:27019")

db = client.test

from datetime import datetime
result = db.restaurants.insert_one(
    {
        "address": {
            "street": "2 Avenue",
            "zipcode": "10075",
            "building": "1480",
            "coord": [-73.9557413, 40.7720266]
        },
        "borough": "Manhattan",
        "cuisine": "Italian",
        "grades": [
            {
                "date": datetime.strptime("2014-10-01", "%Y-%m-%d"),
                "grade": "A",
                "score": 11
            },
            {
                "date": datetime.strptime("2014-01-16", "%Y-%m-%d"),
                "grade": "B",
                "score": 17
            }
        ],
        "name": "Vella",
        "restaurant_id": "41704620"
    }
)

result.inserted_id
ObjectId('5724b88efc1c0f17f1be1b6b')

cursor = db.restaurants.find()
for document in cursor:
    print(document)

# Query by a Top Level Field
cursor = db.restaurants.find({"borough": "Manhattan"})
for document in cursor:
    print(document)

# Query by a Field in an Embedded Document
cursor = db.restaurants.find({"address.zipcode": "10075"})
docs = [d for d in cursor]


# Query by a Field in an Array
cursor = db.restaurants.find({"grades.grade": "B"})
# only take one
cursor.next()

# Specify Conditions with Operators
# larger
cursor = db.restaurants.find({"grades.score": {"$gt": 30}})

# less
cursor = db.restaurants.find({"grades.score": {"$lt": 10}})

# and
cursor = db.restaurants.find({"cuisine": "Italian", "address.zipcode": "10075"})

# or
cursor = db.restaurants.find(
    {"$or": [{"cuisine": "Italian"}, {"address.zipcode": "10075"}]})

# sort
import pymongo
cursor = db.restaurants.find({"cuisine": "Italian", "address.zipcode": "10075"}).sort([
    ("borough", pymongo.ASCENDING),
    ("address.zipcode", pymongo.ASCENDING)
])

# update one
cursor = db.restaurants.find({"name": "Juni"})
cursor.count()
cursor.next()
result = db.restaurants.update_one(
    {"name": "Juni"},
    {
        "$set": {
            "cuisine": "American (New)"
        },
        "$currentDate": {"lastModified": True}
    }
)

result.matched_count
result.modified_count

cursor = db.restaurants.find({"name": "Juni"})
cursor.count()
cursor.next()

# Update an Embedded Field
result = db.restaurants.update_one(
    {"restaurant_id": "41156888"},
    {"$set": {"address.street": "East 31st Street"}}
)

# Update Multiple Documents
cursor = db.restaurants.find({"address.zipcode": "10016", "cuisine": "Other"})
cursor.count()
cursor.next()

result = db.restaurants.update_many(
    {"address.zipcode": "10016", "cuisine": "Other"},
    {
        "$set": {"cuisine": "Category To Be Determined"},
        "$currentDate": {"lastModified": True}
    }
)

result.matched_count
result.modified_count

# replace the entire document except for the _id field
cursor = db.restaurants.find({"restaurant_id": "41704620"})
cursor.count()
cursor.next()
result = db.restaurants.replace_one(
    {"restaurant_id": "41704620"},
    {
        "name": "Vella 2",
        "address": {
            "coord": [-73.9557413, 40.7720266],
            "building": "1480",
            "street": "2 Avenue",
            "zipcode": "10075"
        }
    }
)
result.matched_count
result.modified_count

# delete one and delete many
cursor = db.restaurants.find({"borough": "Manhattan"})
cursor.count()
cursor.next()

result = db.restaurants.delete_one({"borough": "Manhattan"})
result.deleted_count
result = db.restaurants.delete_many({"borough": "Manhattan"})
result.deleted_count

db.restaurants.drop()
db.restaurants.count()

# group
cursor = db.restaurants.aggregate(
    [
        {"$group": {"_id": "$borough", "count": {"$sum": 1}}}
    ]
)
cursor.next()
# the cursor cannot use 
cursor.count()

# match
cursor = db.restaurants.aggregate(
    [
        {"$match": {"borough": "Queens", "cuisine": "Brazilian"}},
        {"$group": {"_id": "$address.zipcode", "count": {"$sum": 1}}}
    ]
)

# index
import pymongo
db.restaurants.create_index([("cuisine", pymongo.ASCENDING)])

db.restaurants.create_index([
    ("cuisine", pymongo.ASCENDING),
    ("address.zipcode", pymongo.DESCENDING)
])



