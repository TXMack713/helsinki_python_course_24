#!/usr/bin/env python 3

class Money:
    def __init__(self, euros: int, cents: int):
        self._euros = euros
        self._cents = cents

    # @property
    # def euros(self):
    #     return self._euros
    
    # @euros.setter
    # def euros(self, euros: int):
    #     self._euros = euros

    # @property
    # def cents(self):
    #     return self._cents
    
    # @cents.setter
    # def cents(self, cents: int):
    #     self._cents = cents

    def __str__(self):
        return f"{self._euros}.{self._cents:02} eur"
    
    def __eq__(self, another):
        return ({self._euros} == {another._euros}) and ({self._cents} == {another._cents})
    
    def __lt__(self, another):
        if self._euros != another._euros:
            return self._euros < another._euros
        else:
            return self._cents < another._cents
            
    def __gt__(self, another):
        if self._euros != another._euros:
            return self._euros > another._euros
        else:
            return self._cents > another._cents

    def __ne__(self, another):
        if ({self._euros} != {another._euros}):
            return True
        elif ({self._euros} == {another._euros}):
            return ({self._cents} != {another._cents})
        
    def __add__(self, another):
        self._euros += another._euros
        self._cents += another._cents
        if self._cents >= 100:
            self._euros += 1
            self._cents -= 100
        return Money(self._euros, self._cents)
    
    def __sub__(self, another):
        if (self._euros - another._euros) < 0:
            raise ValueError("a negative result is not allowed")
        elif (self._euros - another._euros) == 0:
            if (self._cents - another._cents) < 0:
                raise ValueError("a negative result is not allowed")
            else:
                return Money((self._euros - another._euros), (self._cents - another._cents))
        else:
            if (self._cents < another._cents):
                self._euros -= 1
                self._cents += 100
                return Money((self._euros - another._euros), (self._cents - another._cents))
            else:
                return Money((self._euros - another._euros), (self._cents - another._cents))

if __name__ == "__main__":
    e1 = Money(4, 10)
    e2 = Money(2, 5)
    e3 = Money(4, 10)
    e4 = Money(4, 5)
    e5 = Money(2, 95)

    print(e1)
    print(e2)
    print(e3)
    
    print(e1 == e2)
    print(e1 == e3)
    print(e1 != e2)
    print(e1 < e2)
    print(e1 > e2)

    e6 = e4 + e5
    e7 = e4 - e5

    print(e6)
    print(e7)

    # e7.euros = 1000
    print(f"E7: {e7}")
