# Write your solution here
#!/usr/bin/env python3
import json

def print_persons(filename: str):
    # info = ""
    with open(filename) as file:
        data = file.read()
    info = json.loads(data)
    for entry in info:
        person = ""
        for key, values in entry.items():
            if str(values).isdigit():
                person = person + str(values) + " years "
            else:
                if isinstance(values, list) == False:
                    person = person + values + " "
                else:
                    output = ""
                    if len(values) == 0:
                        person = person + "()"
                    else:
                        counter = 0
                        while counter < len(values):
                        # for value in values:
                            output = output + values[counter] + "," + " "
                            counter += 1
                        output = output.rstrip(" ")
                        output = output.rstrip(",")
                        person = person + "(" + output + ")"
        print(person.strip())


if __name__ == "__main__":
    print_persons("file1.json")
    print_persons("file2.json")
    print_persons("file3.json")
    print_persons("file4.json")

