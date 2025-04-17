import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout

exercise = 'src.soppa'

def parse_result(output):
    if len(output) > 30:
        return output[:30] + "..."
    else:
        return output

def oikea_jarjestys(output):
    parts = output.split("\n")
    hinta = False
    for part in parts:
        if 'Slutsumma' in part:
            hinta = True
        if "Nästa!" == part and not hinta:
            return False

    return True  

@points('1.soppa')
class KeittoaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = '0'):
            cls.module = load_module(exercise, 'fi')

    def test_1_kramer_1(self):
        with patch('builtins.input', side_effect = [ 'Kramer', '1', AssertionError("Indata frågas för många gånger.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout().rstrip()
            expected = "Nästa!"
            self.assertTrue(len(output)>0, f"Programmet skrev inte ut någonting.")
            self.assertTrue(expected in output, f"Med värdena Kramer, 1 borde programmet skriva ut\n{expected}\nProgrammet skrev ut\n"+ output)
            expected = 'Slutsumma 5.9'
            self.assertTrue(expected in output, f"Med värdena Kramer, 1 borde programmet skriva ut\n{expected}\nProgrammet skrev ut\n"+ output)
            self.assertTrue(oikea_jarjestys(output), f"Med värdena Kramer, 1 borde programmet skriva ut\n'Nästa' först efter att priset meddelats\nProgrammet skrev ut\n"+ output)

    def test_2_kramer_4(self):
        with patch('builtins.input', side_effect = [ 'Kramer', '4', AssertionError("Indata frågas för många gånger.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout().rstrip()
            expected = "Nästa!"
            self.assertTrue(expected in output, f"Med värdena Kramer, 4 borde programmet skriva ut\n{expected}\nProgrammet skrev ut\n"+ output)
            expected = 'Slutsumma 23.6'
            self.assertTrue(expected in output, f"Med värdena Kramer, 4 borde programmet skriva ut\n{expected}\nProgrammet skrev ut\n"+ output)
            self.assertTrue(oikea_jarjestys(output), f"Med värdena Kramer, 4 borde programmet skriva ut\n'Nästa' först efter att priset meddelats\nProgrammet skrev ut\n"+ output)

    def test_3_jerry(self):
        with patch('builtins.input', side_effect = [ 'Jerry', AssertionError("Indata bes för många gånger då följande namn anges: Jerry.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout().rstrip()
            expected = "Nästa!"
            self.assertTrue(expected in output, f"Med värdena Jerry borde programmet skriva ut\n{expected}\nProgrammet skrev ut\n"+ output)

    def test_4_jane_doe(self):
        with patch('builtins.input', side_effect = [ 'Jane Doe', '2', AssertionError("Indata bes för många gånger då följande namn anges: Jane Doe.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout().rstrip()
            expected = "Nästa!"
            self.assertTrue(expected in output, f"Med värdena Jane Doe, 2 borde programmet skriva ut\n{expected}\nProgrammet skrev ut\n"+ output)
            expected = 'Slutsumma 11.8'
            self.assertTrue(expected in output, f"Med värdena Jane Doe, 2 borde programmet skriva ut\n{expected}\nProgrammet skrev ut\n"+ output)

if __name__ == '__main__':
    unittest.main()
