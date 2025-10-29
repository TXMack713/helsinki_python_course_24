#!/usr/bin/env python 3

import time

class Clock:
    def __init__(self, hours: int, minutes: int, seconds: int):
        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours

    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"
    
    def tick(self):
        # time.sleep(1)
        if self.seconds == 59:
            self.seconds = 0
            if self.minutes == 59:
                self.minutes = 0
                if self.hours == 23:
                    self.hours = 0
                else:
                    self.hours += 1
            else:
                self.minutes += 1
        else:
            self.seconds += 1

    def set(self, hour: int, minute: int):
        self.seconds = 0
        self.minutes = minute
        self.hours = hour
        
if __name__ == "__main__":
    clock = Clock(23, 59, 55)
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)
    clock.tick()
    print(clock)

    clock.set(12, 5)
    print(clock)
