#!/usr/bin/env python3
""" Script that provides some stats about Nginx logs stored in MongoDB """
from pymongo import MongoClient


def display_information(mongo_collection):
    """ Fx that provides some stats about Nginx logs """
    print("{} logs".format(mongo_collection.count_documents({})))
    print("Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for method in methods:
        print("\tmethod {}: {}".format(
            method, mongo_collection.count_documents({"method": method})))

    print("{} status check".format(mongo_collection.count_documents(
        {"method": methods[0], "path": "/status"})))


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    display_information(nginx_collection)
