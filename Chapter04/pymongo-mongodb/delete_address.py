from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

os.environ.get('MONGO_URI', 'mongodb://localhost:27017')
client = MongoClient(con, server_api=ServerApi('1'))
db = client["Subscription"]
col = db["subscription_address"]

col.delete_one({"name": "Monthy Python"})
