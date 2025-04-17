import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint

exercise = 'src.minsta_medeltalet'
function = "minsta_medeltalet"

def hlo(t: tuple):
    return {"namn": "Anna", "resultat1": t[0], "resultat2": t[1], "resultat3": t[2]}

def par(t1: tuple, t2: tuple, t3: tuple):
    s = "("
    for t in (t1,t2,t3):
        s += "{" + ",".join([f'"resultat{x}": {t[x-1]}' for x in range(1,4)]) + "}" + ", "
    return s[:-2] + ")"
        

@points('8.minsta_medeltalet')
class PieninKeskiarvoTest(unittest.TestCase):
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
            from src.minsta_medeltalet import minsta_medeltalet
        except:
            self.assertTrue(False, "Ditt program bör ha en funktion med namnet minsta_medeltalet(h1: dict, h2: dict, h3: dict)")

    def test2_palautusarvon_tyyppi(self):
        try:
            from src.minsta_medeltalet import minsta_medeltalet
            val = minsta_medeltalet(hlo((1,1,1)), hlo((2,2,2)), hlo((3,3,3)))
            taip = str(type(val)).replace("<class '","").replace("'>","")
            self.assertTrue(type(val) == dict, f"Funktionen minsta_medeltalet borde returnera ett värde av typen dict," +  
                f" nu returnerar den värdet {val} som är av typen {taip}\n när den anropas med argumentet {par((1,1,1),(2,2,2),(3,3,3))}")
        except:
            self.assertTrue(False, f"Funktionen gav ett fel när den anropades med argumentvärdet {par((1,1,1),(2,2,2),(3,3,3))}")


    def test3_testaa_arvot(self):
        test_cases = [((1,1,1),(2,2,2),(3,3,3)), ((9,9,9),(7,7,7),(8,8,8)), ((3,3,3),(5,5,5), (1,1,1)), 
                      ((5,3,1),(6,4,2),(2,2,2)), ((9,3,8),(9,4,9),(9,6,8)), ((6,0,0), (5,0,0), (3,3,3)),
                      ((6,4,4),(5,7,7),(4,8,8)), ((4,3,4),(4,2,4),(4,3,4)), ((6,2,2), (5,2,2), (5,2,3))]
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Förväntade inte att värden frågas av användaren")]):
                reload_module(self.module)
                pienin_keskiarvo = load(exercise, function, 'fi')

                h1 = hlo(test_case[0])
                h2 = hlo(test_case[1])
                h3 = hlo(test_case[2])

                results = [sum(test_case[0]),sum(test_case[1]),sum(test_case[2])]
                results.sort()
                if results[0] == results[1]:
                    self.fail("fel i testerna: det minsta medeltalet är inte unikt")

                val = pienin_keskiarvo(h1, h2, h3)

                t1 = hlo(test_case[0])
                t2 = hlo(test_case[1])
                t3 = hlo(test_case[2])
                corr = min((t1,t2,t3), key=lambda x: ((x["resultat1"]+x["resultat2"]+x["resultat3"]) / 3))

                self.assertEqual(val, corr, f"Funktionen borde returnera \n{corr}\nmed returnerar \n{val}\nnär parametrarna är\n{par(test_case[0], test_case[1], test_case[2])}")

    

if __name__ == '__main__':
    unittest.main()
