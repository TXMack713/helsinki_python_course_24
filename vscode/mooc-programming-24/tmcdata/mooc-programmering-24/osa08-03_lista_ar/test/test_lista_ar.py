import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint
from datetime import date

exercise = 'src.lista_ar'
function = "lista_ar"

def get_corr(m):
    return sorted([x.year for x in m])
        

@points('8.lista_ar')
class VuodetListaanTest(unittest.TestCase):
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

    def test1_funktio_olemassa(self):
        try:
            from src.lista_ar import lista_ar
        except:
            self.assertTrue(False, "Ditt program bör ha en funktion med namnet lista_ar(vuodet: list)")

    def test2_palautusarvon_tyyppi(self):
        try:
            from src.lista_ar import lista_ar
            val = lista_ar([date(1900,1,1)])
            taip = str(type(val)).replace("<class '","").replace("'>","")
            self.assertTrue(type(val) == list, f"Funktionen lista_ar borde returnera ett värde av typen list," +  
                f" nu returnerar den ett värde {val} som är av typen {taip}\n när den anropas med argumentet \n[date(1900,1,1)]")
        except Exception as e:
            self.assertTrue(False, f"Funktionen gav ett fel när den anropades med argumentvärdet [date(1900,1,1)]")


    def test3_testaa_arvot(self):
        d = date
        test_cases = ([d(1900,1,1), d(1950,2,3), d(1979,6,6)], [d(2010,5,11),d(2009,11,1),d(2004,3,3),d(2000,1,23)],
                      [d(1976,8,8), d(1984,12,24), d(1979,2,4), d(1980,9,3)], [d(1763,2,7),d(1454,11,11),d(1133,2,23),d(1755,4,22)])
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Förväntade inte att värden frågas av användaren")]):
                reload_module(self.module)
                vuodet_listaan = load(exercise, function, 'fi')

                test_case_2 = test_case[:]
               
                val = vuodet_listaan(test_case)
                
                corr = get_corr(test_case_2)

                self.assertEqual(val, corr, f"Funktionen borde returnera \n{corr}\nmen den returnerar \n{val}\nnär argumentet är\n{test_case_2}")
                self.assertEqual(test_case, test_case_2, f"Funktionen får inte ändra listan den får som indata.\nListan är nu \n{test_case}, \när den borde vara \n{test_case_2}")

    

if __name__ == '__main__':
    unittest.main()
