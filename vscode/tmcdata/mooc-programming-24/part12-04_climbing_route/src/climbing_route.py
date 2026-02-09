#!/usr/bin/env python 3

class ClimbingRoute:
    def __init__(self, name: str, length: int, grade: str):
        self.name = name
        self.length = length
        self.grade = grade

    def __str__(self):
        return f"{self.name}, length {self.length} metres, grade {self.grade}"

def sort_by_length(items: list):
    def check_length(items: list):
        return items.length
    return sorted(items, key=check_length, reverse=True)

def sort_by_difficulty(items:list):
    products = {}
    
    def check_difficulty(items:list):
        return items.grade
    
    temp_list = sorted(items, key=check_difficulty, reverse=True)
    
    for item in temp_list:
        # print(f"For item in temp list: {item}")
        if item.grade not in products:
            products[item.grade] = []
            products[item.grade].append(item)
        else:
            products[item.grade].append(item)
        
    new_list = []
    
    for key,values in products.items():
        for item in sort_by_length(values):
            new_list.append(item)
    
    return new_list

if __name__ == "__main__":
    r1 = ClimbingRoute("Edge", 38, "6A+")
    r2 = ClimbingRoute("Smooth operator", 11, "7A")
    r3 = ClimbingRoute("Synchro", 14, "8C+")
    r4 = ClimbingRoute("Small steps", 12, "6A+")

    routes = [r1, r2, r3, r4]

    for route in sort_by_length(routes):
        print(route)

    print("")

    for route in sort_by_difficulty(routes):
        print(route)
