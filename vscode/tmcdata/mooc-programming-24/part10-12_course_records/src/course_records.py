#!/usr/bin/env python 3

class Course:
    def __init__(self):
        self.__courses = {}

    def add_course(self, name: str, grade: int, credits: int):
        if not name in self.__courses:
            self.__courses[name] = {}
            self.__courses[name]["grade"] = grade
            self.__courses[name]["credits"] = credits
        
        if grade >= self.__courses[name]["grade"]:
            self.__courses[name]["grade"] = grade
        self.__courses[name]["credits"] = credits

    def get_course_data(self, name: str):
        if not name in self.__courses:
            print("no entry for this course")
            return
        print(f"{name} ({self.__courses[name]["credits"]} cr) grade {self.__courses[name]["grade"]}")

    def statistics(self):
        total_credits = 0
        count = 0
        grade_total = 0
        mean = 0
        ones = ""
        twos = ""
        threes = ""
        fours = ""
        fives = ""
        for course, info in self.__courses.items():
            total_credits += self.__courses[course]["credits"]
            grade_total += self.__courses[course]["grade"]
            count += 1
            if self.__courses[course]["grade"] == 1:
                ones += "x"
            elif self.__courses[course]["grade"] == 2:
                twos += "x"
            elif self.__courses[course]["grade"] == 3:
                threes += "x"
            elif self.__courses[course]["grade"] == 4:
                fours += "x"
            elif self.__courses[course]["grade"] == 5:
                fives += "x"
        
        mean = grade_total / count
        print(f"{len(self.__courses.keys())} completed courses, a total of {total_credits} credits")
        print(f"mean {mean:.1f}")
        print("grade distribution")
        print(f"5: {fives}")
        print(f"4: {fours}")
        print(f"3: {threes}")
        print(f"2: {twos}")
        print(f"1: {ones}")

    def all_entries(self):
        return self.__persons

class CourseApplication:
    def __init__(self):
        self.__courses = Course()

    def add_course(self):
        course = input("course: ")
        grade = int(input("grade: "))
        credits = int(input("credits: "))
        self.__courses.add_course(course, grade, credits)

    def get_course_data(self):
        course = input("course: ")
        self.__courses.get_course_data(course)
    
    def statistics(self):
        self.__courses.statistics()
    
    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add course")
        print("2 get course data")
        print("3 statistics")

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_course()
            elif command == "2":
                self.get_course_data()
            elif command == "3":
                self.statistics()
            else:
                self.help()

application = CourseApplication()
application.execute()
