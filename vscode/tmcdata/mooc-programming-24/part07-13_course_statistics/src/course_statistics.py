#!/usr/bin/env python3

import urllib.request, json
def retrieve_all():
    my_request = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")

    data = my_request.read()
    course_info = json.loads(data)
    # print(f"Course info: {course_info}")
    list_of_courses = []

    for entry in course_info:
        # print(f"Current entry: {entry}")
        if entry["enabled"] == True:
            fullName = entry["fullName"]
            name = entry["name"]
            year = entry["year"]
            sum = 0
            for value in entry["exercises"]:
                sum += value
            list_of_courses.append((fullName, name, year, sum))
    return list_of_courses

def retrieve_course(course_name: str):
    url = "https://studies.cs.helsinki.fi/stats-mock/api/courses/****/stats"
    new_url = url.replace("****", course_name)
    my_request = urllib.request.urlopen(url)

print(retrieve_all())
# print(my_request.read())
