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

exercise = 'src.nummerstatistik'

def f(attr: list):
    return ",".join(attr)

class TilastoTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["0","-1"]):
           cls.module = load_module(exercise, 'fi')

    def test0a_paaohjelma_kunnossa(self):
        with open("src/nummerstatistik.py") as t:
            if "if __name__" in t.read():
                self.assertTrue(False, 'Huvudprogrammet får inte skrivas innanför if __name__ == "__main__":')

    @points('8.nummerstatistik_del1')
    def test1_luokka_olemassa(self):
        with patch('builtins.input', side_effect=["0","-1"]):
            try:
                from src.nummerstatistik import Nummerstatistik
            except:
                self.assertTrue(False, "Ditt program bör ha en klass med namnet Nummerstatistik")

    @points('8.nummerstatistik_del1')
    def test2_konstruktori(self):
        with patch('builtins.input', side_effect=["0","-1"]):
            try:
                from src.nummerstatistik import Nummerstatistik
                val = Nummerstatistik()
            except Exception as e:
                self.fail('Anropning av klassen Nummerstatistiks konstruktor Nummerstatistik()' +
                    f' returnerade ett fel: {e}')

    @points('8.nummerstatistik_del1')
    def test2b_testaa_metodit(self):
        from src.nummerstatistik import Nummerstatistik
        tilasto = Nummerstatistik()
        try:
            tilasto.tillsatt_nummer(1)
        except Exception as e:
            self.fail(f"Metodanropet tillsatt_nummer(1) gav ett fel {e}, " +
                "Granska att metoden hittas i klassen!")
        try:
            tilasto.mangden_nummer()
        except Exception as e:
            self.fail(f"Metodanropet mangden_nummer() gav ett fel {e}, " +
                "Granska att metoden hittas i klassen!")
        

    @points('8.nummerstatistik_del1')
    def test3_testaa_lukujen_maara(self):
        test_cases = ([1], (2,3,4,2), (9,8,7,5,3,2,4,1), (3,3), (5,5,5,5,4,4,4,4,3,3,3,3,4,4,4,4))
        for test_case in test_cases:
            with patch('builtins.input', side_effect=["0","-1"]):    
                try:
                    from src.nummerstatistik import Nummerstatistik
                    lukutilasto = Nummerstatistik()
                    for luku in test_case:
                        lukutilasto.tillsatt_nummer(luku)
                    corr = len(test_case)
                except Exception as e:
                    self.assertTrue(False, f"Användning av klassen åstadkom ett fel:\n{e}" +
                        "\ndå statistiken initialiserar med anropet\n" +
                        f"Nummerstatistik()\noch metoden tillsatt_nummer anropades med värdena {test_case}")

                self.assertEqual(lukutilasto.mangden_nummer(), corr, f"Mängden nummer borde vara {corr}, då statistiken initialiserar med anropet\n" +
                    f"Nummerstatistik()\noch metoden tillsatt_nummer anropades med värdena {test_case}.\n" +
                    f"Nu returnerar metoden mangden_nummer däremot {lukutilasto.mangden_nummer()}.")
                

    @points('8.nummerstatistik_del2')
    def test3_testaa_summa(self):
        from src.nummerstatistik import Nummerstatistik
        lukutilasto = Nummerstatistik()
        lukutilasto.tillsatt_nummer(1)
        try:
            lukutilasto.summa()
        except Exception as e:
            self.fail(f"Metodanropet summa() gav ett fel {e}, " +
                "Granska att metoden hittas i klassen!")
       
        test_cases = ([1], (2,3), (5,4,3,4,5), (3,3), (5,5,5,5,4,4,4,4,3,3,3,3,4,4,4,4))
        for test_case in test_cases:
            with patch('builtins.input', side_effect=["0","-1"]):
                lukutilasto = Nummerstatistik()
                for luku in test_case:
                    lukutilasto.tillsatt_nummer(luku)
                corr = sum(test_case)
                val = lukutilasto.summa()

                self.assertEqual(val, corr, f"Talens summa borde vara {corr}, då statistiken initialiserar med anropet\n" +
                    f"Nummerstatistik()\noch metoden tillsatt_nummer anropades med värdena {test_case}.\n" +
                    f"Nu returnerar metoden summa() däremot {val}.")

                # Testataan, ettei määrä hajonnut tässä välissä
                self.assertEqual(lukutilasto.mangden_nummer(), len(test_case), f"Mängden nummer borde vara {len(test_case)}, då statistiken initialiserar med anropet\n" +
                    f"Nummerstatistik()\noch metoden tillsatt_nummer anropades med värdena {test_case}.\n" +
                        f"Nu returnerar metoden mangden_nummer däremot {lukutilasto.mangden_nummer()}.")

    @points('8.nummerstatistik_del2')
    def test_3_testaa_tyhja_keskiarvo(self):
        try:
            from src.nummerstatistik import Nummerstatistik
            lukutilasto = Nummerstatistik()
            lukutilasto.medeltal()
        except ZeroDivisionError:
            self.assertTrue(False, "Du delar väl inte med noll, då du anropar nummerstatistik.medeltal() med en tom statistik.")
        except Exception as e:
                self.assertTrue(False, f"Användning av klassen åstadkom ett fel:\n{e}")

    @points('8.nummerstatistik_del2')
    def test3_testaa_keskiarvo(self):
        from src.nummerstatistik import Nummerstatistik
        lukutilasto = Nummerstatistik()
        try:
            lukutilasto.medeltal()
        except Exception as e:
            self.fail(f"Metodanropet medeltal() gav ett fel {e}, " +
                "Granska att metoden hittas i klassen!")
        
        test_cases = ([1,1], (2,3), (1,2,3,4), (3,3), (5,5,5,5,4,4,4,4))
        for test_case in test_cases:
            lukutilasto = Nummerstatistik()
            with patch('builtins.input', side_effect=["0","-1"]):            
                for luku in test_case:
                    lukutilasto.tillsatt_nummer(luku)
                corr = sum(test_case) / len(test_case)
                val = lukutilasto.medeltal()

                self.assertEqual(val, corr, f"Talens medeltal borde vara {corr}, då statistiken initialiserar med anropet\n" +
                    f"Nummerstatistik()\noch metoden tillsatt_nummer anropades med värdena {test_case}.\n" +
                    f"Nu returnerar metoden medeltal() däremot {val}.")
                
  
    @points('8.nummerstatistik_del3')
    def test3_testaa_input_summa_ja_ka(self):
        test_cases = ([1,-1], (2,3,-1), (5,4,3,4,5,-1), (3,3,-1), (5,5,5,5,4,4,4,4,3,3,3,3,4,4,4,4,-1))
        for test_case in test_cases:
            with patch('builtins.input', side_effect=list([str(x) for x in test_case])):
                reload_module(self.module)

                output = get_stdout()

                summa = sum([x for x in test_case if x != -1])
                ka = summa / (len(test_case) - 1)

                corr1 = f"Summa: {summa}"
                corr2 = f"Medeltal: {ka}"

                self.assertTrue(corr1 in output, f"Utskriften borde innehålla raden\n{corr1}\ndå indatan är \n{test_case}.\nNu är utskriften\n{output}")
                self.assertTrue(corr2 in output, f"Utskriften borde innehålla raden\n{corr2}\ndå indatan är \n{test_case}.\nNu är utskriften\n{output}")

    @points('8.nummerstatistik_del4')
    def test3_testaa_input_parilliset_parittomat(self):
        test_cases = ([1,2,-1], (1,2,3,2,3,2,-1), (5,4,3,4,5,-1), (10,9,8,7,6,5,4,3,2,1,-1))
        for test_case in test_cases:
            with patch('builtins.input', side_effect=list([str(x) for x in test_case])):
                reload_module(self.module)

                output = get_stdout()

                even = sum([x for x in test_case if x % 2 == 0])
                odd = sum([x for x in test_case if x % 2 != 0 and x != -1])

                corr1 = f"Jämna talens summa: {even}"
                corr2 = f"Udda talens summa: {odd}"

                self.assertTrue(corr1 in output, f"Utskriften borde innehålla raden\n{corr1}\ndå indatan är \n{test_case}.\nNu är utskriften\n{output}")
                self.assertTrue(corr2 in output, f"Utskriften borde innehålla raden\n{corr2}\ndå indatan är \n{test_case}.\nNu är utskriften\n{output}")

   

if __name__ == '__main__':
    unittest.main()
