from unittest import TestCase
from pregunta4 import *

class TestPregunta4(TestCase):

    def test_pregunta4(self):

        def test_cuaterniones(self):
            
            x = Cuaterniones(1, 2, 3, 4)
            y = Cuaterniones(1.2, 2.3, 3.4, 4.5)

            self.assertEqual(x.a, 1, "El valor de a deberia ser 1")
            self.assertEqual(x.b, 2, "El valor de b deberia ser 2")
            self.assertEqual(x.c, 3, "El valor de c deberia ser 3")
            self.assertEqual(x.d, 4, "El valor de d deberia ser 4")

            self.assertEqual(y.a, 1.2, "El valor de a deberia ser 1.2")
            self.assertEqual(y.b, 2.3, "El valor de b deberia ser 2.3")
            self.assertEqual(y.c, 3.4, "El valor de c deberia ser 3.4")
            self.assertEqual(y.d, 4.5, "El valor de d deberia ser 4.5")

        def test_sumaCuaternion(self):

            x = Cuaterniones(1, 2, 3, 4)
            y = Cuaterniones(1, 2, 3, 4)

            u = Cuaterniones(1.2, 2.3, 3.4, 4.5)
            v = Cuaterniones(1.2, 2.3, 3.4, 4.5)

            self.assertEqual(x + y, Cuaterniones(2, 4, 6, 8), "Se suma componente a componente")

            self.assertEqual(u + v, Cuaterniones(2.4, 4.6, 6.8, 9), "Se suma componente a componente")

        def test_sumaEscalar(self):

            x = Cuaterniones(1, 2, 3, 4)
            u = Cuaterniones(1.2, 2.3, 3.4, 4.5)
            y = 8

            self.assertEqual(x + y, Cuaterniones(9, 10, 11, 12), "Se suma 'y' a cada componente")

            self.assertEqual(u + y, Cuaterniones(9.2, 10.3, 11.4, 12.5), "Se suma 'y' a cada componente")

        def test_multiplicacionCuaternion(self):

            x = Cuaterniones(1, 2, 3, 4)
            y = Cuaterniones(1, 2, 3, 4)

            self.assertEqual(x * y, Cuaterniones(-28, 4, 6, 8), "Se multiplica segun la definicion")

        def test_multiplicacionEscalar(self):

            x = Cuaterniones(1, 2, 3, 4)
            u = Cuaterniones(1.2, 2.3, 3.4, 4.5)
            y = 5

            self.assertEqual(x * y, Cuaterniones(5, 10, 15, 20), "Se multiplica 'y' a cada componente")   

            self.assertEqual(u * y, Cuaterniones(6, 11.5, 17, 22.5), "Se multiplica 'y' a cada componente")

        def test_conjugado(self):
                
            x = Cuaterniones(1, 2, 3, 4)
    
            self.assertEqual(x.__conjugate__(), Cuaterniones(1, -2, -3, -4), "Se calcula el conjugado")

        def test_modulo(self):
                
            x = Cuaterniones(1, 2, 3, 4)

            self.assertEqual(x.__absolute__(), 5, "Se calcula el modulo")

        def test_str(self):

            x = Cuaterniones(1, 2, 3, 4)

            self.assertEqual(str(x), '(1 + 2i + 3j + 4k)', "Se imprime correctamente")

        def test_otros(self):

            x = Cuaterniones(1, 2, 3, 4)
            y = Cuaterniones(4, 3, 2, 1)
            z = Cuaterniones(1, 3, 5, 7)

            self.assertEqual(x * y + z, Cuaterniones(-11, 9, 29, 19), "Se multiplica y se suma segun la definicion")

