#!/usr/bin/env python3
""" Python fx to change all topics of a school doc by name """


def update_topics(mongo_collection, name, topics):
    """ Method to change all topics of school doc by name """
    return mongo_collection.update_many({"name": name},
                                        {"$set": {"topics": topics}})
