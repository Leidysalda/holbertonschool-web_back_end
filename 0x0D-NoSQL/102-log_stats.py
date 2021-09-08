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

    for method in ["GET". "POST", "PUT", "PATCH", "DELETE"]:
        method_count = collection.count_documents({'method': method})
        print(f"\tmethod {method}: {method_Count}")

    check_get = collection.count_documents(
        {'method': 'GET', 'path': "/status"})
    print(f"{check_get} status check")

    print("IPs:")
    top_ips = collections.aggregate ([
        {"$group":
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
        print(f"\t {ip.get('ip')}: {ip.get('count')}")
