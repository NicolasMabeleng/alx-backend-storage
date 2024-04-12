#!/usr/bin/env python3

"""
Improve 12-log_stats.py by adding the top 10 of the most present IPs in the
  collection nginx of the database logs:
    * The IPs top must be sorted (like the example below)
"""

from pymongo import MongoClient


def log_stats():
    """ provides some stats about Nginx logs stored in MongoDB """
    # Connect to MongoDB
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx
    
    print(f'{collection.estimated_document_count()} logs')

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for method in methods:
        method_count = collection.count_documents({'method': method})
        print(f"\tmethod {method}: {method_count}")

    # Count status check logs
    status_check_count = collection.count_documents({"method": "GET", "path": "/status"})

    print(f"{status_check_count} status check")
    # Close the MongoDB connection
    client.close()


if __name__ == "__main__":
    """ script that provides some stats about Nginx logs stored in MongoDB """
    log_stats()
