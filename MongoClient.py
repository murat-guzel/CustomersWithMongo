from pymongo import MongoClient
import urllib.request, json
with urllib.request.urlopen("http://127.0.0.1:8000/customer/") as url:
    data = json.loads(url.read().decode())
    print(data[0])


client = MongoClient()
db = client.python

for itemData in data:
    result = db.customers.insert_one(itemData)
    print(result.inserted_id)

document = db.customers.find()

for item in document:
    print("id : ",str(item["id"]))
    print("userId : ",str(item["userId"]))
    print("userName : ",str(item["userName"]))


db.customers.drop()

input()