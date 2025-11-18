#!/usr/bin/env python 3

class Item:
    def __init__(self, name: str, weight: int):
        if name != "":
            self.__name = name
        else:
            raise ValueError("Name field cannot be empty")
        if weight >= 0:
            self.__weight = weight
        else:
            raise ValueError("Weight cannot be negative value")

    def name(self):
        return self.__name
    
    def weight(self):
        return self.__weight
         
    def __str__(self):
        return f"{self.name()} ({self.weight()} kg)"
    
class Suitcase:
    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__items = []
        
    def add_item(self, item: Item):
        current_weight = self.weight()
        if (current_weight + item.weight()) <= self.__max_weight:
            self.__items.append(item)
            current_weight = self.weight()

    def weight(self):
        total_weight = 0
        if len(self.__items) == 0:
            return total_weight
        else:
            for item in self.__items:
                total_weight += item.weight()
            return total_weight
    
    def print_items(self):
        for item in self.__items:
            print(item)

    def heaviest_item(self):
        self.__heaviest = ""
        max = 0
        if len(self.__items) == 0:
            return None
        else:
            for item in self.__items:
                if item.weight() > max:
                    max = item.weight()
                    self.__heaviest = item
            return self.__heaviest
    
    def __str__(self):
        if len(self.__items) == 1:
            return f"{len(self.__items)} item ({self.weight()} kg)"
        else:
            return f"{len(self.__items)} items ({self.weight()} kg)"
        
class CargoHold:
    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__cargo = []
        self.__space = self.remaining_capacity()

    def remaining_capacity(self):
        self.__space = self.__max_weight - self.total_weight()
        return self.__space
    
    def add_suitcase(self, suitcase: Suitcase):
        capacity = self.remaining_capacity()
        if capacity >= suitcase.weight():
            self.__cargo.append(suitcase)
            capacity = self.remaining_capacity()
    
    def total_weight(self):
        self.__total_weight = 0
        if len(self.__cargo) == 0:
            return self.__total_weight
        else:
            for suitcase in self.__cargo:
                self.__total_weight += suitcase.weight()
            return self.__total_weight
        
    def print_items(self):
        # print("The suitcases in the cargo hold contain the following items:")
        for item in self.__cargo:
            item.print_items()
        
    def __str__(self):
        if len(self.__cargo) == 1:
            return f"{len(self.__cargo)} suitcase, space for {self.__space} kg"
        else:
            return f"{len(self.__cargo)} suitcases, space for {self.__space} kg"

if __name__ == "__main__":
    # book = Item("ABC Book", 2)
    # phone = Item("Nokia 3210", 1)
    # brick = Item("Brick", 4)

    hold = CargoHold(50)
    suitcase = Suitcase(25)
    item = Item("ABC Book", 2)
    suitcase.add_item(item)
    hold.add_suitcase(suitcase)
    suitcase2 = Suitcase(10)
    suitcase2.add_item(Item("Rock", 1))
    suitcase2.add_item(Item("Mouse", 2))
    hold.add_suitcase(suitcase2)
    hold.print_items()
    
    '''
    print("Name of the book:", book.name())
    print("Weight of the book:", book.weight())

    print("Book:", book)
    print("Phone:", phone)

    cargo_hold = CargoHold(1000)
    print(cargo_hold)

    

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold.add_suitcase(adas_suitcase)
    print(cargo_hold)

    cargo_hold.add_suitcase(peters_suitcase)
    print(cargo_hold)
    '''

    '''
    heaviest = suitcase.heaviest_item()
    print(f"The heaviest item: {heaviest}")
    
    print("The suitcase contains the following items:")
    suitcase.print_items()
    combined_weight = suitcase.weight()
    print(f"Combined weight: {combined_weight} kg")
    '''
    
    # book.weight = 10
    # print("Book:", book)
    
