import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout

exercise = 'src.namn_tva_ganger'

@points('1.namn_tva_ganger')
class NimiKahdestiTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = ''):
            cls.module = load_module(exercise, 'fi')

    def test_syotteen_tulostus_1(self):
        with patch('builtins.input', return_value = 'Pauline'):
            reload_module(self.module)
            output = get_stdout()
            self.assertTrue(len(output)>0, "Programmet skriver inte ut något.")
            splitted = output.split('\n')
            self.assertTrue(splitted[0].rstrip() == 'Pauline' and splitted[1].rstrip() == 'Pauline', f'Programmet fungerade inte korrekt med den angivna strängen: Pauline. Du skrev ut\n{output}\nUtskriften borde ha varit\nPauline\nPauline')

    def test_syotteen_tulostus_2(self):
        with patch('builtins.input', return_value = 'Ada'):
            reload_module(self.module)
            output = get_stdout()
            splitted = output.split('\n')
            self.assertTrue(splitted[0].rstrip() == 'Ada' and splitted[1].rstrip() == 'Ada', f'Programmet fungerade inte korrekt med den angivna strängen: Ada. Du skrev ut\n{output}\nUtskriften borde ha varit\nAda\nAda')


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
