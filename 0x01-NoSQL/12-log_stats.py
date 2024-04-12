#!/usr/bin/env python3

"""
Write a Python script that provides some stats about Nginx logs stored in
 MongoDB:
    * Database: logs
    * Collection: nginx
    * Display (same as the example):
    * first line: x logs where x is the number of documents in this collection
    * second line: Methods:
    * 5 lines with the number of documents with the method = ["GET", "POST", "PUT", "PATCH", "DELETE"] in this order (se        e example below - warning: it’s a tabulation before each line)
    * one line with the number of documents with:
    * method=GET
    * path=/status
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
