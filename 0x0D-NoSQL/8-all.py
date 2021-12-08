#!/usr/bin/env python3
""" Function to list all documents in Python """


def list_all(mongo_collection):
    """ Method to list all documents in a collection """
    if not mongo_collection:
        return []
    return mongo_collection.find()
