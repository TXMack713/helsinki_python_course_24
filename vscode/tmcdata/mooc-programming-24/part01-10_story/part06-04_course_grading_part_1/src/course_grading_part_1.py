# write your solution here
def get_student_exercises():
    student_file = input("Student information: ")
    exercise_file = input("Exercises completed: ")
    students = {}
    exercises_completed = {}

    if student_file == "":
        with open("students1.csv") as file1:
            for line in file1:
                if line.startswith("id"):
                    continue
                else:
                    info = line.split(";")
                    students[int(info[0])] = info[1].strip() + " " + info[2].strip()
    else:
        with open(student_file) as file1:
            for line in file1:
                if line.startswith("id"):
                    continue
                else:
                    info = line.split(";")
                    students[int(info[0])] = info[1].strip() + " " + info[2].strip()

    if exercise_file == "":
        with open("exercises1.csv") as file2:
            for line in file2:
                if line.startswith("id"):
                    continue
                else:
                    exercise_info = []
                    info = line.split(";")
                    count = 0
                    while count < len(info):
                        if count == 0:
                            count += 1
                        else:
                            exercise_info.append(int(info[count]))
                            count += 1
                    exercises_completed[int(info[0])] = exercise_info

    else:
        with open(exercise_file) as file2:
            for line in file2:
                if line.startswith("id"):
                    continue
                else:
                    exercise_info = []
                    info = line.split(";")
                    count = 0
                    while count < len(info):
                        if count == 0:
                            count += 1
                        else:
                            exercise_info.append(int(info[count]))
                            count += 1
                    exercises_completed[int(info[0])] = exercise_info
    for id in students:
        if id in exercises_completed:
            sum = 0
            for item in exercises_completed[id]:
                sum += item
            print(students[id] + " " + str(sum))
    
get_student_exercises()

# if __name__ == "__main__":
#     get_student_exercises()