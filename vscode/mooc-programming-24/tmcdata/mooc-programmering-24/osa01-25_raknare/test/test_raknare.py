import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, sanitize

exercise = 'src.raknare'

def parse_result(output):
    if len(output) > 30:
        return output[:30] + "..."
    else:
        return output

@points('1.raknare')
class LaskinTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = '0'):
            cls.module = load_module(exercise, 'fi')

    def test_summa1(self):
        with patch('builtins.input', side_effect = [ '1', '2', 'summa', AssertionError("Indata frågas för många gånger.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            expect = '1 + 2 = 3'
            self.assertTrue(len(output)>0, "Programmet skrev inte ut någonting. Indata 1, 2, summa")
            self.assertTrue(expect in output, f"Med värdena 1, 2, summa borde programmet ha skrivit ut\n{expect}\nProgrammet skrev ut:\n{output}")

    def test_summa2(self):
        with patch('builtins.input', side_effect = [ '75', '23', 'summa', AssertionError("Indata frågas för många gånger.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            self.assertTrue(len(output)>0, "Programmet skrev inte ut någonting. Indata 75, 23, summa")
            expect = '75 + 23 = 98'
            self.assertTrue(expect in output, f"Med värdena 75, 23, summa borde programmet ha skrivit ut\n{expect}\nProgrammet skrev ut:\n{output}")

    def test_erotus1(self):
        with patch('builtins.input', side_effect = [ '2', '1', 'differens', AssertionError("Indata frågas för många gånger.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            self.assertTrue(len(output)>0, "Programmet skrev inte ut någonting. Indata 2, 1, differens")
            expect = '2 - 1 = 1'
            self.assertTrue(expect in output, f"Med värdena 2, 1, differens borde programmet ha skrivit ut\n{expect}\nProgrammet skrev ut:\n{output}")

    def test_erotus2(self):
        with patch('builtins.input', side_effect = [ '13', '34', 'differens', AssertionError("Indata frågas för många gånger.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            expect = '13 - 34 = -21'
            self.assertTrue(expect in output, f"Med värdena 13, 34, differens borde programmet ha skrivit ut\n{expect}\nProgrammet skrev ut:\n{output}")

    def test_tulo1(self):
        with patch('builtins.input', side_effect = [ '2', '3', 'produkt', AssertionError("Indata frågas för många gånger.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            expect = '2 * 3 = 6'
            self.assertTrue(len(output)>0, "Programmet skrev inte ut någonting. Indata 2, 3, produkt")
            self.assertTrue(expect in output, f"Med värdena 2, 3, produkt borde programmet ha skrivit ut\n{expect}\nProgrammet skrev ut:\n{output}")
   
    def test_tulo2(self):
        with patch('builtins.input', side_effect = [ '27', '-3', 'produkt', AssertionError("Indata frågas för många gånger.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            expect = '27 * -3 = -81'
            self.assertTrue(expect in output, f"Med värdena 27, -3, produkt borde programmet ha skrivit ut\n{expect}\nProgrammet skrev ut:\n{output}")

    def test_xcrap(self):
        with patch('builtins.input', side_effect = [ '27', '-3', 'kvot', AssertionError("Indata frågas för många gånger.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            self.assertTrue(len(output) == 0, f"Med värdena 27, -3, kvot borde programmet inte ha skrivit ut något\nProgrammet skrev ut:\n{output}")

if __name__ == '__main__':
    unittest.main()
