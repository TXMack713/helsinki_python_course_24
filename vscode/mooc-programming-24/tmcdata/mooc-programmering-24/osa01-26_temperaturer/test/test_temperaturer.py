import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, sanitize, remove_extra_whitespace
from functools import reduce
from random import randint

exercise = 'src.temperaturer'

def close(a, b):
    return abs(a-b) < 0.001

@points('1.temperaturer')
class LampotilatTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = '0'):
            cls.module = load_module(exercise, 'fi')

    def test_1_nolla(self):
        test_input = 32
        correct = (test_input - 32) * 5/9
        with patch('builtins.input', return_value = str(test_input)):
            reload_module(self.module)
            output = get_stdout().split("\n")

            self.assertFalse(output[-1].find("Kallt") > -1, "Programmet skriver ut 'Kallt!' även om temperaturen mätt i Celcius är över noll.")
            self.assertEqual(len(output), 1, "Programmet skrev ut fler än en rad med indatat 32")
            out = output[0]
            e = "32 grader Fahrenheit är 0.0 grader Celcius" 
            e2= "32.0 grader Fahrenheit är 0.0 grader Celcius"
            self.assertTrue(sanitize(out) == sanitize(e) or sanitize(out) == sanitize(e2), f"Programmet borde skriva ut\n{e}med indatat {32},\nmen utskriften blir \n{out}")
            tulos = float(remove_extra_whitespace(out).split(' ')[-3])
            self.assertTrue(close(tulos, 0.0), "Programmet konverterade inte temperaturen rätt: resultatet borde vara 0.0 men programmet skriver ut " + output[0])

    def test_2_positiivinen(self):
        test_input = randint(33, 105)
        correct = (test_input - 32) * 5/9
        with patch('builtins.input', return_value = str(test_input)):
            reload_module(self.module)
            output = get_stdout().split("\n")
            self.assertFalse(output[-1].find("Kallt") > -1, "Programmet skriver ut 'Kallt!' även om temperaturen mätt i Celcius är över noll. Varmista että näin ei tapahdu syötteellä {test_input}")
            self.assertEqual(len(output), 1, "Programmet skrev ut fler än en rad")
            out = output[0]
            tulos = float(remove_extra_whitespace(out).split(' ')[-3])
            self.assertTrue(close(tulos, correct), "Programmet konverterade inte temperaturen rätt: resultatet för värdet {} borde vara {}, men programmet skriver ut {}".format(test_input, correct, output[0]))

    def test_3_negatiivinen(self):
        test_input = randint(-50, 31)
        correct = (test_input - 32) * 5/9
        with patch('builtins.input', return_value = str(test_input)):
            reload_module(self.module)
            output = get_stdout().split("\n")
            out = output[0]
            tulos = float(remove_extra_whitespace(out).split(' ')[-3])
            self.assertTrue(close(tulos, correct), "Programmet konverterade inte temperaturen rätt: resultatet för värdet {} borde vara {}, men programmet skriver ut {}".format(test_input, correct, output[0]))
            self.assertTrue(len(output)>1, f"Programmet skrev inte ut texten 'Kallt!' även om temperaturen mätt i Celcius är under noll. Säkerställ att detta sker med värdet {test_input}")
            self.assertTrue(output[1].find("Kallt") > -1, f"Programmet skrev inte ut texten 'Kallt!' även om temperaturen mätt i Celcius är under noll. Säkerställ att detta sker med värdet {test_input}")
   
if __name__ == '__main__':
    unittest.main()
