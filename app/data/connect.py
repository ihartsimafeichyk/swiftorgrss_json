from app import app
from pymongo import MongoClient
from flask_pymongo import PyMongo

# DB connector
class Connect(object):
    @staticmethod
    def get_connection():
        app.config["MONGO_URI"] = "mongodb+srv://root:Asd123!.@tmclaster.9ebrd.mongodb.net/swiftorgdb?retryWrites=true&w=majority"
        return PyMongo(app)
