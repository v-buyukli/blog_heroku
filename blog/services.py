import os
import csv

from django.conf import settings


def get_blogs():
    with open(os.path.join(settings.BASE_DIR, "publications.csv"), "r") as csvfile:
        blogs = {}
        next(csvfile)
        for row in csv.reader(csvfile):
            blogs[row[0]] = {"title": row[1], "content": row[2], "updated_at": row[3]}
    return blogs
