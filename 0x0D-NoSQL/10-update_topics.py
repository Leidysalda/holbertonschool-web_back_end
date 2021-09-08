#!/usr/bin/env python3
""" Change school topics
"""


def update_topics(mongo_collection, name, topics):
    """ Function that changes all topics of a school
    document based on the name
    """

    my_query = {'name': name}
    value = {'$set': {'topics': topics}}
    mongo_collection.update_many(my_query, value)
