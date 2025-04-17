import unittest

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout

exercise = 'src.skriv_ut_kod'

@points('1.skriv_ut_kod')
class TulostaKoodiTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_module(exercise, 'fi')

    def test_tulostus(self):
        reload_module(self.module)
        output = get_stdout()
        split_output = output.split('\n')
        oikea = 'print("Hej!")'

        self.assertFalse(len(output) == 0, "Du skrev inte ut något.")
        self.assertEqual(len(split_output), 1, "Det finns för många rader i utskriften.")
        self.assertTrue(output.count('print') == 1, f"Från utskriften saknas print-kommandot. Utskriften var\n{output}\nUtskriften borde vara\n{oikea}")
        self.assertTrue(output.count('"') == 2, f"Citattecknen saknas i utskriften. Utskriften var\n{output}\nUtskriften borde vara\n{oikea}")
        self.assertEqual(output, oikea , f"Utskriften inkorrekt. Utskriften var\n{output}\nUtskriften borde vara\n{oikea}")

if __name__ == '__main__':
    unittest.main()
