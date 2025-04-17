import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, sanitize

exercise = 'src.matkostnader'

@points('1.matkostnader')
class RuokailuTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = '0'):
            cls.module = load_module(exercise, 'fi')

    def test_0(self):
        with patch('builtins.input', side_effect = [ '4', '2.5', '21.5', AssertionError("Indata frågas för många gånger.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
             
            self.assertTrue(len(output)>0, 'Programmet skrev inte ut någonting.' )
            self.assertFalse(prompt.call_count < 2, 'Programmet ska be om tre värden.')
            expected = "Under en dag 4.5 euro"
            self.assertTrue(sanitize(expected) in sanitize(output), f"Med värdena 4, 2.5 och 21.5 borde programmet skriva ut\n{expected}\nProgrammet skrev ut\n{output}")
            expected = "Under en vecka 31.5 euro"
            self.assertTrue(sanitize(expected) in sanitize(output), f"Med värdena 4, 2.5 och 21.5 borde programmet skriva ut\n{expected}\nProgrammet skrev ut\n{output}")
            
    def test_1(self):
        with patch('builtins.input', side_effect = [ '4', '2.5', '21.5', AssertionError("Indata frågas för många gånger.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            
            self.assertFalse(prompt.call_count < 2, 'Programmet ska be om tre värden.')
            expected = "Under en dag 4.5 euro"
            self.assertTrue(sanitize(expected) in sanitize(output), f"Med värdena 4, 2.5 och 21.5 borde programmet skriva ut\n{expected}\nProgrammet skrev ut\n{output}")
            expected = "Under en vecka 31.5 euro"
            self.assertTrue(sanitize(expected) in sanitize(output), f"Med värdena 4, 2.5 och 21.5 borde programmet skriva ut\n{expected}\nProgrammet skrev ut\n{output}")
                        
    def test_2_lisatestit(self):
        testset = [
            [ '5', '3.5', '43.75', '8.75', '61.25'], 
            [ '1', '2.25', '15.25', '2.5', '17.5' ],
            [ '0', '0', '0', '0.0', '0.0' ],
        ]
        for a, b, c, d, w in testset:
            with patch('builtins.input', side_effect = [ a, b, c, AssertionError("Indata frågas för många gånger.") ]) as prompt:
                reload_module(self.module)
                output = get_stdout()
                inputs = f"{a}, {b}, ja {c}"
                self.assertFalse(prompt.call_count < 3, 'Programmet ska be om tre värden.')
                expected = f"Under en dag {d} euro"
                self.assertTrue(sanitize(expected) in sanitize(output), f"Med värdena {inputs} borde programmet skriva ut\n{expected}\nProgrammet skrev ut\n{output}")
                expected = f"Under en vecka {w} euro"
                self.assertTrue(sanitize(expected) in sanitize(output), f"Med värdena {inputs} borde programmet skriva ut\n{expected}\nProgrammet skrev ut\n{output}")    

if __name__ == '__main__':
    unittest.main()
