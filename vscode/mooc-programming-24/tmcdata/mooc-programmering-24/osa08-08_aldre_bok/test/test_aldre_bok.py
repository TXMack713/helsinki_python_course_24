import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint

exercise = 'src.aldre_bok'
function = "aldre_bok"


@points('8.aldre_bok')
class VanhempiKirjaTest(unittest.TestCase):
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
            from src.aldre_bok import aldre_bok
        except:
            self.assertTrue(False, "Ditt program bör ha en funktion med namnet aldre_bok(bok1: Bok, bok2: Bok)")

    def test1b_luokkamaarittely_olemassa(self):
        try:
            from src.aldre_bok import Bok
        except:
            self.assertTrue(False, "Ditt program ska innehålla en definierad klass Bok!")

    def test2_palautusarvon_tyyppi(self):
        try:
            from src.aldre_bok import aldre_bok
            from src.aldre_bok import Bok
            
            val = aldre_bok(Bok("Python","P. Python", "tieto", 2000), Bok("Java", "J.Java", "tieto", 2001))
            taip = str(type(val)).replace("<class '","").replace("'>","")
            self.assertTrue(val == None, f"Funktionen aldre_bok borde inte returnera ett värde," +  
                f" nu returnerar den ett värde {val} som är av typen {taip}\n när den anropas med argumenten\n" + 
                'aldre_bok(Bok("Python","P. Python", "tieto", 2000), Bok("Java", "J.Java", "tieto", 2001))')
        except Exception as e:
            self.assertTrue(False, f"Funktionen gav ett fel när den anropades med parametervärdet [[1,1],[2,2]]:\n{e}")


    def test3_testaa_eka_vanhempi(self):
        test_cases = ((("Seitsemän veljestä", "Aleksis Kivi", "Romaani", 1870), 
                       ("Sinuhe egyptiläinen", "Mika Waltari", "Romaani", 1945)),
                       (("Kyberias", "Stanislaw Lem", "Sci-fi", 1965), 
                       ("Kotona maailmankaikkeudessa", "Esko Valtaoja", "Tiede", 2001)))
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Förväntade inte att värden frågas av användaren")]):
                reload_module(self.module)
                vanhempi_kirja = load(exercise, function, 'fi')
                from src.aldre_bok import Bok

                k1,k2 = test_case
                kirja1 = Bok(k1[0],k1[1],k1[2],k1[3])
                kirja2 = Bok(k2[0],k2[1],k2[2],k2[3])
                vanhempi = kirja1
                ei_vanhempi = kirja2

                corr = f"{vanhempi.namn} är äldre, den publicerades {vanhempi.ar}"

                vanhempi_kirja(kirja1,kirja2)
                
                output = get_stdout()
                output = output.replace("\n","").strip()

                self.assertTrue("äldre" in output and vanhempi.namn in output and ei_vanhempi.namn not in output and 
                    str(vanhempi.ar) in output and str(ei_vanhempi.ar) not in output, 
                    f"Programmets utdata\n{output}\nmatchar inte modellsvaret\n{corr}\ndå böckerna är\n{test_case}")

    def test4_testaa_toka_vanhempi(self):
        test_cases = ((("Kahdeksan veljestä", "Aleksis Kivelä", "Romaani", 1993), 
                       ("Sinuhe egyptiläinen", "Mika Waltari", "Romaani", 1945)),
                       (("Loiri", "Jari Tervo", "Elämäkerta", 2019), 
                       ("Kotona maailmankaikkeudessa", "Esko Valtaoja", "Tiede", 2001)))
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Förväntade inte att värden frågas av användaren")]):
                reload_module(self.module)
                vanhempi_kirja = load(exercise, function, 'fi')
                from src.aldre_bok import Bok

                k1,k2 = test_case
                kirja1 = Bok(k1[0],k1[1],k1[2],k1[3])
                kirja2 = Bok(k2[0],k2[1],k2[2],k2[3])
                vanhempi = kirja2
                ei_vanhempi = kirja1

                corr = f"{vanhempi.namn} är äldre, den publicerades {vanhempi.ar}"

                vanhempi_kirja(kirja1,kirja2)
                
                output = get_stdout()
                output = output.replace("\n","").strip()

                self.assertTrue("äldre" in output and vanhempi.namn in output and ei_vanhempi.namn not in output and 
                    str(vanhempi.ar) in output and str(ei_vanhempi.ar) not in output, 
                    f"Programmets utdata\n{output}\nmatchar inte modellsvaret\n{corr}\ndå böckerna är\n{test_case}")

    def test5_testaa_yhta_vanhat(self):
        test_cases = ((("Kahdeksan veljestä", "Aleksis Kivelä", "Romaani", 1993), 
                       ("Sinuhe ruotsalainen", "Mikko Waltanen", "Romaani", 1993)),
                       (("Loiri", "Jari Tervo", "Elämäkerta", 2019), 
                       ("Veteen syntyneet", "Akseli Heikkilä", "Romaani", 2019)))
        for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Förväntade inte att värden frågas av användaren")]):
                reload_module(self.module)
                vanhempi_kirja = load(exercise, function, 'fi')
                from src.aldre_bok import Bok

                k1,k2 = test_case
                kirja1 = Bok(k1[0],k1[1],k1[2],k1[3])
                kirja2 = Bok(k2[0],k2[1],k2[2],k2[3])
               
                corr = f"{kirja1.namn} och {kirja2.namn} publicerades {kirja1.ar}"

                vanhempi_kirja(kirja1,kirja2)
                
                output = get_stdout()
                output = output.replace("\n","").strip()

                self.assertTrue("och" in output and kirja1.namn in output and kirja2.namn in output and 
                    str(kirja1.ar) in output, 
                    f"Programmets utdata\n{output}\nmatchar inte modellsvaret\n{corr}\ndå böckerna är\n{test_case}")
                
    

if __name__ == '__main__':
    unittest.main()
