# Write your solution here
def gather_data(grades: list):
    exam_points = []
    exercises_completed = []
    response = input("Exam points and exercises completed: ")
    if response == "":
        break
    else:
        response_list = response.split(" ")
        exam_points.append(int(response_list[0]))
        exercises_completed.append(int(response_list[1]))
    all_grades = [exam_points, exercises_completed]
    return all_grades

def exercise_points(exercises: list):
    points = []
    for x in exercises:
        point = x/100
        points.append(point)

def main():


