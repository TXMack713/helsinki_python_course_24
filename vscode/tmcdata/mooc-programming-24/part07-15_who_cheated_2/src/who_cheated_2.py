#!/usr/bin/env python3

import csv

def final_points():
    start_times = []
    exam_times = []

    # Create a list of the students and their start times
    with open("start_times.csv") as start_file:
        for line in csv.reader(start_file, delimiter=";"):
            start_times.append(line)
            # print(f"Line: {line}")

    # Create a list of the exam times for each student
    with open("submissions.csv") as submissions_file:
        for line in csv.reader(submissions_file, delimiter=";"):
            exam_times.append(line)
            # print(f"Line: {line}")
    
    students = {}
    submissions = {}
    # Create a dictionary of the students and their start times
    for student in start_times:
        # print(f"Student: {student}")
        students[str(student[0])] = student[1]
        submissions[str(student[0])] = []

    # Create a dictionary of all the submissions from each student ordered by task, points awarded, submission time
    for submission in exam_times:
        submissions[submission[0]].append((submission[1], submission[2], submission[3]))
    
    '''for submitter, submitted in submissions.items():
        print(f"Submitter's exam start time: {str(students[str(submitter)])}")
        print(f"Submitter: {submitter} : {submitted}")'''

    assignments = {}
    print(f"Total submitters: {len(submissions.keys())}")

    # For each student, create a dictionary of their task and points, if their submission was submitted on time
    for submitter, entry in submissions.items():
        # print(f"Submitter: {submitter}")
        # print(f"Submitter's exam start time: {str(students[str(submitter)])}")
        points = {}
        start = students[str(submitter)].split(":")
        for exam in entry:
            submit_time = exam[2].split(":")
            if (int(submit_time[0]) - int(start[0])) > 3:
                # points[exam[0]] = 0
                continue
            elif (int(submit_time[0]) - int(start[0])) < 3:
                if exam[0] not in points:
                    points[exam[0]] = int(exam[1])
                else:
                    if int(exam[1]) >= int(points.get(exam[0])):
                        points[exam[0]] = int(exam[1])        
            else:
                if (int(submit_time[1]) - int(start[1])) > 0:
                    # points[exam[0]] = 0            
                    continue
        point_total = 0
        for task, points in points.items():
            point_total += points
        assignments[str(submitter)] = point_total

    print(assignments)
    
    return assignments

if __name__ == "__main__":
    final_points()
