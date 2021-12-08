#!/usr/bin/env python3
""" Fx that returns the list of school having a specific topic """


def schools_by_topic(mongo_collection, topic):
    """ Method to return the list of school having a specific topic """
    return mongo_collection.find({"topics": {"$in": [topic]}})
