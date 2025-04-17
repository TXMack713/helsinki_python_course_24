import unittest
from unittest.mock import patch
from inspect import getsource

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout

exercise = 'src.mellanslag_eller_inte'

expected = [
    "mitt namn är Tindra Testare, jag är 20 år",
    "",
    "till mina kunskaper hör",
    " - python (nybörjare)",
    " - java (expert)",
    " - programmering (nästan proffs)",
    "",
    "jag söker efter ett jobb vars lön är 2000-3000 euro i månaden"
]

@points('1.mellanslag_eller_inte')
class ValilyontiTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with patch('builtins.input', return_value = ''):
            cls.module = load_module(exercise, 'fi')

    def test_tulostus_1(self):
        reload_module(self.module)
        output = get_stdout().split('\n')
        self.assertEqual(8, len(output), f"Programmet skriver ut {len(output)} rader fast antalet borde vara åtta. Du skriver väl också ut de tomma raderna?")
        for i in range(0, 8):
            if i in [3, 4, 5]:
                self.assertEqual(' ', output[i][0], f"Rad {i+1} inkorrekt, du skrev ut:\n{output[i]}\nObservera mellanslaget i början av raden!")    
            self.assertEqual(expected[i], output[i].rstrip(), f"Rad {i+1} inkorrekt, den borde vara:\n{expected[i]}\nDitt program skrev ut:\n{output[i]}")

    def test_tulostus_2(self):
        kielletyt = [
            "mitt namn är Tindra Testare, jag är 20 år",
            " - python (nybörjare)",
            " - java (expert)",
            " - programmering (nästan proffs)",
            "jag söker efter ett jobb vars lön är 2000-3000 euro i månaden"
        ]

        source = getsource(self.module)
        for line in source.split("\n"):
            for kielletty in kielletyt:
                if kielletty in line:
                    self.assertTrue(False, f"Använd variabelvärden, koden får inte innehålla raden\n{line}")

if __name__ == '__main__':
    unittest.main()
