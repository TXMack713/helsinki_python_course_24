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

exercise = 'src.minskande_raknare'
classname = "MinskandeRaknare"

def f(attr: list):
    return ",".join(attr)



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

    @points('8.minskande_raknare_del1')
    def test1_luokka_olemassa(self):
        try:
            from src.minskande_raknare import MinskandeRaknare
        except:
            self.assertTrue(False, "Ditt program bör ha en klass med namnet MinskandeRaknare")

    @points('8.minskande_raknare_del1')
    def test2_konstruktori(self):
        try:
            from src.minskande_raknare import MinskandeRaknare
            val = MinskandeRaknare(1)
            self.assertTrue(True, "")
        except Exception as e:
            self.assertTrue(False, 'Anropning av konstruktorn för klassen MinskandeRaknare med värdet (MinskandeRaknare(1)' +
                f' returnerade ett fel: {e}')

    @points('8.minskande_raknare_del1')
    def test3_testaa_vahenna(self):
        test_cases = ((5,1), (9,4), (100,10), (1,1))
        for test_case in test_cases:
            try:
                from src.minskande_raknare import MinskandeRaknare
                laskuri = MinskandeRaknare(test_case[0])
                for i in range(test_case[1]):
                    laskuri.minska()
                corr = test_case[0] - test_case[1]

                self.assertEqual(laskuri.varde, corr, f"Räknarens värde borde vara {corr}, då räknaren påbörjades med anropet\n" +
                    f"MinskandeRaknare({test_case[0]})\noch metoden minska anropades {test_case[1]} gånger.\n" +
                    f"Nu är räknarens värde {laskuri.varde}.")
            except Exception as e:
                self.assertTrue(False, f"Anropning av metoden minska orsakade ett fel:\n{e}" +
                    f"då objektet skapades med anropet MinskandeRaknare{(test_case[0])}")

    @points('8.minskande_raknare_del2')
    def test4_testaa_negatiivinen(self):
        test_cases = ((1,2), (3,6), (100,101), (1,10))
        for test_case in test_cases:
            try:
                from src.minskande_raknare import MinskandeRaknare
                laskuri = MinskandeRaknare(test_case[0])
                for i in range(test_case[1]):
                    laskuri.minska()
                corr = 0

                self.assertEqual(laskuri.varde, corr, f"Räknarens värde borde vara {corr}, då räknaren påbörjades med anropet\n" +
                    f"MinskandeRaknare({test_case[0]})\noch metoden minska anropades {test_case[1]} gånger.\n" +
                    f"Nu är räknarens värde {laskuri.varde}.\nRäknarens värde får inte vara negativt!")
            except Exception as e:
                self.assertTrue(False, f"Anropning av metoden minska orsakade ett fel:\n{e}" + 
                    f"då objektet skapades med anropet MinskandeRaknare{(test_case[0])}")

    @points('8.minskande_raknare_del3')
    def test5_testaa_nollaus(self):
        test_cases = ((1,0), (3,0), (100,10))
        for test_case in test_cases:
            try:
                from src.minskande_raknare import MinskandeRaknare
                laskuri = MinskandeRaknare(test_case[0])
                for i in range(test_case[1]):
                    laskuri.minska()
                laskuri.nolla()
                corr = 0

                self.assertEqual(laskuri.varde, corr, f"Räknarens värde borde vara {corr}, då räknaren påbörjades med anropet\n" +
                    f"MinskandeRaknare({test_case[0]}),\nmetoden minska anropades {test_case[1]} gånger,\n" +
                    f"och metoden nolla sedan anropades().\n" + 
                    f"Nu är räknarens värde {laskuri.varde}.")
            except Exception as e:
                self.assertTrue(False, f"Åstadkoms ett fel:\n{e}"
                    f"då objektet skapades med anropet MinskandeRaknare{(test_case[0])}" +
                    "\nmetoden minska anropades {test_case[1]} gånger,\n" +
                    f"och metoden nolla sedan anropades().")

    @points('8.minskande_raknare_del4')
    def test6_testaa_palautus(self):
        test_cases = ((2,1), (3,3), (100,20), (5,10))
        for test_case in test_cases:
            try:
                from src.minskande_raknare import MinskandeRaknare
                laskuri = MinskandeRaknare(test_case[0])
                for i in range(test_case[1]):
                    laskuri.minska()
                laskuri.aterstall_ursprungligt_varde()
                corr = test_case[0]

                self.assertEqual(laskuri.varde, corr, f"Räknarens värde borde vara {corr}, då räknaren påbörjades med anropet\n" +
                    f"MinskandeRaknare({test_case[0]}),\nmetoden minska anropades {test_case[1]} gånger,\n" +
                    f"och metoden atarstall_ursprungligt_varde() sedan anropades.\n" + 
                    f"Nu är räknarens värde {laskuri.varde}.")
            except Exception as e:
                self.assertTrue(False, f"Åstadkoms ett fel:\n{e}"
                    f"då objektet skapades med anropet MinskandeRaknare{(test_case[0])}" +
                    "\nmetoden minska anropades {test_case[1]} gånger,\n" +
                    f"och metoden atarstall_ursprungligt_varde() sedan anropades.")

    

if __name__ == '__main__':
    unittest.main()
