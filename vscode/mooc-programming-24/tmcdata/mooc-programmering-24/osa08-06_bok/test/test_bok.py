import unittest
from unittest.mock import patch

from tmc import points, reflect
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint
from datetime import date

exercise = 'src.bok'
classname = "Bok"

def f(attr: list):
    return ",".join(attr)


@points('8.bok')
class KirjaTest(unittest.TestCase):
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
            from src.bok import Bok
        except:
            self.assertTrue(False, "Ditt program bör ha en klass med namnet Bok")

    def test2_konstruktori(self):
        try:
            from src.bok import Bok
            val = Bok("Python 1", "Pekka Python", "Tietokirja", 2010)
            taip = str(type(val)).replace("<class '","").replace("'>","")
            self.assertTrue(True, "")
        except Exception as e:
            self.assertTrue(False, 'Anropan på klassen Boks konstruktor med värdet (Bok("Python 1", "Pekka Python", "Tietokirja", 2010)' +
                f' returnerade ett fel: {e}')

    
    def test3_testaa_attribuutit(self):
        with patch('builtins.input', side_effect=[AssertionError("Förväntade inte att värden frågas av användaren")]):
            reload_module(self.module)
            from src.bok import Bok

            attributes = ("namn", "forfattare", "genre", "ar")

            for attr in attributes:
                ref = reflect.Reflect()
                ref.set_object(Bok("Python 1", "Pekka Python", "Tietokirja", 2010))

                self.assertTrue(ref.has_attribute(attr), f"Det returnerade objektet bör ha attributet {attr}," +  
                    f'\nnu är attributen \n{f(ref.list_attributes(True))}\nnär konstruktorn anropas med argumenten' + 
                    f'Bok("Python 1", "Pekka Python", "Tietokirja", 2010)')
    
    def test4_testaa_attribuuttien_tyypit(self):
        with patch('builtins.input', side_effect=[AssertionError("Förväntade inte att värden frågas av användaren")]):
            reload_module(self.module)
            from src.bok import Bok

            attributes = (("namn", str), ("forfattare", str), ("genre", str), ("ar", int))

            for attr in attributes:
                ref = reflect.Reflect()
                ref.set_object(Bok("Python 1", "Pekka Python", "Tietokirja", 2010))
                name,taip = attr

                taip_name = str(taip).replace("<class '", "").replace("'>", "")
                taip2 = str(type(ref.get_attribute(name))).replace("<class '","").replace("'>","")

                self.assertTrue(type(ref.get_attribute(name)) == taip, f"Typen av attributet {name} borde vara {taip_name}, nu är det {taip2}")

    def test5_testaa_attribuuttien_arvot(self):
         test_cases = [("Seitsemän veljestä", "Aleksis Kivi", "Romaani", 1870), 
                       ("Sinuhe egyptiläinen", "Mika Waltari", "Romaani", 1945),
                       ("Kyberias", "Stanislaw Lem", "Sci-fi", 1965), 
                       ("Kotona maailmankaikkeudessa", "Esko Valtaoja", "Tiede", 2001)]
         
         for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Förväntade inte att värden frågas av användaren")]):
                reload_module(self.module)
                from src.bok import Bok

                kirja = Bok(test_case[0], test_case[1], test_case[2], test_case[3])
                
                attributes = ("namn", "forfattare", "genre", "ar")
                ref = reflect.Reflect()
                ref.set_object(kirja)

                for i in range(len(attributes)):
                    value = ref.get_attribute(attributes[i])
                    self.assertEqual(value, test_case[i], 
                        f'Värdet på attributet {attributes[i]} borde vara {test_case[i]}, nu är det {value},\n när argumenten är \n{test_case}')


if __name__ == '__main__':
    unittest.main()
