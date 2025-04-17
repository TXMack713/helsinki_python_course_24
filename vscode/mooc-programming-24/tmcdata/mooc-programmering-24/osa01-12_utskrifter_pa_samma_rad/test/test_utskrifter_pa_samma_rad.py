import unittest

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout

exercise = 'src.utskrifter_pa_samma_rad'

@points('1.utskrifter_pa_samma_rad')
class TulostuksetSamalleRivilleTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_module(exercise, 'fi')

    def test_tulostus_1(self):
        reload_module(self.module)
        output = get_stdout().split("\n")
        correct = "5 + 8 - 4 = 9"

        self.assertTrue(len(output) == 1, "Programmet skriver inte ut på en rad utan på " + str(len(output)) + " rader.")
        self.assertEqual(output[0], correct, "Utskriften inkorrekt, borde vara\n{}\nUtskriften är\n{}".format(correct, output[0]))            
   
if __name__ == '__main__':
    unittest.main()
