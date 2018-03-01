import pymongo
from bigchaindb_driver import BigchainDB
from pymongo import MongoClient
import pprint

client = MongoClient('127.0.0.1:9984')
root_url = 'http://127.0.0.1:9984/api/v1/transactions/32a184631b7cc4f2878540450f465d82c275f61ce5e4a3c22c840666987e1591'
db = BigchainDB(root_url)
assets= db.assets
print(assets.get(search ='asset'))
