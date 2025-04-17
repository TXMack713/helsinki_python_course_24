import unittest

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout

exercise = 'src.sju_broder'
@points('1.sju_broder')
class SeitsemanVeljestaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_module(exercise, 'fi')

    def test_content(self):
        reload_module(self.module)
        split_output = get_stdout().split('\n')
        self.assertEqual(len(split_output), 7, 'Utskriften borde ha {0} rader, men är nu {1} rad(er).'.format(7, len(split_output)))
        correct = "Aapo Eero Juhani Lauri Simeoni Timo Tuomas".split()
        for i in range(7):
            self.assertEqual(split_output[i], correct[i], "Raden {0} är inkorrekt.".format(i + 1))

if __name__ == '__main__':
    unittest.main()
    