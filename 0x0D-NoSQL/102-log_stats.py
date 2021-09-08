#!/usr/bin/env python3
"""  Log stats
"""
from pymongo import MongoClient


if __name__ == "__main__":
    """ stats about Nginx logs stored in MongoDB
    """
    client = MOngoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    print("{} logs".format(collection.estimated_document_count()))

    print("Methods:")

    for method in ["GET". "POST", "PUT", "PATCH", "DELETE"]:
        method_count = collection.count_documents({'methos': method})
        print("\t method {}: {}".format(method, method_count))

    check_get = collection.count_documents(
        {'method': 'GET', 'path': "/status"})
    print("{} status check".format(check_get))

    print("IPs:")
    top_ips = collections.aggregate ([
        {
            "$group":
            {
                "_id": "$ip",
                "count": {"$sum": 1}
            }
        },
        {"$sort": {"count": -1}},
        {"$limit": 10},
        {"$project": {
            "_id": 0,
            "ip": "$_id",
            "count": 1
        }} 
    ])

    for ip in top_ips:
        print("\t {}: {}".format(ip.get('ip'), ip.get('count')))
