import pymongo
from pymongo import MongoClient
import pprint

client = MongoClient('127.0.0.1:9984')
db = client.test_database
posts= db.digital_asset_payload
pprint.pprint(posts.find_one({"api":"v1"}))
