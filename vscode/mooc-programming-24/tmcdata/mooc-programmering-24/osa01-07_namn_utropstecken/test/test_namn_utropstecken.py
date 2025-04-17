import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, assert_ignore_ws

exercise = 'src.namn_utropstecken'

@points('1.namn_utropstecken')
class NimiJaHuutomerkkiTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = ''):
            cls.module = load_module(exercise, 'fi')

    def test_syotteen_tulostus_1(self):
        with patch('builtins.input', return_value = 'Sandrine'):
            reload_module(self.module)
            output = get_stdout()
            self.assertTrue(len(output)>0, "Programmet skriver inte ut något.")
            assert_ignore_ws(self, output, '!Sandrine!Sandrine!', 'Programmet fungerar inte korrekt med den givna strängen: Sandrine\n' )

    def test_syotteen_tulostus_2(self):
        with patch('builtins.input', return_value = 'Ada'):
            reload_module(self.module)
            output = get_stdout()
            assert_ignore_ws(self,output, '!Ada!Ada!', 'Programmet fungerar inte korrekt med den givna strängen: Ada\n' )

    def test_syotetta_kysytaan_tasmalleen_kerran(self):
        with patch('builtins.input', return_value = '') as prompt:
            reload_module(self.module)
            output = get_stdout()
            try:
                prompt.assert_called_once()
            except AssertionError:
                self.fail('Användaren ska bes ge data bara en gång.')

if __name__ == '__main__':
    unittest.main()
