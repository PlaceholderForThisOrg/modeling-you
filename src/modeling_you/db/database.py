from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi

from modeling_you.configs import mongo

client = AsyncIOMotorClient(mongo.URI, server_api=ServerApi("1"))
database = client.get_database(name=mongo.DATABASE)
collection = database.get_collection(name=mongo.COLLECTION)
