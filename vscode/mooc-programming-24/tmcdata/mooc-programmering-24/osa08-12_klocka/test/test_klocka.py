import unittest
from unittest.mock import patch

from tmc import points, reflect
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint
from datetime import date, datetime, timedelta

exercise = 'src.klocka'
classname = "Klocka"

def f(attr: list):
    return ",".join(attr)

@points('8.klocka')
class KelloTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Förväntade inte att värden frågas av användaren")]):
           cls.module = load_module(exercise, 'fi')

    def test_0a_paaohjelma_kunnossa(self):
        ok, line = check_source(self.module)
        message = """Koden som testar funktionerna ska placeras i blocket
if __name__ == "__main__":
Följande rad måste flyttas:
"""
        self.assertTrue(ok, message+line)

    
    def test1_luokka_olemassa(self):
        try:
            from src.klocka import Klocka
        except:
            self.assertTrue(False, "Ditt program bör ha en klass med namnet Klocka")

    def test2_konstruktori(self):
        try:
            from src.klocka import Klocka
            kello = Klocka(12,0,0)
            self.assertTrue(True, "")
        except Exception as e:
            self.assertTrue(False, 'Anropning av klassen Klockas konstruktor med värdet Klocka(12,0,0)' +
                f' returnerade ett fel: {e}')

    def test3_testaa_str(self):
        test_cases = ((23,30,0), (10,10,10), (15,10,5), (23,5,15), (4,24,28), (3,4,5))
        for test_case in test_cases:
            try:
                from src.klocka import Klocka
                h,m,s = test_case
                kello = Klocka(h,m,s)

                corr = (datetime(2000,1,1,h,m,s)).strftime("%H:%M:%S")
                val = str(kello)

                self.assertEqual(corr, val, f"Metoden __str__ borde returnera strängen {corr}\ndå objektet skapades med anropet\n" + 
                    f"Klocka({h}:{m}:{s}).\nNu returnerar metoden strängen{val}.")

            except Exception as e:
                self.assertTrue(False, 'Metodin __str__ kutsuminen' +
                    f' returnerade ett fel: {e}\ndå klockan initialiserades med anroptet Klocka({h},{m},{s})')

    def test4_testaa_tikitys(self):
        test_cases = ((10,10,58,3),(23,59,55,6),(0,0,0,30),(23,58,30,31))
        for test_case in test_cases:
            try:
                from src.klocka import Klocka
                h,m,s,t = test_case
                kello = Klocka(h,m,s)
                for i in range(t):
                    kello.tick()

                corr = (datetime(2000,1,1,h,m,s) + timedelta(seconds=t)).strftime("%H:%M:%S")
                val = str(kello)

                self.assertEqual(corr, val, f"Metoden __str__ borde returnera strängen {corr}\ndå objektet skapades med anropet\n" + 
                    f"Klocka({h}:{m}:{s}) och metoden tick() anropades {t} gånger.\nNu returnerar metoden strängen{val}.")

            except Exception as e:
                self.assertTrue(False, 'Anropning av metoden tick()' +
                    f' returnerade ett fel: {e}\ndå klockan initialiserades med anroptet Klocka({h},{m},{s})')

    def test5_testaa_ajan_asetus(self):
        test_cases = ((10,10,58,15,15),(23,59,55,11,0),(0,0,0,12,0),(23,58,10,11,34))
        for test_case in test_cases:
            try:
                from src.klocka import Klocka
                h,m,s,h2,m2 = test_case
                kello = Klocka(h,m,s)
                kello.installning(h2,m2)

                corr = (datetime(2000,1,1,h2,m2,0)).strftime("%H:%M:00")
                val = str(kello)

                self.assertEqual(corr, val, f"Metoden __str__ borde returnera strängen {corr}\ndå objektet skapades med anropet\n" + 
                    f"Klocka({h}:{m}:{s}) och därefter anropades installning({h2}:{m2}).\nNu returnerar metoden __str__ strängen {val}.")

            except Exception as e:
                self.assertTrue(False, f'Anropning av metoden installning({h2},{m2})' +
                    f' returnerade ett fel: {e}\ndå klockan initialiserades med anroptet Klocka({h},{m},{s})')

if __name__ == '__main__':
    unittest.main()
