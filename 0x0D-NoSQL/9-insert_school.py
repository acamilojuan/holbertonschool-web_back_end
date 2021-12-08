#!/usr/bin/env python3
""" Python fx to insert a new doc in a collection of kwargs """


def insert_school(mongo_collection, **kwargs):
    """ Method to insert new doc in collection of kwargs """
    new_doc = mongo_collection.insert_one(kwargs)
    return new_doc.inserted_id
