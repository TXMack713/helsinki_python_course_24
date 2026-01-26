#!/usr/bin/env python 3

class PhoneBook:
    def __init__(self):
        self.__persons = {}

    def add_number(self, name: str, number: str):
        if not name in self.__persons:
            self.__persons[name] = Person(name)
            # self.__persons[name].add_number(number)
        self.__persons[name].add_number(number)

    def add_address(self, name: str, address: str):
        if not name in self.__persons:
            self.__persons[name] = Person(name)
            # self.__persons[name].add_number(number)
        self.__persons[name].add_address(address)

    def get_entry(self, name: str):
        if not name in self.__persons:
            return None
        return self.__persons[name]

    def all_entries(self):
        return self.__persons

class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add number")
        print("2 search")
        print("3 add address")

    def add_number(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)

    def add_address(self):
        name = input("name :")
        address = input("address: ")
        self.__phonebook.add_address(name, address)

    def search(self):
        name = input("name: ")
        person = self.__phonebook.get_entry(name)
        if person == None:
            print("number unknown")
            print("address unknown")
            return
        else:
            numbers = person.numbers()
            address = person.address()
            
        if (numbers == None or len(numbers) == 0) and address == None:
            print("number unknown") 
            print("address unknown")
            return 
        elif len(numbers) != 0 and address == None:
            for number in numbers:
                print(number)     
            print("address unknown")
            return
        elif len(numbers) != 0 and address != None:
            for number in numbers:
                print(number)
        if address == None and len(numbers) != 0:
            print("address unknown")
            return
        elif address != None and (numbers == None or len(numbers) == 0):
            print("number unknown")
            print(address)  
            return
        else:
            print(address)
            return

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_number()
            elif command == "2":
                self.search()
            elif command == "3":
                self.add_address()
            else:
                self.help()

class Person:
    def __init__(self, name: str):
        self._person = {}
        self._name = name
        self._numbers = []
        self._address = ""
        self._person["name"] = self._name
        self._person["numbers"] = self._numbers
        self._person["address"] = self._address

    def name(self):
        return self._person["name"]
    
    def numbers(self):
        return self._person["numbers"]
    
    def address(self):
        if self._person["address"] == "":
            return None
        else:
            return self._person["address"]
    
    def add_number(self, number: str):
        self._person["numbers"].append(number)

    def add_address(self, address: str):
        self._person["address"] = address


# when testing, no code should be outside application except the following:
application = PhoneBookApplication()
application.execute()

if __name__ == "__main__":
    person = Person("Eric")
    print(person.name())
    print(person.numbers())
    print(person.address())
    person.add_number("040-123456")
    person.add_address("Mannerheimintie 10 Helsinki")
    print(person.numbers())
    print(person.address())
