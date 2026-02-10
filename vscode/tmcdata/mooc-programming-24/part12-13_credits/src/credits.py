#!/usr/bin/env python 3

from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

def sum_of_all_credits(attempts: list):
    return reduce(lambda sum, item: sum + item.credits, attempts, 0)

def sum_of_passed_credits(attempts: list):
    filtered_list = filter(lambda x: x.grade > 0, attempts)
    return reduce(lambda sum, item: sum + item.credits, filtered_list, 0)

def average(attempts: list):
    filtered_list = list(filter(lambda x: x.grade >= 1, attempts))
    return reduce(lambda sum, item: sum + item.grade, filtered_list, 0) / len(filtered_list)

if __name__ == "__main__":
    attempt = CourseAttempt("Data Structures and Algorithms", 3, 10)
    print(attempt)
    print(attempt.course_name)
    print(attempt.credits)
    print(attempt.grade)

    print("")

    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    
    credit_sum = sum_of_all_credits([s1, s2, s3])
    print(credit_sum)

    print("")

    credit_sum = sum_of_passed_credits([s1, s2, s3])
    print(credit_sum)

    print("")

    ag = average([s1, s2, s3])
    print(ag)
