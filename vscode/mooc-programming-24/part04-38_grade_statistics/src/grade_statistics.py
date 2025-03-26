# Write your solution here
import math
def gather_data():
    exam_points = []
    exercises_completed = []
    points = []
    count = 0
    while True:
        response = input("Exam points and exercises completed: ")
        if response == "":
            break
        else:
            response_list = response.split(" ")
            if len(response_list) == 2:
                exam_points.append(int(response_list[0]))
                exercises_completed.append(int(response_list[1]))
    
    for x in exercises_completed:
        point = int(x / 10)
        points.append(point)
    
    zeroes = 0
    ones = 0
    twos = 0
    threes = 0
    fours = 0
    fives = 0       
        
    grades = []
    
    while count < len(exam_points):
        grade = exam_points[count]+points[count]
        if exam_points[count] < 10 or grade < 15:
            zeroes += 1
        elif grade >= 15 and grade < 18:
            ones += 1
        elif grade >= 18 and grade < 21:
            twos += 1
        elif grade >= 21 and grade < 24:
            threes += 1
        elif grade >=24 and grade < 28:
            fours += 1
        elif grade >= 28 and grade <= 30:
            fives += 1
        grades.append(grade)
        count += 1
    letter_grade = [zeroes, ones, twos, threes, fours, fives]
    all_grades = [grades, letter_grade]
    # print(all_grades)
    return all_grades

def pass_percentage(grades: list):
    count = 0
    sum = 0
    total = 0
    failed = grades[0]
    for x in grades:
        sum += x
        total += x
    percent = ((sum-failed)/total)*100
    return f"{percent:.1f}"
    
def points_average(all_points: list):
    total = 0
    for x in all_points:
        total += x
    average = total / len(all_points)
    return average

def grades_distribution(grades):
    print("Grade distribution:")
    print("  5:", grades[5]*"*")
    print("  4:", grades[4]*"*")
    print("  3:", grades[3]*"*")
    print("  2:", grades[2]*"*")
    print("  1:", grades[1]*"*")
    print("  0:", grades[0]*"*")

def statistics(pass_rate, average, grades):
    print("Statistics:")
    print("Points average:", average)
    print("Pass percentage:", pass_rate)
    grades_distribution(grades)

def main():
    student_grades = gather_data()
    grades_average = points_average(student_grades[0])
    student_pass_rate = pass_percentage(student_grades[1])
    statistics(student_pass_rate, grades_average, student_grades[1])

main()


