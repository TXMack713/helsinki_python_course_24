#!/usr/bin/env python3

import urllib.request, json, math
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
    # try:
    url = "https://studies.cs.helsinki.fi/stats-mock/api/courses/****/stats"
    new_url = url.replace("****", course_name)
    my_request = urllib.request.urlopen(new_url)
    data = my_request.read()
    course_info = json.loads(data)
    my_dict = {}
    weeks = 0
    students_max = 0
    hours = 0
    hours_average = 0
    exercises = 0
    exercises_average = 0
    for keys, values in course_info.items():
        weeks += 1
        if course_info[keys]["students"] > students_max:
            students_max = course_info[keys]["students"]
        hours += course_info[keys]["hour_total"]
        exercises += course_info[keys]["exercise_total"]
    hours_average = math.floor(hours / students_max)
    exercises_average = math.floor(exercises / students_max)
    my_dict["weeks"] = weeks
    my_dict["students"] = students_max
    my_dict["hours"] = hours
    my_dict["hours_average"] = hours_average
    my_dict["exercises"] = exercises
    my_dict["exercises_average"] = exercises_average    
    
    return my_dict
    
    # except:
    #     print(f"An error occurred, there's no course named {course_name}")
    # return None

if __name__ == "__main__":
    print(retrieve_all())
    course = input("Please enter the course name:")
    print(retrieve_course(course))
    # print(my_request.read())
