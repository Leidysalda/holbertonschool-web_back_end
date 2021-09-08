#!/usr/bin/env python3
"""  Log stats
"""
from pymongo import MongoClient


if __name__ == "__main__":
    """ stats about Nginx logs stored in MongoDB
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    print("{} logs".format(collection.estimated_document_count()))

    print("Methods:")

    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        method_count = collection.count_documents({'method': method})
        print("\t method {}: {}".format(method, method_count))

    check_get = collection.count_documents(
        {'method': 'GET', 'path': "/status"})
    print("{} status check".format(check_get))
