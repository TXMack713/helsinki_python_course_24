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

exercise = 'src.for_och_efternamn'

def f(attr: list):
    return ",".join(attr)

@points('8.for_och_efternamn')
class EtuJaSukunimiTest(unittest.TestCase):
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
            from src.for_och_efternamn import Person
        except:
            self.assertTrue(False, "Ditt program bör ha en klass med namnet Person")


    def test2_konstruktori(self):
        try:
            from src.for_och_efternamn import Person
            val = Person("Pekka Python")
            self.assertTrue(True, "")
        except Exception as e:
            self.assertTrue(False, 'Anropning av klassen Persons konstruktor med värdet Person("Pekka Python")' +
                f' returnerade ett fel: {e}')

    def test3_testaa_etunimi(self):
        test_cases = ("Pekka Python", "Paula Pascal", "Jarmo Java", "Heikki Haskell", "Benjamin Basic", "Carlos Ceesharp")
        for test_case in test_cases:
            try:
                from src.for_och_efternamn import Person
                hlo = Person(test_case)
                val = hlo.ge_fornamn()
                corr = test_case.split(" ")[0]

                self.assertEqual(val, corr, f"Metoden ge_fornamn borde returnera {corr}, då räknaren påbörjades med anropet\n" +
                    f"Person('{test_case}')\nNu returnerar metoden\n{val}")
                    
            except Exception as e:
                self.assertTrue(False, f"Anropning av metoden ge_fornamn åstadkom ett fel:\n{e}" +
                    f"då objektet inbitialiserades med anropningen Person{(test_case)}")

    def test4_testaa_sukunimi(self):
        test_cases = ("Pekka Python", "Paula Pascal", "Jarmo Java", "Heikki Haskell", "Benjamin Basic", "Carlos Ceesharp")
        for test_case in test_cases:
            try:
                from src.for_och_efternamn import Person
                hlo = Person(test_case)
                val = hlo.ge_efternamn()
                corr = test_case.split(" ")[-1]

                self.assertEqual(val, corr, f"Metoden ge_efternamn borde returnera {corr}, då räknaren påbörjades med anropet\n" +
                    f"Person('{test_case}')\nNu returnerar metoden\n{val}")
                    
            except Exception as e:
                self.assertTrue(False, f"Anropning av metoden ge_efternamn åstadkom ett fel:\n{e}" +
                    f"då objektet inbitialiserades med anropningen Person{(test_case)}")

    def test5_testaa_attribuutit(self):
        try:
            from src.for_och_efternamn import Person
            hlo = Person("Eka Vekara")
            en = hlo.ge_fornamn()
            sn = hlo.ge_efternamn()

            
        except Exception as e:
            self.fail(f"Ett fel åstadkoms:\n{e}" +
                    f"då objektet inbitialiserades med anropningen Person('Eka Vekara')\n" + 
                    "och anropades metoderna ge_fornamn() och ge_efternamn()")

        ref = reflect.Reflect(hlo)
        ref.set_object(hlo)
        att_list = ref.attributes_only()
        

        self.assertTrue(len(att_list) == 1, f"Klassen Person får ha endast ett attribut, nu har den {len(att_list)}\n" + 
            f"Bekräfta att du inte använder self-definitionen i onödan då du skapar en lokal vartiabel!\n" + 
            f"I klassen finns nu följande attribut:\n{att_list}")



    

if __name__ == '__main__':
    unittest.main()
