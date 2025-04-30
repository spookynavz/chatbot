from pymongo import MongoClient
from datetime import datetime, timezone

class ChatDB:
    def __init__(self, db_name="chatbot_db", collection="conversations"):
        self.client = MongoClient("mongodb://localhost:27017")
        self.db = self.client[db_name]
        self.collection = self.db[collection]

    def save_message(self, session_id, role, message):
        self.collection.insert_one({
            "session_id": session_id,
            "role": role,
            "message": message,
            "timestamp": datetime.now(timezone.utc)
        })

    def get_last_messages(self, session_id, limit=10):
        messages = self.collection.find(
            {"session_id": session_id}
        ).sort("timestamp", -1).limit(limit)
        return list(reversed(list(messages)))

