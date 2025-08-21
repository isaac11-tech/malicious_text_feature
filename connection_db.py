from pymongo import MongoClient
import os

class ConnectionDB:
    def __init__(self, db_name, collection_name):
        mongo_uri_conn = os.getenv("CONN_STRING")

        uri = "mongodb+srv://IRGC:iraniraniran@iranmaldb.gurutam.mongodb.net/"#test

        # connecting to server
        self.client = MongoClient(uri)
        # select a DB
        self.db = self.client[db_name]
        # select collection
        self.collection = self.db[collection_name]

    def get_all_documents(self):
        return list(self.collection.find())

#testing
c = ConnectionDB("IranMalDB","tweets")
print(c.get_all_documents())

#mongo_uri = os.getenv("CONN_STRING")
#print("Mongo URI:", mongo_uri)

