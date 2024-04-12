#!/usr/bin/env python3

"""
A Python function that lists all documents in a collection:
    * Prototype: def list_all(mongo_collection):
    * Return an empty list if no document in the collection
    * mongo_collection will be the pymongo collection object
"""

from pymongo import MongoClient


def list_all(mongo_collection):
    """  lists all documents in a collection """
    return mongo_collection.find()
