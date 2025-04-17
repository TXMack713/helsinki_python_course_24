import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce

exercise = 'src.storleksklass'

@points('1.storleksklass')
class LuvunSuuruusluokkaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = '0'):
            cls.module = load_module(exercise, 'fi')

    def test_tulostus_1(self):
        luku = 9
        with patch('builtins.input', return_value = str(luku)):
            reload_module(self.module)
            output = get_stdout().split("\n")
            if luku < 1000:
                self.assertEqual(output[0].strip(), "Siffran är mindre än 1000", "Programmet skrev inte ut\nSiffran är mindre än 1000\nFör talet " + str(luku))
            if luku < 100:
                self.assertTrue(len(output)>1, "Programmet skrev inte ut\nSiffran är mindre än 100\nFör talet " + str(luku))
                self.assertEqual(output[1].strip(), "Siffran är mindre än 100", "Programmet skrev inte ut\nSiffran är mindre än 100\nFör talet " + str(luku))
            if luku < 10:
                self.assertTrue(len(output)>2, "Programmet skrev inte ut\nSiffran är mindre än 10\nFör talet " + str(luku))
                self.assertEqual(output[2].strip(), "Siffran är mindre än 10", "Programmet skrev inte ut\nSiffran är mindre än 10\nFör talet " + str(luku))
            self.assertEqual(output[-1], "Tackar!", "Programmet skrev inte ut raden 'Tackar!' till sist")

    def test_tulostus_2(self):
        luku = 97
        with patch('builtins.input', return_value = str(luku)):
            reload_module(self.module)
            output = get_stdout().split("\n")
            if luku < 1000:
                self.assertEqual(output[0], "Siffran är mindre än 1000", "Programmet skrev inte ut, että Siffran är mindre än 1000 För talet " + str(luku))
            if luku < 100:
                self.assertTrue(len(output)>1, "Programmet skrev inte ut\nSiffran är mindre än 100\nFör talet " + str(luku))
                self.assertEqual(output[1], "Siffran är mindre än 100", "Programmet skrev inte ut, että Siffran är mindre än 100 För talet " + str(luku))
            if luku < 10:
                self.assertTrue(len(output)>2, "Programmet skrev inte ut\nSiffran är mindre än 10\nFör talet " + str(luku))
                self.assertEqual(output[2], "Siffran är mindre än 10", "Programmet skrev inte ut, että Siffran är mindre än 10 För talet " + str(luku))
            self.assertEqual(output[-1], "Tackar!", "Programmet skrev inte ut raden 'Tackar!' till sist")

    def test_tulostus_3(self):
        luku = 451
        with patch('builtins.input', return_value = str(luku)):
            reload_module(self.module)
            output = get_stdout().split("\n")
            if luku < 1000:
                self.assertEqual(output[0], "Siffran är mindre än 1000", "Programmet skrev inte ut, että Siffran är mindre än 1000 För talet " + str(luku))
            if luku < 100:
                self.assertTrue(len(output)>1, "Programmet skrev inte ut\nSiffran är mindre än 100\nFör talet " + str(luku))
                self.assertEqual(output[1], "Siffran är mindre än 100", "Programmet skrev inte ut, että Siffran är mindre än 100 För talet " + str(luku))
            if luku < 10:
                self.assertTrue(len(output)>2, "Programmet skrev inte ut\nSiffran är mindre än 10\nFör talet " + str(luku))
                self.assertEqual(output[2], "Siffran är mindre än 10", "Programmet skrev inte ut, että Siffran är mindre än 10 För talet " + str(luku))
            self.assertEqual(output[-1], "Tackar!", "Programmet skrev inte ut raden 'Tackar!' till sist")

    def test_tulostus_4(self):
        luku = 111234
        with patch('builtins.input', return_value = str(luku)):
            reload_module(self.module)
            output = get_stdout().split("\n")
            if luku < 1000:
                self.assertEqual(output[0], "Siffran är mindre än 1000", "Programmet skrev inte ut, että Siffran är mindre än 1000 För talet " + str(luku))
            if luku < 100:
                self.assertTrue(len(output)>1, "Programmet skrev inte ut\nSiffran är mindre än 100\nFör talet " + str(luku))
                self.assertEqual(output[1], "Siffran är mindre än 100", "Programmet skrev inte ut, että Siffran är mindre än 100 För talet " + str(luku))
            if luku < 10:
                self.assertTrue(len(output)>2, "Programmet skrev inte ut\nSiffran är mindre än 10\nFör talet " + str(luku))
                self.assertEqual(output[2], "Siffran är mindre än 10", "Programmet skrev inte ut, että Siffran är mindre än 10 För talet " + str(luku))
            self.assertEqual(output[-1], "Tackar!", "Programmet skrev inte ut raden 'Tackar!' till sist")

if __name__ == '__main__':
    unittest.main()
