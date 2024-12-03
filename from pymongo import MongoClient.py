from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client['test_database']
collection = db['test_collection']

def save_document(document):
    collection.insert_one(document)