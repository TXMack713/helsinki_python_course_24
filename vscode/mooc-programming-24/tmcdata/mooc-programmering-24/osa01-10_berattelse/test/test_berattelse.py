import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout, sanitize

exercise = 'src.berattelse'

@points('1.berattelse')
class TarinaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = ''):
            cls.module = load_module(exercise, 'fi')

    def test_tulostus_1(self):
        pieces = "Jennifer,2000"
        plist = pieces.split(",")
        with patch('builtins.input', side_effect = plist):
            reload_module(self.module)
            output = get_stdout().strip()
                
            self.assertTrue(len(output)>0, "Programmet skrev inte ut någonting. Indata:\nJennifer\n2000")
                    
            for piece in plist:
                self.assertTrue(output.find(piece) > -1, "Hittade inte " + piece + " i utskriften, indata:\nJennifer\n2000")
            
            story = plist[0] + " är kommunens bästa läkare. När " + plist[0] + ", född " + plist[1]
            story += ", vaknar till ett telefonsamtal klockan 4 på morgonen, blir det brådis. "
            story += plist[0] + " behövs till akuten för att rädda livet hos en cyklist som krockat med en bil."
            output = output.replace("\n"," ")
            self.assertTrue(sanitize(output) == sanitize(story), "Utskriften inkorrekt med indatat\nJennifer\n2000\nDu skrev ut:\n{}\nFörväntade:\n{}".format(output, story))

    def test_tulostus_2(self):
        pieces = "Konstantin,1966"
        plist = pieces.split(",")
        with patch('builtins.input', side_effect = plist):
            reload_module(self.module)
            output = get_stdout().strip()
                     
            for piece in plist:
                self.assertTrue(output.find(piece) > -1, "Hittade inte " + piece + " i utskriften, indata:\nKonstantin\n1966")
            
            story = plist[0] + " är kommunens bästa läkare. När " + plist[0] + ", född " + plist[1]
            story += ", vaknar till ett telefonsamtal klockan 4 på morgonen, blir det brådis. "
            story += plist[0] + " behövs till akuten för att rädda livet hos en cyklist som krockat med en bil."
            output = output.replace("\n"," ")
            self.assertTrue(sanitize(output) == sanitize(story), "Utskriften inkorrekt med indatat\nKonstantin\n1966\nDu skrev ut:\n{}\nFörväntade:\n{}".format(output, story))
            
    def test_tulostus_3(self):
        pieces = "Adele,1991"
        plist = pieces.split(",")
        with patch('builtins.input', side_effect = plist):
            reload_module(self.module)
            output = get_stdout().strip()
                     
            for piece in plist:
                self.assertTrue(output.find(piece) > -1, "Hittade inte " + piece)
            
            story = plist[0] + " är kommunens bästa läkare. När " + plist[0] + ", född " + plist[1]
            story += ", vaknar till ett telefonsamtal klockan 4 på morgonen, blir det brådis. "
            story += plist[0] + " behövs till akuten för att rädda livet hos en cyklist som krockat med en bil."
            output = output.replace("\n"," ")
            self.assertTrue(sanitize(output) == sanitize(story), "Utskriften inkorrekt med indatat\nAdele\n1991\nDu skrev ut:\n{}\nFörväntade:\n{}".format(output, story))
if __name__ == '__main__':
    unittest.main()
