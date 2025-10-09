# Write your solution here#!/usr/bin/env python3

from datetime import datetime
import csv

def cheaters():
    start_times = []
    exam_times = []

    with open("start_times.csv") as start_file:
        for line in csv.reader(start_file, delimiter=";"):
            start_times.append(line)
            # print(f"Line: {line}")

    with open("submissions.csv") as submissions_file:
        for line in csv.reader(submissions_file, delimiter=";"):
            exam_times.append(line)
            # print(f"Line: {line}")
    
    students = {}
    submissions = {}
    for student in start_times:
        # print(f"Student: {student}")
        students[str(student[0])] = student[1]
        submissions[str(student[0])] = []

    for submission in exam_times:
        submissions[submission[0]].append((submission[1], submission[2], submission[3]))
    
    '''for submitter, submitted in submissions.items():
        print(f"Submitter's exam start time: {str(students[str(submitter)])}")
        print(f"Submitter: {submitter} : {submitted}")'''

    cheats = []
    print(f"Total submitters: {len(submissions.keys())}")
    for submitter, entry in submissions.items():
        # print(f"Submitter: {submitter}")
        # print(f"Submitter's exam start time: {str(students[str(submitter)])}")
        start = students[str(submitter)].split(":")
        for exam in entry:
            submit_time = exam[2].split(":")
            if (int(submit_time[0]) - int(start[0])) > 3:
                print(f"{submitter} cheated")
                print(f"Start time: {str(students[str(submitter)])}")
                print(f"Task: {exam[0]}")
                print(f"Task submission time: {exam[2]}")
                cheats.append(submitter)
                break
            elif (int(submit_time[0]) - int(start[0])) < 3:
                continue
            else:
                if (int(submit_time[1]) - int(start[1])) > 0:
                    print(f"{submitter} cheated")
                    print(f"Start time: {str(students[str(submitter)])}")
                    print(f"Task: {exam[0]}")
                    print(f"Task submission time: {exam[2]}")
                    cheats.append(submitter)
                    break
    print(cheats)
    return cheats

if __name__ == "__main__":
    cheaters()
