#!/usr/bin/env python 3

class ListHelper:
    def __init__(self, my_list: list):
        self.__list = my_list
    

    @classmethod
    def greatest_frequency(cls, my_list: list):
        most_frequent = ""
        count = 0
        item_list = []
        for item in my_list:
            if item not in item_list:
                item_list.append(item)
        
        for item in item_list:
            list_counter = 0
            for entry in my_list:
                if entry == item:
                    list_counter += 1
            if list_counter > count:
                count = list_counter
                most_frequent = item
        
        return most_frequent
    
    @classmethod
    def doubles(cls, my_list: list):
        doubles_list = []
        counter = 0
        for item in my_list:
            if item not in doubles_list:
                doubles_list.append(item)
            
        for item in doubles_list:
            count = 0
            for entry in my_list:
                if entry == item:
                    count += 1
            if count >= 2:
                counter += 1
        return counter
    
if __name__ == "__main__":
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))
