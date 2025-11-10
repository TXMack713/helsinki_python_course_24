#!/usr/bin/env python 3

class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name
    
class Room:
    def __init__(self):
        self.people = []
        self.height = 0

    def is_empty(self):
        if len(self.people) == 0:
            return True
        else:
            return False
        
    def add(self, person: Person):
        self.people.append(person)
    
    def print_contents(self):
        if len(self.people) == 0:
            pass
            # print("The room is empty")
        else:
            self.height = 0
            for person in self.people:
                self.height += person.height
            print(f"There are {len(self.people)} in the room, and their combined height is {self.height} cm")
            for person in self.people:
                print(f"{person.name} ({person.height} cm)")

    def shortest(self):
        if len(self.people) == 0:
            return None
        else:
            self.height = 0
            self.name = ""
            self.person = ""
            for person in self.people:
                if self.height == 0:
                    self.height = person.height
                    self.name = person.name
                    self.person = person
                else:
                    if person.height < self.height:
                        self.height = person.height
                        self.name = person.name
                        self.person = person
            return self.person
        
    def remove_shortest(self):
        if len(self.people) == 0:
            return None
        else:
            shortest_person = self.shortest()
            self.people.remove(shortest_person)
            return shortest_person

if __name__ == "__main__":
    room = Room()
    print("Is the room empty?", room.is_empty())
    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Ally", 166))
    room.add(Person("Nina", 162))
    room.add(Person("Dorothy", 155))
    print("Is the room empty?", room.is_empty())
    room.print_contents()

    print()

    print("Shortest:", room.shortest())

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()

    while room.is_empty() == False:
        print("Shortest:", room.shortest())
        room.remove_shortest()
        room.print_contents()

