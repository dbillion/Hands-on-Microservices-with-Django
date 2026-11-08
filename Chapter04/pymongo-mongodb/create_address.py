from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

os.environ.get('MONGO_URI', 'mongodb://localhost:27017')
client = MongoClient(con, server_api=ServerApi('1'))
db = client["Subscription"]
col = db["subscription_address"]

address = {"name": "Monthy Python",
           "address": "Hardwood Lane",
           "postalcode": "MP1"
           "city": "London",
           "country": "England"
           "email": "monthy@python.com"
           }
col.insert_one(address)
