#!/usr/bin/env python 3

class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        self._day = day
        self._month = month
        self.year = year
    
    def __str__(self):
        return f"{self._day}.{self._month}.{self.year}"
    
    def __lt__(self, another):
        if (self.year < another.year):
            return True
        elif (self.year > another.year):
            return False
        elif (self.year == another.year):
            if (self._month < another._month):
                return True
            elif (self._month > another._month):
                return False
            elif (self._month == another._month):
                if (self._day < another._day):
                    return True
                elif (self._day > another._day):
                    return False
                elif (self._day == another._day):
                    return False
                
    def __gt__(self, another):
        if (self.year > another.year):
            return True
        elif (self.year < another.year):
            return False
        elif (self.year == another.year):
            if (self._month > another._month):
                return True
            elif (self._month < another._month):
                return False
            elif (self._month == another._month):
                if (self._day > another._day):
                    return True
                elif (self._day < another._day):
                    return False
                elif (self._day == another._day):
                    return False
    
    def __eq__(self, another):
        if (self.year == another.year) and (self._month == another._month) and (self._day == another._day):
            return True
        else:
            return False
        
    def __ne__(self, another):
        if (self.year != another.year) or (self._month != another._month) or (self._day != another._day):
            return True
        else:
            return False
        
    def __add__(self, another):
        current_day = self._day + another
        current_month = self._month
        current_year = self.year
        if (current_day > 30):
            while (current_day > 30):
                current_month += 1
                if (current_month > 12):
                    current_year += 1
                    current_month = 1
                current_day -= 30
        return SimpleDate(current_day, current_month, current_year)

    def __sub__(self, another):
        days = 0
        if (self.year != another.year):
            if (self.year > another.year):
                days += 360 * (self.year - another.year)
                if (self._month != another._month):
                    if (self._month > another._month):
                        days += 30 * (self._month - another._month)
                    elif (self._month < another._month):
                        days -= 30 * (another._month - self._month)
                if (self._day != another._day):
                    if (self._day > another._day):
                        days += self._day - another._day
                    elif (self._day < another._day):
                        days += another._day - self._day
            else:
                days += 360 * (another.year - self.year)
                if (self._month != another._month):
                    if (self._month > another._month):
                        days -= 30 * (self._month - another._month)
                    elif (self._month < another._month):
                        days += 30 * (another._month - self._month)
                if (self._day != another._day):
                    if (self._day > another._day):
                        days += self._day - another._day
                    elif (self._day < another._day):
                        days += another._day - self._day

        elif (self._month != another._month) and (self.year == another.year):
            if (self._month > another._month):
                days += 30 * (self._month - another._month)
                if (self._day != another._day):
                    if (self._day > another._day):
                        days += self._day - another._day
                    elif (self._day < another._day):
                        days += another._day - self._day
            elif (self._month < another._month):
                days += 30 * (another._month - self._month)
                if (self._day != another._day):
                    if (self._day > another._day):
                        days -= self._day - another._day
                    elif (self._day < another._day):
                        days -= another._day - self._day
        
        if (self._month == another._month) and (self.year == another.year):
            if (self._day > another._day):
                days += self._day - another._day
            elif (self._day < another._day):
                days += another._day - self._day

        return days

if __name__ == "__main__":
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(28, 12, 1985)
    d3 = SimpleDate(28, 12, 1985)

    print(d1)
    print(d2)
    print(d1 == d2)
    print(d1 != d2)
    print(d1 == d3)
    print(d1 < d2)
    print(d1 > d2)

    d4 = SimpleDate(4, 10, 2020)
    d5 = SimpleDate(28, 12, 1985)

    d6 = d4 + 3
    d7 = d5 + 400

    print(d4)
    print(d5)
    print(d6)
    print(d7)

    d8 = SimpleDate(2, 11, 2020)

    print(d8 - d1)
    print(d1 - d8)
    print(d1 - d3)
