# write your solution here
def get_student_exercises():
    student_file = input("Student information: ")
    exercise_file = input("Exercises completed: ")
    if student_file == "":
        with open("students1.csv") as file1:
    else:
        with open(student_file) as file1:

    if exercise_file == "":
        with open("exercises1.csv") as file2:
    else:
        with open(exercise_file) as file2: