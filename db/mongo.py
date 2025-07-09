import os
from typing import List
from pymongo import MongoClient, ASCENDING
from pymongo.collection import Collection
from dotenv import load_dotenv
from models import NormalizedHost

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB = os.getenv("MONGO_DB", "silk_pipeline")
MONGO_COLLECTION = "hosts"


class MongoDBClient:
    def __init__(self):
        self.client = MongoClient(MONGO_URI)
        self.db = self.client[MONGO_DB]
        self.collection: Collection = self.db[MONGO_COLLECTION]
        self._ensure_indexes()

    def _ensure_indexes(self):
        self.collection.create_index([("hostname", ASCENDING)])
        self.collection.create_index([("ip_addresses", ASCENDING)])
        self.collection.create_index([("mac_addresses", ASCENDING)])
        self.collection.create_index([("agent_id", ASCENDING)])
        self.collection.create_index([("vendor", ASCENDING)])

    def save_hosts(self, hosts: List[NormalizedHost]):
        for host in hosts:
            # Convert model to dict
            doc = host.dict()

            # Convert IP address objects to strings
            doc["ip_addresses"] = [str(ip) for ip in doc.get("ip_addresses", [])]

            # Convert MAC address objects to strings (if they are not already)
            doc["mac_addresses"] = [str(mac) for mac in doc.get("mac_addresses", [])]
            
            # Perform an upsert (replace if exists, insert otherwise)
            self.collection.update_one(
                {"hostname": host.hostname, "vendor": host.vendor},
                {"$set": doc},
                upsert=True
            )

    def fetch_all_hosts(self) -> List[NormalizedHost]:
        return [NormalizedHost(**doc) for doc in self.collection.find()]
