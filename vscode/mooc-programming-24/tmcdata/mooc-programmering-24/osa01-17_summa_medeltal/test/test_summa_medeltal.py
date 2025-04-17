import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, sanitize

exercise = 'src.summa_medeltal'

@points('1.summa_medeltal')
class SummaJaKeskiarvoTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = '0'):
            cls.module = load_module(exercise, 'fi')

    def test_1234(self):
        with patch('builtins.input', side_effect = [ '1', '2', '3', '4', AssertionError("Indata frågas för många gånger.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            self.assertFalse(prompt.call_count < 2, 'Programmet borde be om fyra värden.')
            self.assertTrue(len(output)>0, 'Programmet skrev inte ut någonting.' )
            self.assertTrue('10' in output, 'Programmet skriver inte ut summan av 1, 2, 3 och 4 korrekt. Förväntade: 10'+ '\nProgrammet skrev ut\n'+ str(output))
            self.assertTrue('2.5' in output, 'Programmet skriver inte ut medeltalet av 1, 2, 3 och 4 korrekt. Förväntade: 2.5'+ '\nProgrammet skrev ut\n'+ str(output))
            expected = "Summan av talen är 10 och medeltalet är 2.5"
            self.assertTrue(sanitize(expected) in sanitize(output), "Med värdena 1, 2, 3 och 4 borde programmet skriva ut\n{}\nProgrammet skrev ut\n{}".format(expected, output))
            

    def test_lisatestit(self):
        testset = [
            [ '3', '7', '2', '8' ],
            [ '8', '-22', '75', '5' ],
            [ '0', '0', '0', '0' ],
        ]
        for a, b, c, d in testset:
            with patch('builtins.input', side_effect = [ a, b, c, d, AssertionError("Indata frågas för många gånger.") ]) as prompt:
                reload_module(self.module)
                output = get_stdout()
                summ =  int(a) + int(b) + int(c) + int(d)
                avg = summ / 4
                inputs = f"{a}, {b}, {c} ja {d}"
                self.assertTrue(str(summ) in output, 'Med värdena {} räknas summan fel, förväntade: {}'.format(inputs, summ))
                self.assertTrue(str(avg) in output, 'Med värdena {} räknas medeltalet fel, förväntade: {}'.format(inputs, avg))
                expected = f"Summan av talen är {summ} och medeltalet är {avg}"
                self.assertTrue(sanitize(expected) in sanitize(output), "Med värdena {} borde programmet skriva ut\n{}".format(inputs, expected))

if __name__ == '__main__':
    unittest.main()
