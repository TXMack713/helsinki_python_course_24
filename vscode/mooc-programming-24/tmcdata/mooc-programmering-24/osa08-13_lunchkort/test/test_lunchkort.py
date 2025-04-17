import unittest
from unittest.mock import patch

from tmc import points, reflect
from tmc.utils import load, load_module, reload_module, get_stdout, check_source
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint
from datetime import date, datetime, timedelta

exercise = 'src.lunchkort'
classname = "Lunchkort"

def f(attr: list):
    return ",".join(attr)

class MaksukorttiTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=[AssertionError("Förväntade inte att värden frågas av användaren")]):
           cls.module = load_module(exercise, 'fi')

    def test_0a_paaohjelma_kunnossa(self):
        with open("src/lunchkort.py") as t:
            if "if __name__" in t.read():
                self.assertTrue(False, 'Huvudprogrammet får inte skrivas innanför if __name__ == "__main__": blocket')

    @points('8.lunchkort_del1')
    def test1_luokka_olemassa(self):
        try:
            from src.lunchkort import Lunchkort
        except:
            self.assertTrue(False, "Ditt program bör ha en klass med namnet Lunchkort")

    @points('8.lunchkort_del1')
    def test2_konstruktori(self):
        try:
            from src.lunchkort import Lunchkort
            kortti = Lunchkort(100)
            self.assertTrue(True, "")
        except Exception as e:
            self.assertTrue(False, 'Anropning av klassen Lunchkorts konstruktorn med värdet Lunchkort(100)' +
                f' returnerade ett fel: {e}\nGranska att konstruktorn är definierad korrekt')

    @points('8.lunchkort_del1')
    def test3_testaa_str(self):
        test_cases = (100, 25, 0, 10, 23)
        for test_case in test_cases:
            try:
                from src.lunchkort import Lunchkort
                kortti = Lunchkort(test_case)

                corr = f'Kortets saldo är {test_case:.1f} euro'
                val = str(kortti)

                self.assertEqual(corr, val, f"Metoden __str__ borde returnera strängen\n{corr}\nkun olio luotiin kutsulla\n" + 
                    f"Lunchkort({test_case})\nNu returnerar metoden strängen\n{val}")

            except Exception as e:
                self.assertTrue(False, f'Anropning av metoden __str__ returnerade ett fel: {e}\ndå objektet skapades med anropet\nLunchkort({test_case})')

    @points('8.lunchkort_del2')
    def test4_syo_edullisesti_olemassa(self):
        try:
            from src.lunchkort import Lunchkort 
            koodi = """
kortti = Lunchkort(10)
kortti.at_formanligt()"""

            kortti = Lunchkort(10)
            kortti.at_formanligt()  

        except Exception as e:
            self.assertTrue(False, f'Exekvering av koden\n{koodi}\nåstadkom ett fel\n{e}\nNog är väl metoden at_formanligt(self) definierad?')

    @points('8.lunchkort_del2')
    def test5_syo_edullisesti(self):
            from src.lunchkort import Lunchkort
            rahaa = 7
            koodi = """
kortti = Lunchkort(7)
kortti.at_formanligt()
"""

            kortti = Lunchkort(rahaa)
            kortti.at_formanligt()

            rahaa -= 2.6
            corr = f'Kortets saldo är {rahaa:.1f} euro'
            val = str(kortti)

            self.assertEqual(corr, val, f"Metoden __str__ borde returnera strängen\n{corr}\nvid exekvering av koden\n{koodi}\n" + 
                f"Nu returnerar metoden strängen\n{val}")

            kortti.at_formanligt()
            koodi += "kortti.at_formanligt()\n"
            rahaa -= 2.6
            corr = f'Kortets saldo är {rahaa:.1f} euro'
            val = str(kortti)
            self.assertEqual(corr, val, f"Metoden __str__ borde returnera strängen\n{corr}\nvid exekvering av koden\n{koodi}\n" + 
                f"Nu returnerar metoden strängen\n{val}")
            
            kortti.at_formanligt()
            koodi += "kortti.at_formanligt()\n"
            corr = f'Kortets saldo är {rahaa:.1f} euro'
            val = str(kortti)
            self.assertEqual(corr, val, f"Metoden __str__ borde returnera strängen\n{corr}\nvid exekvering av koden\n{koodi}\n" + 
                f"Nu returnerar metoden strängen\n{val}")

    @points('8.lunchkort_del2')
    def test6_syo_maukkaasti_olemassa(self):
        try:
            from src.lunchkort import Lunchkort 
            koodi = """
kortti = Lunchkort(10)
kortti.at_special()"""

            kortti = Lunchkort(10)
            kortti.at_special()  

        except Exception as e:
            self.assertTrue(False, f'Exekvering av koden\n{koodi}\nåstadkom ett fel\n{e}\nNog är väl metoden at_special(self) definierad?')

    @points('8.lunchkort_del2')
    def test7_syo_maukkaasti(self):
            from src.lunchkort import Lunchkort
            rahaa = 10
            koodi = """
kortti = Lunchkort(10)
kortti.at_special()
"""

            kortti = Lunchkort(rahaa)
            kortti.at_special()

            rahaa -= 4.6
            corr = f'Kortets saldo är {rahaa:.1f} euro'
            val = str(kortti)

            self.assertEqual(corr, val, f"Metoden __str__ borde returnera strängen\n{corr}\nvid exekvering av koden\n{koodi}\n" + 
                f"Nu returnerar metoden strängen\n{val}")

            kortti.at_special()
            koodi += "kortti.at_special()\n"
            rahaa -= 4.6
            corr = f'Kortets saldo är {rahaa:.1f} euro'
            val = str(kortti)
            self.assertEqual(corr, val, f"Metoden __str__ borde returnera strängen\n{corr}\nvid exekvering av koden\n{koodi}\n" + 
                f"Nu returnerar metoden strängen\n{val}")
            
            kortti.at_special()
            koodi += "kortti.at_special()\n"
            corr = f'Kortets saldo är {rahaa:.1f} euro'
            val = str(kortti)
            self.assertEqual(corr, val, f"Metoden __str__ borde returnera strängen\n{corr}\nvid exekvering av koden\n{koodi}\n" + 
                f"Nu returnerar metoden strängen\n{val}")

    @points('8.lunchkort_del3')
    def test8_lataa_rahaa_olemassa(self):
        try:
            from src.lunchkort import Lunchkort 
            koodi = """
kortti = Lunchkort(10)
kortti.tillsatt_pengar(5)"""

            kortti = Lunchkort(10)
            kortti.tillsatt_pengar(5)  

        except Exception as e:
            self.assertTrue(False, f'Exekvering av koden\n{koodi}\nåstadkom ett fel\n{e}\nNog är väl metoden tillsatt_pengar(self, summa: float) definierad?')

    @points('8.lunchkort_del3')
    def test9_lataa_raha(self):
            from src.lunchkort import Lunchkort
            rahaa = 10
            koodi = """
kortti = Lunchkort(10)
kortti.tillsatt_pengar(5)
"""

            kortti = Lunchkort(10)
            kortti.tillsatt_pengar(5)  

            rahaa += 5
            corr = f'Kortets saldo är {rahaa:.1f} euro'
            val = str(kortti)

            self.assertEqual(corr, val, f"Metoden __str__ borde returnera strängen\n{corr}\nvid exekvering av koden\n{koodi}\n" + 
                f"Nu returnerar metoden strängen\n{val}")

            kortti.tillsatt_pengar(75)  
            koodi += "kortti.tillsatt_pengar(75)\n"
            rahaa += 75
            corr = f'Kortets saldo är {rahaa:.1f} euro'
            val = str(kortti)

            self.assertEqual(corr, val, f"Metoden __str__ borde returnera strängen\n{corr}\nvid exekvering av koden\n{koodi}\n" + 
                f"Nu returnerar metoden strängen\n{val}")

            kortti.tillsatt_pengar(20)  
            koodi += "kortti.tillsatt_pengar(20)\n"
            rahaa += 20
            corr = f'Kortets saldo är {rahaa:.1f} euro'
            val = str(kortti)

            self.assertEqual(corr, val, f"Metoden __str__ borde returnera strängen\n{corr}\nvid exekvering av koden\n{koodi}\n" + 
                f"Nu returnerar metoden strängen\n{val}")

    @points('8.lunchkort_del3')
    def test10_lataa_raha_negatiivinen(self):
            from src.lunchkort import Lunchkort
            rahaa = 10
            koodi = """
kortti = Lunchkort(10)
kortti.tillsatt_pengar(-25)
"""

            ok = False
            kortti = Lunchkort(10)
            try:
                kortti.tillsatt_pengar(-25)  
            except ValueError:
                rahaa += 5
                ok = True
                
            self.assertTrue(ok, f"Exekvering av koden\n{koodi}\nborde åstadkomma ValueError")

    @points('8.lunchkort_del4')
    def test11_paaohjelma(self):
        try:
            reload_module(self.module)
            output_all = get_stdout()
        except:
            self.assertTrue(False, f"Granska att programmet kan köras")

        mssage = """\nObservera, att i denna uppgift ska koden INTE BEFINNA SIG innanför
if __name__ == "__main__":
blocket
        """

        self.assertTrue(len(output_all)>0, f"Ditt program skriver inte ut nånting!\n{mssage}")  
        output = [line.strip() for line in output_all.split("\n") if len(line) > 0]

        oikea = [
            "Peter: Kortets saldo är 15.4 euro",
            "Matte: Kortets saldo är 27.4 euro",
            "Peter: Kortets saldo är 35.4 euro",
            "Matte: Kortets saldo är 22.8 euro",
            "Peter: Kortets saldo är 30.2 euro",
            "Matte: Kortets saldo är 72.8 euro"
        ]

        self.assertTrue(len(oikea) == len(output),f"Ditt program ska skriva ut {len(oikea)} rader, det skrev ut {len(output)} rader. Utskriften var\n{output_all}")

        for i in range(0, len(oikea)):
            t = output[i]
            o = oikea[i]
            self.assertTrue(t == o,f"Ditt programs utskrivna rad {i+1} är fel. Den borde vara\n{o}\nDen var däremot\n{t}\nProgrammets hela utskrift var\n{output_all}")               

    @points('8.lunchkort_del4')
    def test12_paaohjelma2(self):

        src_file = os.path.join('src', 'lunchkort.py')
        kielletty = [
            "Peter: Kortets saldo är 15.4 euro",
            "Matte: Kortets saldo är 27.4 euro",
            "Peter: Kortets saldo är 35.4 euro",
            "Matte: Kortets saldo är 22.8 euro",
            "Peter: Kortets saldo är 30.2 euro",
            "Matte: Kortets saldo är 72.8 euro"
        ]        
        with open(src_file) as f:
            for line in f:
                for k in kielletty:
                    if k in line:
                        self.assertTrue(False, f"i uppgiften ska Lunchkort-objekt användas alltså får i din kod inte finnas raderna\n{line}")                

        vaadittu = [
            "= Lunchkort(20)",
            ".at_formanligt()",
            ".at_special()",
            ".tillsatt_pengar(20)"
        ]
        lines = []
        with open(src_file) as f:
            for line in f:
                lines.append(line)
    
        for v in vaadittu:
            on = False
            for line in lines:
                if v in line:
                    on = True              
            self.assertTrue(on, f"i uppgift ska Lunchkort-objekt användas alltså ska i din kod hittas en rad med\n{v}")   

if __name__ == '__main__':
    unittest.main()

   
