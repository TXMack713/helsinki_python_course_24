import unittest

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout

exercise = 'src.rakneoperationer'

@points('1.rakneoperationer')
class LaskutoimituksetTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_module(exercise, 'fi')

    def test_tulostus_1(self):
        reload_module(self.module)
        output = get_stdout().split("\n")
        correct = self.generate(27,15)

        self.assertTrue(len(output) == 4, "Programmet skrev inte ut fyra rader utan " + str(len(output)) + " rader.")
        for i in range(4):
            self.assertEqual(output[i].rstrip(), correct[i], "Utskrift inkorrekt på rad {}, borde vara\n{}\nProgrammet skriver ut\n{}".format((i + 1), correct[i], output[i]))            
        
    def generate(self, x, y):
        s = [""] * 4
        s[0] = "{} + {} = {}".format(x, y, (x + y))
        s[1] = "{} - {} = {}".format(x, y, (x - y))
        s[2] = "{} * {} = {}".format(x, y, (x * y))
        s[3] = "{} / {} = {}".format(x, y, (x / y))
        return s
   

if __name__ == '__main__':
    unittest.main()
