#!/usr/bin/env python 3

class Present:
    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f"{self.name} ({self.weight} kg)"

class Box:
    def __init__(self):
        self.presents = []
        self.weight = 0
    
    def add_present(self, present: Present):
        self.presents.append(present)

    def total_weight(self):
        self.weight = 0
        for item in self.presents:
            # print(f"{item.name}: {item.weight}")
            self.weight += item.weight

        return self.weight

if __name__ == "__main__":
    book = Present("ABC Book", 2)

    print("The name of the present:", book.name)
    print("The weight of the present:", book.weight)
    print("Present", book)

    box = Box()
    box.add_present(book)
    print(box.total_weight())

    cd = Present("Pink Floy: Dark Side of the Moon", 1)
    box.add_present(cd)
    print(box.total_weight())
    
