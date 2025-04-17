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
from src.affarslista import Affarslista

exercise = 'src.affarslista'
function = "totala_mangd"

def get_corr(l):
    return sum(l.mangd(i) for i in range(1, l.mangden_foremal() + 1))

def gen(l: list):
    k = Affarslista()
    for i in l:
        k.tillagg(i[0],i[1])
    return k

def format(l: list):
    return "\n".join([f"{x[0]}: {x[1]} st." for x in l])

        

@points('8.affarslista')
class KauppalistaTest(unittest.TestCase):
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
            from src.affarslista import totala_mangd
        except:
            self.assertTrue(False, "Ditt program bör ha en funktion med namnet totala_mangd(lista: Affarslista)")

    def test2_palautusarvon_tyyppi(self):
        try:
            from src.affarslista import totala_mangd
            lista = gen([("omena",1)])
            val = totala_mangd(lista)
            taip = str(type(val)).replace("<class '","").replace("'>","")
            self.assertTrue(type(val) == int, f"Funktionen totala_mangd borde returnera ett värde av typen int," +  
                f" nu returnerar den ett värde {val} som är av typen {taip}\n när den anropas på en lista som har ett föremål")
        except Exception as e:
            self.assertTrue(False, f"Funktionen gav ett fel när den anropades på ett Affarslista-objekt som har ett föremål:\n{e}")


    def test3_testaa_arvot(self):
        d = date
        test_cases = ([("omena",5),("appelsiini",5)], [("omena",4),("appelsiini",5),("banaani",6)],
                      [("marsu", 2), ("hamsteri",8), ("gerbiili", 6)], [("auto",24),("mopo",40),("moottoripyörä",10),("kuorma-auto",5)], 
                      [("ruusu",100),("orvokki",90),("sinivuokko",80),("lilja",70),("valkovuokko",60)])

        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Förväntade inte att värden frågas av användaren")]):
                reload_module(self.module)
                tuotteita_yhteensa = load(exercise, function, 'fi')

                lista = gen(test_case)
               
                val = tuotteita_yhteensa(lista)
                corr = get_corr(lista)

                self.assertEqual(val, corr, f"Funktionen borde returnera värdet {corr}\nmen den returnerar värdet {val}\nnär listan innehåller föremålen \n{format(test_case)}")
    

if __name__ == '__main__':
    unittest.main()
