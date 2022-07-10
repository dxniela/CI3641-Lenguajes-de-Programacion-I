from unittest import TestCase
from pregunta2 import *

class TestPregunta4(TestCase):

    def test_opBin(self):
        self.assertEqual(opBin('^', 'true', 'false'), False, 'Deberia dar false')
        self.assertEqual(opBin('&', 'false', 'true'), False, 'Deberia dar false')
        self.assertEqual(opBin('|', 'true', 'true'), True, 'Deberia dar true')
        self.assertEqual(opBin('=>', 'false', 'true'), True, 'Deberia dar true')

    def test_mostrarBin(self):
        self.assertEqual(mostrarBinPRE('^', 'true', 'false'), '^true')
        self.assertEqual(mostrarBinPRE('&', 'false', 'true'), 'false & true')
        self.assertEqual(mostrarBinPRE('|', 'true', 'true'), 'true | true')
        self.assertEqual(mostrarBinPRE('=>', 'false', 'true'), 'false => true')

        self.assertEqual(mostrarBinPOST('^', 'true', 'false'), '^false')
        self.assertEqual(mostrarBinPOST('&', 'false', 'true'), 'false & true')
        self.assertEqual(mostrarBinPOST('|', 'true', 'true'), 'true | true')
        self.assertEqual(mostrarBinPOST('=>', 'false', 'true'), 'false => true')

    def test_prefijo(self):
        self.assertEqual(prefijo('EVAL', ['=>', '&', 'true', 'true', 'false']), 'False')
        self.assertEqual(prefijo('EVAL', ['=>', '|', 'false', 'false', 'true']), 'True')
        self.assertEqual(prefijo('EVAL', ['|', '=>', 'false', 'true', '&', 'false', 'true']), 'True')
        #self.assertEqual(prefijo('EVAL', ['|', '^', '=>', 'true', '=>', 'false', 'true', 'false']), 'True')
        self.assertEqual(prefijo('MOSTRAR', ['=>', '&', 'true', 'true', 'false']), 'true & true => false')
        self.assertEqual(prefijo('MOSTRAR', ['=>', '|', 'false', 'false', 'true']), 'false | false => true')
        self.assertEqual(prefijo('MOSTRAR', ['|', '=>', '&', 'false', 'true', 'false', 'true']), 'false & true => false | true')
        self.assertEqual(prefijo('MOSTRAR', ['|', '^', '=>', '=>', 'true', 'false', 'true', 'false']), 'true => false => ^ true | false')

    def test_postfijo(self):
        self.assertEqual(postfijo('EVAL', ['true', 'true', '&', 'false', '=>']), 'False')
        self.assertEqual(postfijo('EVAL', ['false', 'false', 'true', '=>', '|']), 'True')
        self.assertEqual(postfijo('EVAL', ['false', 'true', '&', 'false', 'true', '|', '=>']), 'True')
        self.assertEqual(postfijo('EVAL', ['true', 'false', '=>', 'true', 'false', '|', '^', '=>']), 'True')
        self.assertEqual(postfijo('MOSTRAR', ['true', 'true', 'false', '=>', '&']), 'true & true => false')
        self.assertEqual(postfijo('MOSTRAR', ['false', 'false', 'true', '=>', '|']), 'false | false => true')
        self.assertEqual(postfijo('MOSTRAR', ['false', 'true', '&', 'false', 'true', '|', '=>']), 'false & true => false | true')
        self.assertEqual(postfijo('MOSTRAR', ['true', 'false', '=>', 'true', 'false', '|', '^', '=>']), 'true => false => ^true | false')

    def test_evaluar(self):
        self.assertEqual(evaluar('EVAL PRE => & true true false'), 'False')
        self.assertEqual(evaluar('EVAL PRE => | false false true'), 'True')
        self.assertEqual(evaluar('EVAL PRE | => false true & false true'), 'True')
        #self.assertEqual(evaluar('EVAL PRE | ^ => true => false true false'), 'True')
        self.assertEqual(evaluar('MOSTRAR PRE => & true true false'), 'true & true => false')
        self.assertEqual(evaluar('MOSTRAR PRE => | false false true'), 'false | false => true')
        self.assertEqual(evaluar('MOSTRAR PRE | => & false true false true'), 'false & true => false | true')
        self.assertEqual(evaluar('MOSTRAR PRE | ^ => => true false true false'), 'true => false => ^ true | false')
        self.assertEqual(evaluar('EVAL POST true true false => &'), 'False')
        self.assertEqual(evaluar('EVAL POST false false true => |'), 'True')
        self.assertEqual(evaluar('EVAL POST false true & false true | =>'), 'True')
        self.assertEqual(evaluar('EVAL POST true false => true false | ^ =>'), 'True')
        self.assertEqual(evaluar('MOSTRAR POST true true false => &'), 'true & true => false')
        self.assertEqual(evaluar('MOSTRAR POST false false true => |'), 'false | false => true')
        self.assertEqual(evaluar('MOSTRAR POST false true & false true | =>'), 'false & true => false | true')
        self.assertEqual(evaluar('MOSTRAR POST true false => true false | ^ =>'), 'true => false => ^true | false')

        self.assertEqual(evaluar('MOSTRAR '), "Error: falta el orden")
        self.assertEqual(evaluar('MOSTRAR POST'), "Error: falta la expresion")
        self.assertEqual(evaluar('MOSTRAR POSTFIJO'), "Error: orden invalido")
        self.assertEqual(evaluar('EVAL '), "Error: falta el orden")
        self.assertEqual(evaluar('EVAL POST'), "Error: falta la expresion")
        self.assertEqual(evaluar('EVAL POSTFIJO'), "Error: orden invalido")

        self.assertEqual(evaluar('holi'), "Error: comando invalido")
