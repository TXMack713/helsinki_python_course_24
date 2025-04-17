import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint

exercise = 'src.genrens_bocker'
function = "genrens_bocker"


@points('8.genrens_bocker')
class GenrenKirjatTest(unittest.TestCase):
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
            from src.genrens_bocker import genrens_bocker
        except:
            self.assertTrue(False, "Ditt program bör ha en funktion med namnet genrens_bocker(bocker: list, genre: str)")

    def test1b_luokkamaarittely_olemassa(self):
        try:
            from src.genrens_bocker import Bok
        except:
            self.assertTrue(False, "Ditt program bör innehålla en definierad klass Bok!")

    def test2_palautusarvon_tyyppi(self):
        try:
            from src.genrens_bocker import genrens_bocker
            from src.genrens_bocker import Bok
            
            val = genrens_bocker([Bok("Python","P. Python", "tieto", 2000), Bok("Java", "J.Java", "tieto", 2001)], "tieto")
            taip = str(type(val)).replace("<class '","").replace("'>","")
            self.assertTrue(type(val) == list, f"Funktionen genrens_bocker ska returnera en lista," +  
                f" nu returnerar den ett värde {val} som är av typen {taip}\n när den anropas med argumenten\n" + 
                'genrens_bocker([Bok("Python","P. Python", "tieto", 2000), Bok("Java", "J.Java", "tieto", 2001)])')
        except Exception as e:
            self.assertTrue(False, f"Funktionen gav ett fel när den anropades med parametervärdet\n" +
                f'genrens_bocker([Bok("Python","P. Python", "tieto", 2000), Bok("Java", "J.Java", "tieto", 2001)])\n{e}')


    def test3_testaa_lista1(self):
        test_case = [("Seitsemän veljestä", "Aleksis Kivi", "Romaani", 1870), 
                       ("Sinuhe egyptiläinen", "Mika Waltari", "Romaani", 1945),
                       ("Kyberias", "Stanislaw Lem", "Sci-fi", 1965), 
                       ("Kotona maailmankaikkeudessa", "Esko Valtaoja", "Tiede", 2001)]
        genre = "Romaani"
        
        with patch('builtins.input', side_effect=[AssertionError("Förväntade inte att värden frågas av användaren")]):
            reload_module(self.module)
            genren_kirjat = load(exercise, function, 'fi')
            from src.genrens_bocker import Bok

            lista = [Bok(x[0],x[1],x[2],x[3]) for x in test_case]
            corr = sorted([x for x in lista if x.genre == genre], key = lambda x: x.namn)
            val = sorted(genren_kirjat(lista, genre), key = lambda x: x.namn)
            
            self.assertEqual(corr, val, f"Funktionen ska returnerna en lista med värdena\n{corr}\n,nu returnerar den listan\n{val}\ndå böckerna är\n{test_case}")

    def test4_testaa_lista2(self):
        test_case = [("Seitsemän veljestä", "Aleksis Kivi", "Romaani", 1870), 
                       ("Sinuhe egyptiläinen", "Mika Waltari", "Romaani", 1945),
                       ("Kyberias", "Stanislaw Lem", "Sci-fi", 1965), 
                       ("Kotona maailmankaikkeudessa", "Esko Valtaoja", "Tiede", 2001),
                       ("Avaruusseikkalu 2001", "Arthur C. Clarke", "Sci-fi", 1968)]
        genre = "Sci-fi"
        
        with patch('builtins.input', side_effect=[AssertionError("Förväntade inte att värden frågas av användaren")]):
            reload_module(self.module)
            genren_kirjat = load(exercise, function, 'fi')
            from src.genrens_bocker import Bok

            lista = [Bok(x[0],x[1],x[2],x[3]) for x in test_case]
            corr = sorted([x for x in lista if x.genre == genre], key = lambda x: x.namn)
            val = sorted(genren_kirjat(lista, genre), key = lambda x: x.namn)
            
            self.assertEqual(corr, val, f"Funktionen ska returnerna en lista med värdena\n{corr}\n,nu returnerar den listan\n{val}\ndå böckerna är\n{test_case}")

                
    

if __name__ == '__main__':
    unittest.main()
