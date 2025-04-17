import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, sanitize
from functools import reduce

exercise = 'src.produkten_av_talen'

@points('1.produkten_av_talen')
class LukujenTuloTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect = "0,0,0".split(",")):
            cls.module = load_module(exercise, 'fi')

    def test_tulostus_1(self):
        inputs = "1,2,3"
        with patch('builtins.input', side_effect = inputs.split(",")):
            reload_module(self.module)
            output = get_stdout().strip()
            ilist = [int(x) for x in inputs.split(",")]
            correct = "Produkten av talen är " + str(reduce(lambda x,y: x * y, ilist))
            self.assertTrue(len(output.split("\n")) == 1, "Programmet skrev inte ut en rad utan " + str(len(output.split("\n"))) + " rader.")            
            self.assertEqual(sanitize(output), sanitize(correct), "Programmet skrev ut\n{}\nDen korrekta utskriften borde ha varit\n{}\nmed värdena {}".format(output, correct, inputs)) 
            
    def test_tulostus_2(self):
        inputs = "7,2,14"
        with patch('builtins.input', side_effect = inputs.split(",")):
            reload_module(self.module)
            output = get_stdout().strip()
            ilist = [int(x) for x in inputs.split(",")]
            correct = "Produkten av talen är " + str(reduce(lambda x,y: x * y, ilist))
            self.assertTrue(len(output.split("\n")) == 1, "Programmet skrev inte ut en rad utan " + str(len(output.split("\n"))) + " rader.")            
            self.assertEqual(sanitize(output), sanitize(correct), "Programmet skrev ut\n{}\nDen korrekta utskriften borde ha varit\n{}\nmed värdena {}".format(output, correct, inputs)) 
            
if __name__ == '__main__':
    unittest.main()
