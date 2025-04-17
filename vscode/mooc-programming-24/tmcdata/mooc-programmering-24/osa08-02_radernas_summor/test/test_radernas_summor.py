import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint

exercise = 'src.radernas_summor'
function = "radernas_summor"

def get_corr(m):
    return [r + [sum(r)] for r in m]
        

@points('8.radernas_summor')
class RivienSummatTest(unittest.TestCase):
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
            from src.radernas_summor import radernas_summor
        except:
            self.assertTrue(False, "Ditt program bör ha en funktion med namnet radernas_summor(matris: list)")

    def test2_palautusarvon_tyyppi(self):
        try:
            from src.radernas_summor import radernas_summor
            val = radernas_summor([[1,1],[2,2]])
            taip = str(type(val)).replace("<class '","").replace("'>","")
            self.assertTrue(val == None, f"Funktionen radernas_summor borde inte returnera ett värde," +  
                f" nu returnerar den ett värde {val} som är av typen {taip}\n när den anropas med argumentet \n[[1,1],[2,2]]")
        except Exception as e:
            self.assertTrue(False, f"Funktionen gav ett fel när den anropades med argumentvärdet [[1,1],[2,2]]:\n{e}")


    def test3_testaa_arvot(self):
        test_cases = ([[1,1],[2,2]], [[2]*3,[4]*3,[6]*3], [[1,2,3,4],[2,3,4,5],[3,4,5,6]], [[5,6],[4,1],[10,20],[6,9],[11,22]],
                      [[1,3,5,7,9],[2,4,6,8,10],[-1,-3,-5,-7,-9]])
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Förväntade inte att värden frågas av användaren")]):
                reload_module(self.module)
                rivien_summat = load(exercise, function, 'fi')

                test_case_2 = [m[:] for m in test_case[:]]
                rivien_summat(test_case)
                
                corr = get_corr(test_case_2)

                self.assertEqual(test_case, corr, f"Efter funktionens exekvering borde matrisen vara \n{corr}\nmen den är \n{test_case}\ndå argumentet är\n{test_case_2}")

    

if __name__ == '__main__':
    unittest.main()
