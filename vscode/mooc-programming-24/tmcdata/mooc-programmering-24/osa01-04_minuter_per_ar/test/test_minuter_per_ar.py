import unittest

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout

exercise = 'src.minuter_per_ar'

@points('1.minuter_per_ar')
class MinuuttejaVuodessaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_module(exercise, 'fi')

    def test_tulostus(self):
        reload_module(self.module)
        output = get_stdout()
        split_output = output.split('\n')

        # self.assertEqual(len(split_output), 1, "Det finns för många rader i utskriften.")
        self.assertTrue(output.find("525600") > -1, "Utskriften innehåller inte korrekt minutantal.")

if __name__ == '__main__':
    unittest.main()
