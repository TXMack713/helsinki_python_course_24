import unittest
from unittest.mock import patch

from tmc import points
from tmc.utils import load_module, reload_module, get_stdout

exercise = 'src.kladsel'

housut_tpaita = "Ta på dig byxor och t-skjorta"
pitkahih = "Ta på dig också en långärmad tröja"
takki = "Klä på dig en jacka"
lammin_takki = "En varm jacka rekommenderas"
hanskat = "Vantar rekommenderas också"
sateenvarjo = "Kom ihåg paraplyet!"


@points('1.kladsel')
class VaatteetTest(unittest.TestCase):
    @classmethod 
    def setUpClass(cls):
        with patch('builtins.input', return_value = '0'):
            cls.module = load_module(exercise, 'fi')

    def test_25(self):
        with patch('builtins.input', side_effect = [ '25', 'nej', AssertionError("Indata frågas för många gånger.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            syote = "25, nej"
            self.assertFalse(prompt.call_count < 1, 'Programmet ska be om två värden.')
            self.assertTrue(housut_tpaita in output, f"Med värdet:\n{syote}\nborde programmet skriva ut raden\n" + housut_tpaita+ "\nProgrammet skriver ut\n"+ output)
            self.assertFalse(pitkahih in output, f"Med värdet:\n{syote}\nborde programmet INTE skriva ut raden\n" + pitkahih+ "\nProgrammet skriver ut\n"+ output)
            self.assertFalse(takki in output, f"Med värdet:\n{syote}\nborde programmet INTE skriva ut raden\n" + takki+ "\nProgrammet skriver ut\n"+ output)
            self.assertFalse(lammin_takki in output, f"Med värdet:\n{syote}\nborde programmet INTE skriva ut raden\n" + lammin_takki+ "\nProgrammet skriver ut\n"+ output)
            self.assertFalse(hanskat in output, f"Med värdet:\n{syote}\nborde programmet INTE skriva ut raden\n" + hanskat+ "\nProgrammet skriver ut\n"+ output)
            self.assertFalse(sateenvarjo in output, f"Med värdet:\n{syote}\nborde programmet INTE skriva ut raden\n" + sateenvarjo+ "\nProgrammet skriver ut\n"+ output)
    
    def test_21_sade(self):
        with patch('builtins.input', side_effect = [ '21', 'ja', AssertionError("Indata frågas för många gånger.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            syote = "21, ja"
            self.assertFalse(prompt.call_count < 1, 'Programmet ska be om två värden.')
            self.assertTrue(housut_tpaita in output, f"Med värdet:\n{syote}\nborde programmet skriva ut raden\n" + housut_tpaita+ "\nProgrammet skriver ut\n"+ output)
            self.assertFalse(pitkahih in output, f"Med värdet:\n{syote}\nborde programmet INTE skriva ut raden\n" + pitkahih+ "\nProgrammet skriver ut\n"+ output)
            self.assertFalse(takki in output, f"Med värdet:\n{syote}\nborde programmet INTE skriva ut raden\n" + takki+ "\nProgrammet skriver ut\n"+ output)
            self.assertFalse(lammin_takki in output, f"Med värdet:\n{syote}\nborde programmet INTE skriva ut raden\n" + lammin_takki+ "\nProgrammet skriver ut\n"+ output)
            self.assertFalse(hanskat in output, f"Med värdet:\n{syote}\nborde programmet INTE skriva ut raden\n" + hanskat+ "\nProgrammet skriver ut\n"+ output)
            self.assertTrue(sateenvarjo in output, f"Med värdet:\n{syote}\nborde programmet skriva ut raden\n" + sateenvarjo+ "\nProgrammet skriver ut\n"+ output)
    
    def test_15(self):
        with patch('builtins.input', side_effect = [ '15', 'nej', AssertionError("Indata frågas för många gånger.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            syote = "15, nej"
            self.assertFalse(prompt.call_count < 1, 'Programmet ska be om två värden.')
            self.assertTrue(housut_tpaita in output, f"Med värdet:\n{syote}\nborde programmet skriva ut raden\n" + housut_tpaita+ "\nProgrammet skriver ut\n"+ output)
            self.assertTrue(pitkahih in output, f"Med värdet:\n{syote}\nborde programmet skriva ut raden\n" + pitkahih+ "\nProgrammet skriver ut\n"+ output)
            self.assertFalse(takki in output, f"Med värdet:\n{syote}\nborde programmet INTE skriva ut raden\n" + takki+ "\nProgrammet skriver ut\n"+ output)
            self.assertFalse(lammin_takki in output, f"Med värdet:\n{syote}\nborde programmet INTE skriva ut raden\n" + lammin_takki+ "\nProgrammet skriver ut\n"+ output)
            self.assertFalse(hanskat in output, f"Med värdet:\n{syote}\nborde programmet INTE skriva ut raden\n" + hanskat+ "\nProgrammet skriver ut\n"+ output)
            self.assertFalse(sateenvarjo in output, f"Med värdet:\n{syote}\nborde programmet INTE skriva ut raden\n" + sateenvarjo+ "\nProgrammet skriver ut\n"+ output)
    
    def test_20_sade(self):
        with patch('builtins.input', side_effect = [ '20', 'ja', AssertionError("Indata frågas för många gånger.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            syote = "20, ja"
            self.assertFalse(prompt.call_count < 1, 'Programmet ska be om två värden.')
            self.assertTrue(housut_tpaita in output, f"Med värdet:\n{syote}\nborde programmet skriva ut raden\n" + housut_tpaita+ "\nProgrammet skriver ut\n"+ output)
            self.assertTrue(pitkahih in output, f"Med värdet:\n{syote}\nborde programmet skriva ut raden\n" + pitkahih+ "\nProgrammet skriver ut\n"+ output)
            self.assertFalse(takki in output, f"Med värdet:\n{syote}\nborde programmet INTE skriva ut raden\n" + takki+ "\nProgrammet skriver ut\n"+ output)
            self.assertFalse(lammin_takki in output, f"Med värdet:\n{syote}\nborde programmet INTE skriva ut raden\n" + lammin_takki+ "\nProgrammet skriver ut\n"+ output)
            self.assertFalse(hanskat in output, f"Med värdet:\n{syote}\nborde programmet INTE skriva ut raden\n" + hanskat+ "\nProgrammet skriver ut\n"+ output)
            self.assertTrue(sateenvarjo in output, f"Med värdet:\n{syote}\nborde programmet skriva ut raden\n" + sateenvarjo+ "\nProgrammet skriver ut\n"+ output)
    
    def test_10(self):
        with patch('builtins.input', side_effect = [ '10', 'nej', AssertionError("Indata frågas för många gånger.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            syote = "10, nej"
            self.assertFalse(prompt.call_count < 1, 'Programmet ska be om två värden.')
            self.assertTrue(housut_tpaita in output, f"Med värdet:\n{syote}\nborde programmet skriva ut raden\n" + housut_tpaita+ "\nProgrammet skriver ut\n"+ output)
            self.assertTrue(pitkahih in output, f"Med värdet:\n{syote}\nborde programmet skriva ut raden\n" + pitkahih+ "\nProgrammet skriver ut\n"+ output)
            self.assertTrue(takki in output, f"Med värdet:\n{syote}\nborde programmet skriva ut raden\n" + takki+ "\nProgrammet skriver ut\n"+ output)
            self.assertFalse(lammin_takki in output, f"Med värdet:\n{syote}\nborde programmet INTE skriva ut raden\n" + lammin_takki+ "\nProgrammet skriver ut\n"+ output)
            self.assertFalse(hanskat in output, f"Med värdet:\n{syote}\nborde programmet INTE skriva ut raden\n" + hanskat+ "\nProgrammet skriver ut\n"+ output)
            self.assertFalse(sateenvarjo in output, f"Med värdet:\n{syote}\nborde programmet INTE skriva ut raden\n" + sateenvarjo+ "\nProgrammet skriver ut\n"+ output)
    
    def test_3(self):
        with patch('builtins.input', side_effect = [ '3', 'nej', AssertionError("Indata frågas för många gånger.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            syote = "3, nej"
            self.assertFalse(prompt.call_count < 1, 'Programmet ska be om två värden.')
            self.assertTrue(housut_tpaita in output, f"Med värdet:\n{syote}\nborde programmet skriva ut raden\n" + housut_tpaita+ "\nProgrammet skriver ut\n"+ output)
            self.assertTrue(pitkahih in output, f"Med värdet:\n{syote}\nborde programmet skriva ut raden\n" + pitkahih+ "\nProgrammet skriver ut\n"+ output)
            self.assertTrue(takki in output, f"Med värdet:\n{syote}\nborde programmet skriva ut raden\n" + takki+ "\nProgrammet skriver ut\n"+ output)
            self.assertTrue(lammin_takki in output, f"Med värdet:\n{syote}\nborde programmet skriva ut raden\n" + lammin_takki+ "\nProgrammet skriver ut\n"+ output)
            self.assertTrue(hanskat in output, f"Med värdet:\n{syote}\nborde programmet skriva ut raden\n" + hanskat+ "\nProgrammet skriver ut\n"+ output)
            self.assertFalse(sateenvarjo in output, f"Med värdet:\n{syote}\nborde programmet INTE skriva ut raden\n" + sateenvarjo+ "\nProgrammet skriver ut\n"+ output)
    
    def test_5_sade(self):
        with patch('builtins.input', side_effect = [ '5', 'ja', AssertionError("Indata frågas för många gånger.") ]) as prompt:
            reload_module(self.module)
            output = get_stdout()
            syote = "5, ja"
            self.assertFalse(prompt.call_count < 1, 'Programmet ska be om två värden.')
            self.assertTrue(housut_tpaita in output, f"Med värdet:\n{syote}\nborde programmet skriva ut raden\n" + housut_tpaita+ "\nProgrammet skriver ut\n"+ output)
            self.assertTrue(pitkahih in output, f"Med värdet:\n{syote}\nborde programmet skriva ut raden\n" + pitkahih+ "\nProgrammet skriver ut\n"+ output)
            self.assertTrue(takki in output, f"Med värdet:\n{syote}\nborde programmet skriva ut raden\n" + takki+ "\nProgrammet skriver ut\n"+ output)
            self.assertTrue(lammin_takki in output, f"Med värdet:\n{syote}\nborde programmet skriva ut raden\n" + lammin_takki+ "\nProgrammet skriver ut\n"+ output)
            self.assertTrue(hanskat in output, f"Med värdet:\n{syote}\nborde programmet skriva ut raden\n" + hanskat+ "\nProgrammet skriver ut\n"+ output)
            self.assertTrue(sateenvarjo in output, f"Med värdet:\n{syote}\nborde programmet skriva ut raden\n" + sateenvarjo+ "\nProgrammet skriver ut\n"+ output)
    

if __name__ == '__main__':
    unittest.main()
