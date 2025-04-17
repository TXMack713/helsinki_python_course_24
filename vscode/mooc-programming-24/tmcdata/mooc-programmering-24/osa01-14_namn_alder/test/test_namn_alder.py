import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, assert_ignore_ws

exercise = 'src.namn_alder'

def parse_result(output):
    if len(output) > 30:
        return output[:30] + "..."
    else:
        return output

@points('1.namn_alder')
class NimiJaIkaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = '0'):
            cls.module = load_module(exercise, 'fi')

    def test_keijo_keksitty(self):
        with patch('builtins.input', side_effect = [ 'Sandro Syntetisk', '1990', AssertionError("Indata frågas för många gånger.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            self.assertTrue(len(output)>0, 'Programmet skrev inte ut någonting.' )
            e = 'Hej Sandro Syntetisk, du är 30 år i slutet av 2020'
            assert_ignore_ws(self, output, e, "När indatat är Sandro Syntetisk 1990\n")

    def test_muita_nimia1(self):
        testset = [
            ['Pekka Python', '2019', '1'],
        ]
        for nimi, syntvuosi, ika in testset:
            with patch('builtins.input', side_effect = [nimi, syntvuosi]):
                reload_module(self.module)
                output = get_stdout()
                e = f"Hej {nimi}, du är {ika} år i slutet av 2020"
                assert_ignore_ws(self, output, e, f"När indatat är {nimi} {syntvuosi}\n")

    def test_muita_nimia2(self):
        testset = [
            ['Angela Merkel', '1954', '66'],
        ]
        for nimi, syntvuosi, ika in testset:
            with patch('builtins.input', side_effect = [nimi, syntvuosi]):
                reload_module(self.module)
                output = get_stdout()
                e = f"Hej {nimi}, du är {ika} år i slutet av 2020"
                assert_ignore_ws(self, output, e, f"När indatat är {nimi} {syntvuosi}\n")


    def test_muita_nimia3(self):
        testset = [
            ['Venla Ruuska', '2013', '7'],
        ]
        for nimi, syntvuosi, ika in testset:
            with patch('builtins.input', side_effect = [nimi, syntvuosi]):
                reload_module(self.module)
                output = get_stdout()
                e = f"Hej {nimi}, du är {ika} år i slutet av 2020"
                assert_ignore_ws(self, output, e, f"När indatat är {nimi} {syntvuosi}\n")


if __name__ == '__main__':
    unittest.main()
