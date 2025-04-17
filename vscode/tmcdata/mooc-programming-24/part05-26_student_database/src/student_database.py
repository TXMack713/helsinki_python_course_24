# Write your solution here
def add_student(database: dict, name: str):
    completed_courses = {}
    if name not in database:
        database[name] = completed_courses

def print_student(database: dict, name: str):
    if name not in database:
        print(f"{name}: no such person in the database")
    elif len(database[name]) == 0:
        print(f"{name}:")
        print(" no completed courses")
    elif len(database[name].items()) > 0:
        sum = 0
        count = 0
        print(f"{name}:")
        for key, value in database[name].items():
            if value == 0:
                continue
            else:
                sum += value
                count += 1
        if count != 0:
            print(" " + str(count) + " completed courses:")
            for key, value in database[name].items():
                if value == 0:
                    continue
                else:
                    print("  " + key + " " + str(value))
            print(" average grade " + str(sum/count))
        elif count == 0:
            print(" no completed courses")
    
def add_course(database: dict, name: str, course: tuple):
    if course[0] not in database[name]:
        database[name][course[0]] = course[1]
    else:
        if database[name][course[0]] < course[1]:
            database[name][course[0]] = course[1]
        
def summary(database: list):
    print("students " + str(len(database.items())))
    most_courses = 0
    most_courses_student = ""
    best_average = 0
    best_average_student = ""
    
    # Determine who complete the most courses
    for student, courses in database.items():
        if len(courses.items()) > 0:
            total = 0
            for key, value in courses.items():
                if value == 0:
                    continue
                else:
                    total += 1
            if total > most_courses:
                most_courses = total
                most_courses_student = student
        # Determine who has the best GPA
        sum = 0
        count = 0
        # print(f"{name}:")
        for course, grade in courses.items():
            if grade == 0:
                continue
            else:
                sum += grade
                count += 1
        average = sum / count
        if average > best_average:
            best_average = average
            best_average_student = student
    print("most courses completed", str(most_courses), most_courses_student)
    print("best average grade", str(best_average), best_average_student)


if __name__ == "__main__":
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)