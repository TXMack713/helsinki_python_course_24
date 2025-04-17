import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, sanitize

exercise = 'src.summa_produkt'

@points('1.summa_produkt')
class TuloJaSummaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = '0'):
            cls.module = load_module(exercise, 'fi')

    def test_kolme_ja_seitseman(self):
        with patch('builtins.input', side_effect = [ '3', '7', AssertionError("Indata frågas för många gånger.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            self.assertFalse(prompt.call_count < 2, 'Programmet ska be om två värden.')
            self.assertTrue(len(output)>0, 'Programmet skrev inte ut någonting.' )
            self.assertTrue('10' in output, 'Programmet skriver inte ut summan av 3 och 7 korrekt. Förväntade: 10'+ '\nUtskriften var\n'+ str(output))
            self.assertTrue('21' in output, 'Programmet skriver inte ut produkten av 3 och 7 korrekt. Förväntade: 21'+ '\nUtskriften var\n'+ str(output))
            expected = f"Talens summa 10"

            self.assertTrue(sanitize(expected) in sanitize(output), "Med värdena 3 och 7 borde programmet innehålla raden\n{}\nUtskriften var\n{}".format(expected, output))
            expected = f"Produkten av talen 21"
            self.assertTrue(sanitize(expected) in sanitize(output), "Med värdena 3 och 7 borde programmet innehålla raden\n{}\nUtskriften var\n{}".format(expected, output))
            
    def test_lisatestit(self):
        testset = [
            ['0', '0'],
            ['0', '1'],
            ['13', '4'],
            ['7', '191'],
            ['716', '28213']
        ]
        for a, b in testset:
            with patch('builtins.input', side_effect = [ a, b, AssertionError("Indata frågas för många gånger.") ]) as prompt:
                reload_module(self.module)
                output = get_stdout()
                summ =  int(a) + int(b) 
                prod = int(a) * int(b) 
                inputs = f"{a} ja {b}"
                self.assertTrue(str(summ) in output, 'Med värdena {} beräknas summan fel, förväntade: {}'.format(inputs, summ))
                self.assertTrue(str(prod) in output, 'Med värdena {} beräknas produkten fel, förväntade: {}'.format(inputs, prod))
                expected = f"Talens summa {summ}"
                self.assertTrue(sanitize(expected) in sanitize(output), "Med värdena {} borde programmet skriva ut: {}".format(inputs, expected))
                expected = f"Produkten av talen {prod}"
                self.assertTrue(sanitize(expected) in sanitize(output), "Med värdena {} borde programmet skriva ut: {}".format(inputs, expected))

if __name__ == '__main__':
    unittest.main()
