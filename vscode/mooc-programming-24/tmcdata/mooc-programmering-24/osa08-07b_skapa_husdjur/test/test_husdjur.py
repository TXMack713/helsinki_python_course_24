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

exercise = 'src.skapa_husdjur'
function = "nytt_husdjur"

def f(attr: list):
    return ",".join(attr)


@points('8.skapa_husdjur')
class LemmikkiTest(unittest.TestCase):
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

    def test_0b_konstruktori(self):
        try:
            from src.skapa_husdjur import Husdjur
            musti = Husdjur("Musti","Koira",2014)
        except Exception as e:
            self.fail(f'Konstruktoranropet Husdjur("Musti","Koira",2014) gav ett fel \n{e}')


    def test1_funktio_olemassa(self):
        try:
            from src.skapa_husdjur import nytt_husdjur
        except:
            self.assertTrue(False, "Ditt program bör ha en funktion " + 
                "med namnet nytt_husdjur(namn: str, ras: str, fodelsear: int)")

    def test2_palautusarvon_tyyppi(self):
        try:
            from src.skapa_husdjur import nytt_husdjur
            val = nytt_husdjur("Musti","koira",1970)
        except Exception as e:
            self.fail('Funktionen åstadkom ett fel då den anropades med argumenten nytt_husdjur("Musti","koira",1970)')
        taip = str(type(val)).replace("<class '","").replace("'>","")
        self.assertTrue("Husdjur" in str(type(val)), f"Funktion nytt_husdjur borde returnera ett värde av typen Husdjur," +  
            f' nu returnerar den ett värde {val} som är av typen {taip}\n när den anropas med argumenten nytt_husdjur("Musti","koira",1970)')
        


    def test3_testaa_attribuutit(self):
        with patch('builtins.input', side_effect=[AssertionError("Förväntade inte att värden frågas av användaren")]):
            reload_module(self.module)
            uusi_lemmikki = load(exercise, function, 'fi')

            attributes = ("namn", "ras", "fodelsear")

            for attr in attributes:
                ref = reflect.Reflect()
                ref.set_object(uusi_lemmikki("Musti","koira",1970))

                self.assertTrue(ref.has_attribute(attr), f"Det returnerade Husdjur-objektet borde ha attributet {attr}," +  
                    f'\nnu är attributen\n{f(ref.list_attributes(True))}\ndå funktionen anropades med argumenten ("Musti","koira",1970)')
    
    def test4_testaa_attribuuttien_tyypit(self):
        with patch('builtins.input', side_effect=[AssertionError("Förväntade inte att värden frågas av användaren")]):
            reload_module(self.module)
            uusi_lemmikki = load(exercise, function, 'fi')

            attributes = (("namn", str), ("ras", str), ("fodelsear", int))

            for attr in attributes:
                ref = reflect.Reflect()
                ref.set_object(uusi_lemmikki("Musti","koira",1970))
                name,taip = attr

                taip2 = str(type(ref.get_attribute(name))).replace("<class '","").replace("'>","")

                self.assertTrue(type(ref.get_attribute(name)) == taip, f"Typen på attributet {name} borde vara {taip}, nu är det {taip2}")

    def test5_testaa_attribuuttien_arvot(self):
         test_cases = [("Musti","koira",1970), ("Viiru","kissa",1986), ("Tiku","orava",1999),("Dumbo","norsu",1963)]
         
         for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Förväntade inte att värden frågas av användaren")]):
                reload_module(self.module)
                uusi_lemmikki = load(exercise, function, 'fi')

                val = uusi_lemmikki(test_case[0], test_case[1], test_case[2])
                
                attributes = ("namn", "ras", "fodelsear")
                ref = reflect.Reflect()
                ref.set_object(val)

                for i in range(len(attributes)):
                    value = ref.get_attribute(attributes[i])
                    self.assertEqual(value, test_case[i], 
                        f'Värdet på attributet {attributes[i]} borde vara {test_case[i]}, nu är det {value},\n då argumenten är {test_case}')
if __name__ == '__main__':
    unittest.main()
