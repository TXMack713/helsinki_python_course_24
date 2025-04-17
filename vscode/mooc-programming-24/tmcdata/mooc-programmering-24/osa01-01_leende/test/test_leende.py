import unittest

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout

exercise = 'src.leende'
@points('1.leende')
class HymioTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_module(exercise, 'fi')

    def test_print_hymio(self):
        reload_module(self.module)
        output = get_stdout()
        self.assertTrue(output.startswith(":"), "Se till att du inte skriver ut extra tecken före leendet.")
        self.assertTrue(output.endswith(")"), "Se till att du inte skriver ut extra tecken efter leendet.")
        self.assertEqual(output, ":-)", "Inkorrekt leende.")

if __name__ == '__main__':
    unittest.main()
    