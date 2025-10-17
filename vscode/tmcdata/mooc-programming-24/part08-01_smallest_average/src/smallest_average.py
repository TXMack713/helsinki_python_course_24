#!/usr/bin/env python3

def smallest_average(person1: dict, person2: dict, person3: dict):
    person1_avg = (person1["result1"] + person1["result2"] + person1["result3"]) / 3
    person2_avg = (person2["result1"] + person2["result2"] + person2["result3"]) / 3
    person3_avg = (person3["result1"] + person3["result2"] + person3["result3"]) / 3

    if person1_avg < person2_avg and person1_avg < person3_avg:
        return person1
    elif person2_avg < person1_avg and person2_avg < person3_avg:
        return person2
    if person3_avg < person2_avg and person3_avg < person1_avg:
        return person3
    
if __name__ == "__main__":
    smallest_average()
