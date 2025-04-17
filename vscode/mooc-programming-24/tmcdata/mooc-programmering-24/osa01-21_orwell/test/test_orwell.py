import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout

exercise = 'src.orwell'

def parse_result(output):
    if len(output) > 30:
        return output[:30] + "..."
    else:
        return output

@points('1.orwell')
class OrwellTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = '0'):
            cls.module = load_module(exercise, 'fi')

    def test_1984(self):
        with patch('builtins.input', return_value = '1984'):
            reload_module(self.module)
            output = get_stdout()
            self.assertFalse(len(output)==0, "Med värdet 1984 borde programmet skriva ut Orwell\nProgrammet skrev inte ut något")
            self.assertTrue('Orwell' in output, "Med värdet 1984 borde programmet skriva ut Orwell\nProgrammet skrev ut\n" + output )

    def test_lisatestit(self):
        testset = ['2020', '1983', '1985']
        for vuosi in testset:
            with patch('builtins.input', return_value = vuosi):
                reload_module(self.module)
                output = get_stdout()
                self.assertFalse(len(output)>0, f"Med värdet {vuosi} borde programmet inte skriva ut något, det skrev ändå ut\n"+ output)

if __name__ == '__main__':
    unittest.main()
