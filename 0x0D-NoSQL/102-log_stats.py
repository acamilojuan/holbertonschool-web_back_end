#!/usr/bin/env python3
""" Improving 12-log_stats.py adding the top 10 of the most present IPs in nginx database logs """


def top_students(mongo_collection):
    """ FX to return all students sorted by average score """

    top_student = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])

    return top_student
