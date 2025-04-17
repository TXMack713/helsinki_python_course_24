import unittest
unittest.TestLoader.sortTestMethodsUsing = None

from tmc import points

from tmc.utils import get_stdout, load_module, reload_module, assert_ignore_ws, sanitize

exercise = 'src.gubben_noak'
@points('1.gubben_noak')
class UkkoNooaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_module(exercise, 'fi')
        
    def test_content(self):
        reload_module(self.module)
        out = get_stdout()
        self.assertTrue(len(out)>0, 'Koden skriver inte ut något.')
        split_output = sanitize(out).split('\n')

        self.assertFalse(len(split_output) != 3, 'Utskriften borde ha {0} rader, men är nu {1} rad(er).'.format(3, len(split_output)))
        assert_ignore_ws(self, split_output[0], 'Gubben Noak, gubben Noak var en hedersman', 'Första raden inkorrekt.')
        assert_ignore_ws(self, split_output[1], 'När han gick ur arken plantera han på marken', 'Andra raden inkorrekt.')
        assert_ignore_ws(self, split_output[2], 'Gubben Noak, gubben Noak var en hedersman.', 'Tredje raden inkorrekt.')

if __name__ == '__main__':
    unittest.main()
