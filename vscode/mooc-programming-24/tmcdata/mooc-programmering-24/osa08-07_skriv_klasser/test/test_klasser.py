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

exercise = 'src.skriv_klasser'

def f(attr: list):
    return ",".join(attr)

@points('8.skriv_klasser')
class LuokatTest(unittest.TestCase):
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

    def test1_luokat_olemassa(self):
        try:
            from src.skriv_klasser import Minneslista
        except:
            self.fail("Ditt program bör ha en klass med namnet Minneslista")

        try:
            from src.skriv_klasser import Kund
        except:
            self.fail("Ditt program bör ha en klass med namnet Kund")

        try:
            from src.skriv_klasser import Kabel
        except:
            self.fail("Ditt program bör ha en klass med namnet Kabel")

    def test2_konstruktorit(self):
        try:
            from src.skriv_klasser import Minneslista
            val = Minneslista("lista", [])
        except Exception as e:
            self.assertTrue(False, 'Anrop av klassen Minneslistas konstruktor med värdet Minneslista("lista", [])' +
                f' returnerade ett fel: {e}')
        try:
            from src.skriv_klasser import Kund
            val = Kund("asiakas",1,1.0)
        except Exception as e:
            self.assertTrue(False, 'Anrop av klassen Kunds konstruktor med värdet Kund("asiakas",1,1.0)' +
                f' returnerade ett fel: {e}')

        try:
            from src.skriv_klasser import Kabel
            val = Kabel("kaapeli",1.0,1,True)
        except Exception as e:
            self.assertTrue(False, 'Anrop av klassen Kabels konstruktor med värdet Kabel("kaapeli",1.0,1.True)' +
                f' returnerade ett fel: {e}')

    
    def test3_testaa_attribuutit(self):
        with patch('builtins.input', side_effect=[AssertionError("Förväntade inte att värden frågas av användaren")]):
            reload_module(self.module)
            from src.skriv_klasser import Minneslista, Kund, Kabel

            attributes = ("rubrik","inlagg")
            for attr in attributes:
                ref = reflect.Reflect()
                ref.set_object(Minneslista("lista",[]))

                self.assertTrue(ref.has_attribute(attr), f"Det returnerade objekten bör ha attributet {attr}," +  
                    f'\nnu är attributen\n{f(ref.list_attributes(True))}\nnär konstruktorn anropas med argumenten' + 
                    f'Muistilista("lista",[])')

            attributes = ("id", "saldo", "rabatt")
            for attr in attributes:
                ref = reflect.Reflect()
                ref.set_object(Kund("asiakas", 1.0, 1))

                self.assertTrue(ref.has_attribute(attr), f"Det returnerade objekten bör ha attributet {attr}," +  
                    f'\nnu är attributen\n{f(ref.list_attributes(True))}\nnär konstruktorn anropas med argumenten' + 
                    f'Asiakas("asiakas", 1.0, 1)')

            attributes = ("modell", "langd", "maximal_hastighet", "dubbelriktad")
            for attr in attributes:
                ref = reflect.Reflect()
                ref.set_object(Kabel("kaapeli",1.0,1,True))

                self.assertTrue(ref.has_attribute(attr), f"Det returnerade objekten bör ha attributet {attr}," +  
                    f'\nnu är attributen\n{f(ref.list_attributes(True))}\nnär konstruktorn anropas med argumenten' + 
                    f'Kaapeli("kaapeli",1.0,1,True)')

    
    def test4_testaa_muistikirja(self):
         test_cases = [("Laskut", ["Muista vuokra", "Muista puhelinlasku"]), 
                       ("Kauppalista", ["Maito", "Leipä", "Mehu", "Viili"])]
         
         for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Förväntade inte att värden frågas av användaren")]):
                reload_module(self.module)
                from src.skriv_klasser import Minneslista

                lista = Minneslista(test_case[0], test_case[1])
                
                attributes = ("rubrik", "inlagg")
                ref = reflect.Reflect()
                ref.set_object(lista)

                for i in range(len(attributes)):
                    value = ref.get_attribute(attributes[i])
                    self.assertEqual(value, test_case[i], 
                        f'Värdet på attributen {attributes[i]} borde vara {test_case[i]}, nu är de {value},\n då argumenten är \n{test_case}')

    def test5_testaa_asiakas(self):
         test_cases = [("Arto Asiakas", 1424.50, 10), ("Anne Asiakas", 550.0, 7), ("Aune Asiakas", 240.25, 15)]
         
         for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Förväntade inte att värden frågas av användaren")]):
                reload_module(self.module)
                from src.skriv_klasser import Kund

                asiakas = Kund(test_case[0], test_case[1], test_case[2])
                
                attributes = ("id", "saldo", "rabatt")
                ref = reflect.Reflect()
                ref.set_object(asiakas)

                for i in range(len(attributes)):
                    value = ref.get_attribute(attributes[i])
                    self.assertEqual(value, test_case[i], 
                        f'Värdet på attributen {attributes[i]} borde vara {test_case[i]}, nu är de {value},\n då argumenten är \n{test_case}')

    def test6_testaa_kaapeli(self):
         test_cases = [("cat", 5.0, 128, True), ("USB2", 10.0, 24, True), ("BSU3", 25.0, 18, False)]
         
         for test_case in test_cases:
            with patch('builtins.input', side_effect=[AssertionError("Förväntade inte att värden frågas av användaren")]):
                reload_module(self.module)
                from src.skriv_klasser import Kabel

                kaapeli = Kabel(test_case[0], test_case[1], test_case[2], test_case[3])
                
                attributes = ("modell", "langd", "maximal_hastighet", "dubbelriktad")
                ref = reflect.Reflect()
                ref.set_object(kaapeli)

                for i in range(len(attributes)):
                    value = ref.get_attribute(attributes[i])
                    self.assertEqual(value, test_case[i], 
                        f'Värdet på attributen {attributes[i]} borde vara {test_case[i]}, nu är de {value},\n då argumenten är \n{test_case}')


if __name__ == '__main__':
    unittest.main()
