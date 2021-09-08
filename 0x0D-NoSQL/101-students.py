#!/usr/bin/env python3
""" 14. Top students
"""


def top_students(mongo_collection):
    """ Function that returns all students sorted by average score
    """return mongo_collection.aggregate([
        {
            '$project': {
                'name': '$name',
                'averageScore': {
                    '$avg': "$topics.score"
                }
            }
        },
        {
            '$sort': {
                "average": -1
            }
        }
    ])