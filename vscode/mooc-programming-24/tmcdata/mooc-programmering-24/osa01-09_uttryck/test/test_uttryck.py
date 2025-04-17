import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout

exercise = 'src.uttryck'

@points('1.uttryck')
class LausahduksetTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = ''):
            cls.module = load_module(exercise, 'fi')

    def test_tulostus_1(self):
        pieces = "simsala bimsala bim"
        plist = pieces.split()
        with patch('builtins.input', side_effect = plist):
            reload_module(self.module)
            output = get_stdout()
            self.assertTrue(len(output.split("\n")) == 1, "Programmet skrev inte ut en rad utan " + str(len(output)))            
            self.assertTrue(output.count("-") == 2, f"Utskriften borde ha två streck (-), men det fanns {output.count('-')} st.")
            for piece in plist:
                self.assertTrue(output.find(piece) > -1, "Utskriften innehöll inte " + piece +f" med indatat {pieces}")
            self.assertTrue(output.strip().count(" ") == 0, "Det finns extra mellanslag i utskriften.")
            vast = pieces.replace(" ", "-")+"!"
            self.assertTrue(output == vast, f"Utskriften följer inte exemplet.\nUtskriften var\n{output}\nUtskriften borde vara\n{vast}\ndå indatat är\n{pieces}")

    def test_tulostus_2(self):
        pieces = "ärtan pärtan puff"
        plist = pieces.split()
        with patch('builtins.input', side_effect = plist):
            reload_module(self.module)
            output = get_stdout()
            self.assertTrue(len(output.split("\n")) == 1, "Programmet skrev inte ut en rad utan " + str(len(output)))            
            self.assertTrue(output.count("-") == 2, "Utskriften innehåller inte två streck (-).")
            for piece in plist:
                self.assertTrue(output.find(piece) > -1, "Utskriften innehöll inte " + piece)
            self.assertTrue(output.strip().count(" ") == 0, "Det finns extra mellanslag i utskriften.")
            
            self.assertEqual(output, pieces.replace(" ", "-")+"!", "Utskriften följer inte exemplet.")
    
    def test_tulostus_3(self):
        pieces = "mutter putter skrudelutter"
        plist = pieces.split()
        with patch('builtins.input', side_effect = plist):
            reload_module(self.module)
            output = get_stdout()
            self.assertTrue(len(output.split("\n")) == 1, "Programmet skrev inte ut en rad utan " + str(len(output)))            
            self.assertTrue(output.count("-") == 2, "Utskriften innehåller inte två streck (-).")
            for piece in plist:
                self.assertTrue(output.find(piece) > -1, "Utskriften innehöll inte " + piece)
            self.assertTrue(output.strip().count(" ") == 0, "Det finns extra mellanslag i utskriften.")
            
            self.assertEqual(output, pieces.replace(" ", "-")+"!", "Utskriften följer inte exemplet.")
    
if __name__ == '__main__':
    unittest.main()
