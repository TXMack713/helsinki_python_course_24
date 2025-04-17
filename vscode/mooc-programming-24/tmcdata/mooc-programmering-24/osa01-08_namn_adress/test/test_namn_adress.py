import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, sanitize

exercise = 'src.namn_adress'

@points('1.namn_adress')
class NimiJaOsoiteTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = ''):
            cls.module = load_module(exercise, 'fi')

    def test_tulostus_1(self):
        test_input = "Per,Python,Pythonstigen 1,12345 PYTHON"
        test_output = "Per Python,Pythonstigen 1,12345 PYTHON".split(",")
        with patch('builtins.input', side_effect = test_input.split(",")):
            reload_module(self.module)
            out = get_stdout()
            self.assertTrue(len(out)>0, "Programmet skrev inte ut någonting.") 
            output = out.split("\n")
            self.assertTrue(len(output) == 3, "Programmet skrev inte ut tre rader utan  " + str(len(output)))
            self.assertTrue(sanitize(output[0]) == sanitize(test_output[0]), f"Första raden inkorrekt.\nFörväntade\n{test_output[0]}\nRaden var\n{output[0]}\nGivna indata\n{test_input}")
            for i in range(1,3):
                self.assertEqual(output[i], test_output[i], 'Rad {} inkorrekt med indatat {}'.format((i + 1), test_input))
    
    def test_tulostus_2(self):
        test_input = "Kex,Kexigare,Finurliggränd 123 A 1,54321,PÅHITTIG"
        test_output = "Kex Kexigare,Finurliggränd 123 A 1,54321,PÅHITTIG".split(",")
        with patch('builtins.input', side_effect = test_input.split(",")):
            reload_module(self.module)
            output = get_stdout().split("\n")
            self.assertTrue(len(output) == 3, "Programmet skrev inte ut tre rader utan  " + str(len(output)))            
            self.assertTrue(sanitize(output[0]) == sanitize(test_output[0]), f"Första raden inkorrekt.\nFörväntade\n{test_output[0]}\nRaden var\n{output[0]}\nGivna indata\n{test_input}")
            for i in range(1, 3):
                self.assertEqual(output[i], test_output[i], 'Rad {} inkorrekt med indatat {}'.format((i + 1), test_input))
 
    def test_tulostus_3(self):
        test_input = "Rebecca Riona,Rymdvarelse,Svarta hålet 555 bst. 234,99099,RYMDEN"
        test_output = "Rebecca Riona Rymdvarelse,Svarta hålet 555 bst. 234,99099,RYMDEN".split(",")
        with patch('builtins.input', side_effect = test_input.split(",")):
            reload_module(self.module)
            output = get_stdout().split("\n")
            self.assertTrue(len(output) == 3, "Programmet skrev inte ut tre rader utan  " + str(len(output)))            
            self.assertTrue(sanitize(output[0]) == sanitize(test_output[0]), f"Första raden inkorrekt.\nFörväntade\n{test_output[0]}\nRaden var\n{output[0]}\nGivna indata\n{test_input}")
            for i in range(1, 3):
                self.assertEqual(output[i], test_output[i], 'Rad {} inkorrekt med indatat {}'.format((i + 1), test_input))
            
if __name__ == '__main__':
    unittest.main()
