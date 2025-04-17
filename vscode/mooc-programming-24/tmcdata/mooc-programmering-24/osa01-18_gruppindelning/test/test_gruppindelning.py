import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, sanitize

exercise = 'src.gruppindelning'

@points('1.gruppindelning')
class OpiskelijatRyhmiinTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = '1'):
            cls.module = load_module(exercise, 'fi')

    def test_A_8_ja_4(self):
        with patch('builtins.input', side_effect = [ '8', '4', AssertionError("Indata frågas för många gånger.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            self.assertFalse(prompt.call_count < 2, 'Programmet ska be om två värden.')
            expected = "Antalet grupper: 2"
            self.assertTrue(len(output)>0, "Programmet skrev inte ut någonting.")
            self.assertTrue(sanitize(expected) in sanitize(output), "Med värdena 8 och 4 borde programmet skriva ut::\n{}\nProgrammet skrev ut\n{}".format(expected, output))
            
    def test_B_11_ja_3(self):
        with patch('builtins.input', side_effect = [ '11', '3', AssertionError("Indata frågas för många gånger.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            expected = "Antalet grupper: 4"
            self.assertTrue(sanitize(expected) in sanitize(output), "Med värdena 11 och 3 borde programmet skriva ut::\n{}\nProgrammet skrev ut\n{}".format(expected, output))

    def test_C_200_ja_99(self):
        with patch('builtins.input', side_effect = [ '200', '99', AssertionError("Indata frågas för många gånger.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            expected = "Antalet grupper: 3"
            self.assertTrue(sanitize(expected) in sanitize(output), "Med värdena 200 och 99 borde programmet skriva ut::\n{}\nProgrammet skrev ut\n{}".format(expected, output))
            
    def test_D_53_ja_11(self):
        with patch('builtins.input', side_effect = [ '53', '11', AssertionError("Indata frågas för många gånger.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            expected = "Antalet grupper: 5"
            self.assertTrue(sanitize(expected) in sanitize(output), "Med värdena 53 och 11 borde programmet skriva ut::\n{}\nProgrammet skrev ut\n{}".format(expected, output))
            
if __name__ == '__main__':
    unittest.main()
