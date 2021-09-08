#!/usr/bin/env python3
""" List all documents in Python
"""
import pymongo


def list_all(mongo_collection):
    """ Function that lists all documents in a collection
    """

    cursor = mongo_collection.find({})
    return cursor
