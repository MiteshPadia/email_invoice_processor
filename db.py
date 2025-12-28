# db.py

from pymongo import MongoClient
from config import MONGO_URI, MONGO_DB, MONGO_COLLECTION

# Create MongoDB connection
client = MongoClient(MONGO_URI)
db = client[MONGO_DB]
collection = db[MONGO_COLLECTION]


def save_attachment_metadata(metadata: dict) -> None:
    """
    Saves basic  information to MongoDB.
    """
    collection.insert_one(metadata)


def get_all_attachments():
    """
    Returns all  records.
    """
    return list(collection.find({}, {"_id": 0}))
