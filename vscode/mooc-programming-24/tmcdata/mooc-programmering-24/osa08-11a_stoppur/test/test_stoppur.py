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

exercise = 'src.stoppur'
classname = "Stoppur"

def f(attr: list):
    return ",".join(attr)

@points('8.stoppur')
class SekuntielloTest(unittest.TestCase):
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
            from src.stoppur import Stoppur
        except:
            self.assertTrue(False, "Ditt program bör ha en klass med namnet Stoppur")

        def test2_konstruktori(self):
            try:
                from src.stoppur import Stoppur
                kello = Stoppur()
            except Exception as e:
                self.assertTrue(False, 'Anropning av klassen Stoppurs konstruktor()' +
                    f' åstadkom ett fel: {e}')

    def test3_testaa_str(self):
        try:
            from src.stoppur import Stoppur
            kello = Stoppur()

            corr = "00:00"
            val = str(kello)

            self.assertEqual(corr, val, f"Metoden __str__ borde returnera strängen {corr}\ndå objektet skapades med anropet\n" + 
                f"Stoppur().\nNu returnerar metoden strängen {val}.")

        except Exception as e:
            self.assertTrue(False, 'Metodin __str__ kutsuminen' +
                f' returnerade ett fel: {e}\ndå klockan initialiserades med anropet Stoppur()')

    def test5_tick_olemassa(self):

        try:
            from src.stoppur import Stoppur
            koodi = """
kello = Stoppur()                
kello.tick()
"""

            kello = Stoppur()
            kello.tick()  

        except Exception as e:
            self.assertTrue(False, f'Exekvering av koden\n{koodi}\n åstadkom ett fel\n{e}\nNog är väl metoden tick(self) definierad?')

    def test6_testaa_tikitys(self):
            try:
                from src.stoppur import Stoppur
                kello = Stoppur()
                kello.tick()

                koodi = """
kello = Stoppur()                
kello.tick()                
""" 
                corr = "00:01"
                val = str(kello)

                self.assertEqual(corr, val, f"Metoden __str__ borde returnera strängen\n{corr}\nvid exekvering av koden\n{koodi}\nNu returnerar metoden strängen\n{val}")

                kello.tick()
                kello.tick()

                koodi += "kello.tick()\nkello.tick()\n"   

                corr = "00:03"
                val = str(kello)

                self.assertEqual(corr, val, f"Metoden __str__ borde returnera strängen\n{corr}\nvid exekvering av koden\n{koodi}\nNu returnerar metoden strängen\n{val}")

                kello = Stoppur()
                for i in range(60):
                    kello.tick()
                
                koodi = """
kello = Stoppur()
for i in range(60):
    kello.tick()         
""" 

                corr = "01:00"
                val = str(kello)

                self.assertEqual(corr, val, f"Metoden __str__ borde returnera strängen\n{corr}\nvid exekvering av koden\n{koodi}\nNu returnerar metoden strängen\n{val}")

                kello.tick()

                koodi += "kello.tick()\nkello.tick()\n"   

                corr = "01:01"
                val = str(kello)

                self.assertEqual(corr, val, f"Metoden __str__ borde returnera strängen\n{corr}\nvid exekvering av koden\n{koodi}\nNu returnerar metoden strängen\n{val}")

                kello = Stoppur()
                for i in range(60*59+59):
                    kello.tick()
                
                koodi = """
kello = Stoppur()
# åker framåt tills en sekund innan en timme
for i in range(60*59+59):
    kello.tick()         
""" 

                corr = "59:59"
                val = str(kello)

                self.assertEqual(corr, val, f"Metoden __str__ borde returnera strängen\n{corr}\nvid exekvering av koden\n{koodi}\nNu returnerar metoden strängen\n{val}")

                koodi += "kello.tick()\n"   

                kello.tick()
                corr = "00:00"
                val = str(kello)

                self.assertEqual(corr, val, f"Metoden __str__ borde returnera strängen\n{corr}\nvid exekvering av koden\n{koodi}\nNu returnerar metoden strängen\n{val}")


            except Exception as e:
                self.assertTrue(False, 'Anropning av metoden tick()' +
                f' returnerade ett fel: {e}\nvid exekvering av koden\n{koodi}')

if __name__ == '__main__':
    unittest.main()
