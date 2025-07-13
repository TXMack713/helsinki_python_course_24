# Write your solution here
def new_person(name: str, age: int):
    if name == "":
        raise ValueError("Name is an empty string.")
    elif len(name) > 40:
        raise ValueError("Name cannot be more than 40 characters long.")
    names = name.split(" ")
    if len(names) < 2:
        raise ValueError("Name should be at least two words long.")
    
    if age < 0:
        raise ValueError("Age cannot be less than 0: " + str(age))
    elif age > 150:
        raise ValueError("Age is greater than 150: " + str(age))
    
    return (name, age)

if __name__ == "__main__":
    new_person()
