import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout

exercise = 'src.absolutbelopp'

def parse_result(output):
    if len(output) > 30:
        return output[:30] + "..."
    else:
        return output

@points('1.absolutbelopp')
class ItseisarvoTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = '0'):
            cls.module = load_module(exercise, 'fi')

    def test_1_miinus_8(self):
        with patch('builtins.input', return_value = '-8'):
            reload_module(self.module)
            output = get_stdout()
            self.assertTrue('Talets absolutbelopp är 8' in output, "Med värdet -8 borde programmet skriva ut\nTalets absolutbelopp är 8\nProgrammet skrev ut\n"+ output)

    def test_2_plus_2(self):
        with patch('builtins.input', return_value = '2'):
            reload_module(self.module)
            output = get_stdout()
            self.assertTrue('Talets absolutbelopp är 2' in output, "Med värdet 2 borde programmet skriva ut\nTalets absolutbelopp är 2\nProgrammet skrev ut\n"+ output)

    def test_3_lisatestit(self):
        testset = ['-99', '4', '435634', '-234', '6', '0']
        for luku in testset:
            with patch('builtins.input', return_value = luku):
                reload_module(self.module)
                result = luku[1:-1] if int(luku)<0 else luku
                if int(luku) >= 0:
                    self.assertTrue(f'-{luku}' not in get_stdout(), 'Programmet fungerar fel med värdet ' + luku + '. Svaret borde vara ' + result)
                self.assertTrue(result in get_stdout(), 'Programmet fungerar fel med värdet ' + luku + '. Svaret borde vara ' + result)

if __name__ == '__main__':
    unittest.main()
