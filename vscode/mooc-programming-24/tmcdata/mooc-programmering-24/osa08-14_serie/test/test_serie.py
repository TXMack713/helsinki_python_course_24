import unittest
from unittest.mock import patch

from tmc import points, reflect
from tmc.utils import load, load_module, reload_module, get_stdout, check_source, sanitize
from functools import reduce
import os
import os.path
import textwrap
from random import choice, randint
from datetime import date, datetime, timedelta

exercise = 'src.serie'
classname = "Serie"

def f(attr: list):
    return ",".join(attr)

class SarjaTest(unittest.TestCase):
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

    @points('8.serie_serie1')
    def test1_luokka_olemassa(self):
        try:
            from src.serie import Serie
        except:
            self.assertTrue(False, "Ditt program bör ha en klass med namnet Serie")

    @points('8.serie_serie1')
    def test2_konstruktori(self):
        try:
            from src.serie import Serie
            sarja = Serie("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
        except Exception as e:
            self.fail('Anropning av klassen Series konstruktor med värdet Serie("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])' +
                f' returnerade ett fel: {e}\nGranska att konstruktorn är definierad korrekt')

    @points('8.serie_serie1')
    def test3_testaa_str(self):
        test_case = ("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
        try:
            from src.serie import Serie
            koodi = f'Serie("{test_case[0]}", {test_case[1]}, {test_case[2]})'
            sarja = Serie(test_case[0], test_case[1], test_case[2])

            genret = ", ".join(test_case[2])
            corr = f'{test_case[0]} ({test_case[1]} säsonger)\ngenrer: {genret}\ninga betygsättningar'
            val = str(sarja)

            self.assertEqual(sanitize(corr), sanitize(val), f"Metoden __str__ borde returnera strängen\n{corr}\ndå objektet anropas\n" + 
                f"{koodi}\nNu returnerar metoden en sträng\n{val}")

        except Exception as e:
            self.assertTrue(False, f'Anropning av metoden __str__ returnerade ett fel: {e}\ndå objektet skapades med anropet\n{koodi}')

    @points('8.serie_serie1')
    def test3_testaa_str2(self):
        test_case = ("South Park", 24, ["Animation", "Comedy"])
        try:
            from src.serie import Serie
            koodi = f'Serie("{test_case[0]}", {test_case[1]}, {test_case[2]})'
            sarja = Serie(test_case[0], test_case[1], test_case[2])

            genret = ", ".join(test_case[2])
            corr = f'{test_case[0]} ({test_case[1]} säsonger)\ngenrer: {genret}\ninga betygsättningar'
            val = str(sarja)

            self.assertEqual(sanitize(corr), sanitize(val), f"Metoden __str__ borde returnera strängen\n{corr}\ndå objektet anropas\n" + 
                f"{koodi}\nNu returnerar metoden en sträng\n{val}")

        except Exception as e:
            self.assertTrue(False, f'Anropning av metoden __str__ returnerade ett fel: {e}\ndå objektet skapades med anropet\n{koodi}')


    @points('8.serie_serie2')
    def test5_arvostele_olemassa(self):
        try:
            from src.serie import Serie
            koodi = """
s = Serie("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
s.betygsatt(5)
"""
     
            s = Serie("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
            s.betygsatt(5)

        except Exception as e:
            self.assertTrue(False, f'Exekvering av koden\n{koodi}\nåstadkom ett fel\n{e}\nNog är väl metoden betygsatt(self, betyg: int) definierad?')

    @points('8.serie_serie2')
    def test5_arvostele(self):
        from src.serie import Serie
        koodi = """
s = Serie("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
s.betygsatt(5)
"""

        test_case = ("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])

        s = Serie("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
        s.betygsatt(5)

        arv = "Betyg 1, medeltal 5.0 poäng"
        
        genret = ", ".join(test_case[2])
        corr = f'{test_case[0]} ({test_case[1]} säsonger)\ngenrer: {genret}\n{arv}'
        val = str(s)

        self.assertTrue(sanitize(corr) == sanitize(val), f"Metoden __str__ borde returnera strängen\n{corr}\ndå objektet anropas\n" + 
            f"{koodi}\nNu returnerar metoden en sträng\n{val}")


        s.betygsatt(3)

        koodi += "s.betygsatt(3)\n"
        arv = "Betyg 2, medeltal 4.0 poäng"

        corr = f'{test_case[0]} ({test_case[1]} säsonger)\ngenrer: {genret}\n{arv}'
        val = str(s)

        self.assertTrue(sanitize(corr) == sanitize(val), f"Metoden __str__ borde returnera strängen\n{corr}\ndå objektet anropas\n" + 
            f"{koodi}\nNu returnerar metoden en sträng\n{val}")

        s.betygsatt(2)

        koodi += "s.betygsatt(2)\n"
        arv = "Betyg 3, medeltal 3.3 poäng"

        corr = f'{test_case[0]} ({test_case[1]} säsonger)\ngenrer: {genret}\n{arv}'
        val = str(s)

        self.assertTrue(sanitize(corr) == sanitize(val), f"Metoden __str__ borde returnera strängen\n{corr}\ndå objektet anropas\n" + 
            f"{koodi}\nNu returnerar metoden en sträng\n{val}")

        s.betygsatt(5)

        koodi += "s.betygsatt(5)\n"
        arv = "Betyg 4, medeltal 3.8 poäng"

        corr = f'{test_case[0]} ({test_case[1]} säsonger)\ngenrer: {genret}\n{arv}'
        val = str(s)

        self.assertTrue(sanitize(corr) == sanitize(val), f"Metoden __str__ borde returnera strängen\n{corr}\ndå objektet anropas\n" + 
            f"{koodi}\nNu returnerar metoden en sträng\n{val}")

    @points('8.serie_serie3')
    def test6_funktio_arvosana_vahintaan_olemassa(self):
        try:
            from src.serie import betyg_minst
        except:
            self.assertTrue(False, "Ditt program bör ha en funktion med namnet betyg_minst(betyg: float, serier: list)")

    @points('8.serie_serie3')
    def test7_funktio_arvosana_vahintaan(self):
        from src.serie import betyg_minst
        from src.serie import Serie

        s1 = Serie("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
        s1.betygsatt(5)

        s2 = Serie("South Park", 24, ["Animation", "Comedy"])
        s2.betygsatt(3)

        s3 = Serie("Friends", 10, ["Romance", "Comedy"])
        s3.betygsatt(2)

        sarjat = [s1, s2, s3]

        koodi = """
s1 = Serie("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
s1.betygsatt(5)
s2 = Serie("South Park", 24, ["Animation", "Comedy"])
s2.betygsatt(3)
s3 = Serie("Friends", 10, ["Romance", "Comedy"])
s3.betygsatt(2)
sarjat = [s1, s2, s3]

vastaus = betyg_minst(4.5, sarjat)
"""
        try:
            vastaus = betyg_minst(4.5, sarjat)
        except:
            self.fail(f"Granska att följande kods exekvering lyckas\n{koodi}")
        
        self.assertTrue(type(vastaus) == list, "Funktionen betyg_minst(betyg: float, serier: list) ska returnera en lista")

        odotettu = 1
        self.assertTrue(len(vastaus)==odotettu, f"Då koden\n{koodi}\nexekveras, borde den returnerade listans längd vara {odotettu}, den var däremot {len(vastaus)}")
        self.assertTrue(vastaus[0].namn=="Dexter", f"Då koden\n{koodi}\nexekveras den returnerade listans enda serie borde ha varit Dexter, den är däremot {vastaus[0].namn}")

        koodi = """
s1 = Serie("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
s1.betygsatt(5)
s2 = Serie("South Park", 24, ["Animation", "Comedy"])
s2.betygsatt(3)
s3 = Serie("Friends", 10, ["Romance", "Comedy"])
s3.betygsatt(2)
sarjat = [s1, s2, s3]

vastaus = betyg_minst(1.5, sarjat)
"""
        try:
            vastaus = betyg_minst(2.5, sarjat)
        except:
            self.fail(f"Granska att följande kods exekvering lyckas\n{koodi}")
        
        self.assertTrue(type(vastaus) == list, "Funktionen betyg_minst(betyg: float, serier: list) ska returnera en lista")

        odotettu = 2
        self.assertTrue(len(vastaus)==odotettu, f"Då koden\n{koodi}\nexekveras, borde den returnerade listans längd vara {odotettu}, den var däremot {len(vastaus)}")
        ehto = (vastaus[0].namn=="Dexter" and vastaus[1].namn=="South Park") or (vastaus[1].namn=="Dexter" and vastaus[0].namn=="South Park")
        self.assertTrue(ehto, f"Då koden\n{koodi}\nexekveras ska den returnerade listan innehålla Dexter och South park, på listan fanns {vastaus[0].namn} ja {vastaus[1].namn}")

    @points('8.serie_serie3')
    def test8_funktio_sisaltaa_genren_olemassa(self):
        try:
            from src.serie import innehallar_genren
        except:
            self.assertTrue(False, "Ditt program bör ha en funktion med namnet innehallar_genren(genre: str, serier: list)")

    @points('8.serie_serie3')
    def test9_funktio_sisaltaa_genret(self):
        from src.serie import innehallar_genren
        from src.serie import Serie

        s1 = Serie("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
        s1.betygsatt(5)

        s2 = Serie("South Park", 24, ["Animation", "Comedy"])
        s2.betygsatt(3)

        s3 = Serie("Friends", 10, ["Romance", "Comedy"])
        s3.betygsatt(2)

        sarjat = [s1, s2, s3]

        koodi = """
s1 = Serie("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
s1.betygsatt(5)
s2 = Serie("South Park", 24, ["Animation", "Comedy"])
s2.betygsatt(3)
s3 = Serie("Friends", 10, ["Romance", "Comedy"])
s3.betygsatt(2)
sarjat = [s1, s2, s3]

vastaus = innehallar_genren("Crime", sarjat)
"""
        try:
            vastaus = innehallar_genren("Crime", sarjat)
        except:
            self.fail(f"Granska att följande kods exekvering lyckas\n{koodi}")

        self.assertTrue(type(vastaus) == list, "Funktion innehallar_genren(genre: str, serier: list) ska returnera en lista")

        odotettu = 1
        self.assertTrue(len(vastaus)==odotettu, f"Då koden\n{koodi}\nexekveras, borde den returnerade listans längd vara {odotettu}, den var däremot {len(vastaus)}")
        self.assertTrue(vastaus[0].namn=="Dexter", f"Då koden\n{koodi}\nexekveras den returnerade listans enda serie borde ha varit Dexter, den är däremot {vastaus[0].namn}")

        koodi = """
s1 = Serie("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
s1.betygsatt(5)
s2 = Serie("South Park", 24, ["Animation", "Comedy"])
s2.betygsatt(3)
s3 = Serie("Friends", 10, ["Romance", "Comedy"])
s3.betygsatt(2)
sarjat = [s1, s2, s3]

vastaus = innehallar_genren("Programming", sarjat)
"""
        try:
            vastaus = innehallar_genren("Programming", sarjat)
        except:
            self.fail(f"Granska att följande kods exekvering lyckas\n{koodi}")


        odotettu = 0
        self.assertTrue(len(vastaus)==odotettu, f"Då koden\n{koodi}\nexekveras, borde den returnerade listans längd vara {odotettu}, den var däremot {len(vastaus)}")

        koodi = """
s1 = Serie("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
s1.betygsatt(5)
s2 = Serie("South Park", 24, ["Animation", "Comedy"])
s2.betygsatt(3)
s3 = Serie("Friends", 10, ["Romance", "Comedy"])
s3.betygsatt(2)
sarjat = [s1, s2, s3]

vastaus = innehallar_genren("Comedy", sarjat)
"""
        try:
            vastaus = innehallar_genren("Comedy", sarjat)
        except:
            self.fail(f"Granska att följande kods exekvering lyckas\n{koodi}")
        
        self.assertTrue(type(vastaus) == list, "Funktionen betyg_minst(betyg: float, serier: list) ska returnera en lista")

        odotettu = 2
        self.assertTrue(len(vastaus)==odotettu, f"Då koden\n{koodi}\nexekveras, borde den returnerade listans längd vara {odotettu}, den var däremot {len(vastaus)}")
        ehto = (vastaus[0].namn=="Friends" and vastaus[1].namn=="South Park") or (vastaus[1].namn=="Friends" and vastaus[0].namn=="South Park")
        self.assertTrue(ehto, f"Då koden\n{koodi}\nexekveras ska den returnerade listan innehålla Friends och South park, på listan fanns {vastaus[0].namn} ja {vastaus[1].namn}")

if __name__ == '__main__':
    unittest.main()
