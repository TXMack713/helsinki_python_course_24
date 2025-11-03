#!/usr/bin/env python 3

import time

class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0

    def __str__(self):
        return f"{self.minutes:02}:{self.seconds:02}"
    
    def tick(self):
        # time.sleep(1)
        if self.seconds == 59:
            self.seconds = 0
            if self.minutes == 59:
                self.minutes = 0
            else:
                self.minutes += 1
        else:
            self.seconds += 1
        
if __name__ == "__main__":
    watch = Stopwatch()
    for i in range(12):
        print(watch)
        watch.tick()
