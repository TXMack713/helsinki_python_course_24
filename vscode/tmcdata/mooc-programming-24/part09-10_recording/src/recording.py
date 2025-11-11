#!/usr/bin/env python 3

class Recording:
    def __init__(self, length: int):
        if length >= 0:
            self.__length = length
        else:
            raise ValueError("The length of the recording cannnot be less than 0")

    # getter method
    @property
    def length(self):
        return self.__length
    
    # setter method
    @length.setter
    def length(self, length):
        if length >= 0:
            self.__length = length
        else:
            raise ValueError("The length of the recording cannnot be less than 0")
        

if __name__ == "__main__":
    the_wall = Recording(43)
    print(the_wall.length)
    the_wall.length = 44
    print(the_wall.length)
