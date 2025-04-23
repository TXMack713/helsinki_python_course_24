# write your solution here
def get_student_exercises():
    student_file = input("Student information: ")
    exercise_file = input("Exercises completed: ")
    exam_file = input("Exam points: ")
    students = {}
    exercises_completed = {}
    exam_points = {}
    total_points = {}

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
    
    if exam_file == "":
        with open("exam_points1.csv") as file3:
            for line in file3:
                if line.startswith("id"):
                    continue
                else:
                    exam_info = []
                    info = line.split(";")
                    count = 0
                    while count < len(info):
                        if count == 0:
                            count += 1
                        else:
                            exam_info.append(int(info[count]))
                            count += 1
                    exam_points[int(info[0])] = exam_info
                    total_points[int(info[0])] = 0

    else:
        with open(exam_file) as file3:
            for line in file3:
                if line.startswith("id"):
                    continue
                else:
                    exam_info = []
                    info = line.split(";")
                    count = 0
                    while count < len(info):
                        if count == 0:
                            count += 1
                        else:
                            exam_info.append(int(info[count]))
                            count += 1
                    exam_points[int(info[0])] = exam_info
                    total_points[int(info[0])] = 0

    # Update to calculate total points    
    for id in students:
        if id in exam_points:
            exam_sum = 0
            for item in exam_points[id]:
                exam_sum += item        
            total_points[id] += exam_sum
    
    for id in students:
        if id in exercises_completed:
            sum = 0
            for item in exercises_completed[id]:
                sum += item
            # print(students[id] + " " + str(sum))
            exercises_grade = int(sum / 4)
            total_points[id] += exercises_grade
            # total_points[id] += exercises_grade
            if total_points[id] < 15:
                print(students[id], str(0))
            elif total_points[id] >= 15 and total_points[id] < 18:
                print(students[id], str(1))
            elif total_points[id] >= 18 and total_points[id] < 21:
                print(students[id], str(2))
            elif total_points[id] >= 21 and total_points[id] < 24:
                print(students[id], str(3))
            elif total_points[id] >= 24 and total_points[id] < 28:
                print(students[id], str(4))
            elif total_points[id] >= 28:
                print(students[id], str(5))
    
get_student_exercises()

# if __name__ == "__main__":
#     get_student_exercises()