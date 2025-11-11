#!/usr/bin/env python 3

class Car:
    def __init__(self):
        self.__fuel = 0
        self.__odometer = 0

    def __str__(self):
        return f"Car: odometer reading {self.__odometer} km, petrol remaining {self.__fuel} litres"
    
    def fill_up(self):
        self.__fuel = 60
    
    def drive(self, km: int):
        if self.__fuel >= km:
            self.__fuel -= km
            self.__odometer += km
        else:
            self.__odometer += self.__fuel
            self.__fuel = 0
        
if __name__ == "__main__":
    car = Car()
    print(car)
    car.fill_up()
    print(car)
    car.drive(20)
    print(car)
    car.drive(50)
    print(car)
    car.drive(10)
    print(car)
    car.fill_up()
    car.fill_up()
    print(car)
        
