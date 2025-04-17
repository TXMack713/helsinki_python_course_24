import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, assert_ignore_ws

exercise = 'src.x_ganger_fem'

@points('1.x_ganger_fem')
class KerrottunaViidellaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = '0'):
            cls.module = load_module(exercise, 'fi')

    def test_kerrottuna_kolmella(self):
        with patch('builtins.input', return_value = '3'):
            reload_module(self.module)
            output = get_stdout()
            self.assertTrue(len(output)>0, 'Programmet skrev inte ut någonting.' )
            self.assertTrue('15' in output, 'Fel utskrift med indatat 3, programmet skriver ut\n' + output)
            expected = '3 * 5 = 15'
            assert_ignore_ws(self, output, expected,  'Inkorrekt utskrift med värdet 3, ')

    def test_kerrottuna_viidella(self):
        with patch('builtins.input', return_value = '5'):
            reload_module(self.module)
            output = get_stdout()
            expected = '5 * 5 = 25'
            assert_ignore_ws(self, output, expected,  'Inkorrekt utskrift med värdet 5, ')

    def test_kerrottuna_sadalla(self):
        with patch('builtins.input', return_value = '100'):
            reload_module(self.module)
            output = get_stdout()
            expected = '100 * 5 = 500'
            assert_ignore_ws(self, output, expected,  'Inkorrekt utskrift med värdet 100, ')

    def test_lukua_kysytaan_tasmalleen_kerran(self):
        with patch('builtins.input', return_value = '0') as prompt:
            reload_module(self.module)
            output = get_stdout()
            try:
                prompt.assert_called_once()
            except AssertionError:
                self.fail('Användaren ska bes ge data bara en gång.')

if __name__ == '__main__':
    unittest.main()
