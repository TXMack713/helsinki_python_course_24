import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout
from functools import reduce
from random import randint

exercise = 'src.andra_gradens_ekvation'

@points('1.andra_gradens_ekvation')
class ToisenAsteenYhtaloTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', side_effect=["1","2","-8"]):
            cls.module = load_module(exercise, 'fi')

    def test_output_1(self):
        inputs = "1,2,-8"
        root1 = "2"
        root2 = "-4"
        ilist = inputs.split(",")
        with patch('builtins.input', side_effect=ilist):
            reload_module(self.module)
            output = get_stdout()
            
            self.assertTrue(len(output.split("\n")) == 1, "Istället för en rad skrivs {} rader ut".format(len(output.split("\n"))))
            self.assertTrue(output.find(root1) > -1, "Med värdet {} skrivs inte den korrekta roten {} ut".format(inputs, root1))
            self.assertTrue(output.find(root2) > -1, "Med värdet {} skrivs inte den korrekta roten {} ut".format(inputs, root2))

    def test_output_2(self):
        inputs = "5,6,1"
        root1 = "-0.2"
        root2 = "-1"
        ilist = inputs.split(",")
        with patch('builtins.input', side_effect=ilist):
            reload_module(self.module)
            output = get_stdout()
            
            self.assertTrue(len(output.split("\n")) == 1, "Istället för en rad skrivs {} rader ut".format(len(output.split("\n"))))
            self.assertTrue(output.find(root1) > -1, "Med värdet {} skrivs inte den korrekta roten {} ut".format(inputs, root1))
            self.assertTrue(output.find(root2) > -1, "Med värdet {} skrivs inte den korrekta roten {} ut".format(inputs, root2))

    def test_output_3(self):
        inputs = "2,-14,24"
        root1 = "4"
        root2 = "3"
        ilist = inputs.split(",")
        with patch('builtins.input', side_effect=ilist):
            reload_module(self.module)
            output = get_stdout()
            
            self.assertTrue(len(output.split("\n")) == 1, "Istället för en rad skrivs {} rader ut".format(len(output.split("\n"))))
            self.assertTrue(output.find(root1) > -1, "Med värdet {} skrivs inte den korrekta roten {} ut".format(inputs, root1))
            self.assertTrue(output.find(root2) > -1, "Med värdet {} skrivs inte den korrekta roten {} ut".format(inputs, root2))
    


                 
            
   
if __name__ == '__main__':
    unittest.main()
