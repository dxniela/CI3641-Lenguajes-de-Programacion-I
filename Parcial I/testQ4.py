from unittest import TestCase
from pregunta4 import *

class TestPregunta4(TestCase):

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

        self.assertEqual(str(x + y), str(Cuaterniones(2, 4, 6, 8)), "Se suma componente a componente")

        self.assertEqual(str(u + v), str(Cuaterniones(2.4, 4.6, 6.8, 9.0)), "Se suma componente a componente")


    def test_sumaEscalar(self):

        x = Cuaterniones(1, 2, 3, 4)
        u = Cuaterniones(1.2, 2.3, 3.4, 4.5)
        y = 8

        self.assertEqual(str(x + y), str(Cuaterniones(9, 10, 11, 12)), "Se suma 'y' a cada componente")

        self.assertEqual(str(u + y), str(Cuaterniones(9.2, 10.3, 11.4, 12.5)), "Se suma 'y' a cada componente")


    def test_multiplicacionCuaternion(self):
        
        self.assertEqual(str(Cuaterniones(1, 2, 3, 4) * Cuaterniones(1, 2, 3, 4)), str(Cuaterniones(-28, 4, 6, 8)), "Se multiplica segun la definicion")


    def test_multiplicacionEscalar(self):

        x = Cuaterniones(1, 2, 3, 4)
        u = Cuaterniones(1.2, 2.3, 3.4, 4.5)
        y = 5

        self.assertEqual(str(x * y), str(Cuaterniones(5, 10, 15, 20)), "Se multiplica 'y' a cada componente")   

        self.assertEqual(str(u * y), str(Cuaterniones(6.0, 11.5, 17.0, 22.5)), "Se multiplica 'y' a cada componente")


    def test_conjugado(self):
                
        x = Cuaterniones(1, 2, 3, 4)
    
        self.assertEqual(str(~x), str(Cuaterniones(1, -2, -3, -4)), "Se calcula el conjugado")


    def test_modulo(self):
                
        x = Cuaterniones(1, 2, 3, 4)

        self.assertEqual(+x, 5.477225575051661, "Se calcula el modulo")


    def test_str(self):

        x = Cuaterniones(1, 2, 3, 4)
        y = Cuaterniones(3, -4, -2, 10)
        z = Cuaterniones(1, -3, 5, -7)
        u = Cuaterniones(3, 18, -30, -1)
        v = Cuaterniones(1, -2, 3, 4)
        t = Cuaterniones(1, 2, -3, 4)
        w = Cuaterniones(1, 2, 3, -4)

        self.assertEqual(str(x), '(1 + 2i + 3j + 4k)', "Se imprime correctamente")
        self.assertEqual(str(y), '(3 - 4i - 2j + 10k)', "Se imprime correctamente")
        self.assertEqual(str(z), '(1 - 3i + 5j - 7k)', "Se imprime correctamente")
        self.assertEqual(str(u), '(3 + 18i - 30j - 1k)', "Se imprime correctamente")
        self.assertEqual(str(v), '(1 - 2i + 3j + 4k)', "Se imprime correctamente")
        self.assertEqual(str(t), '(1 + 2i - 3j + 4k)', "Se imprime correctamente")
        self.assertEqual(str(w), '(1 + 2i + 3j - 4k)', "Se imprime correctamente")


    def test_otros(self):

        x = Cuaterniones(1, 2, 3, 4)
        y = Cuaterniones(4, 3, 2, 1)
        z = Cuaterniones(1, 3, 5, 7)

        self.assertEqual(str(x * y + z), str(Cuaterniones(-11, 9, 29, 19)), "Se multiplica y se suma segun la definicion")
        self.assertEqual(str((y + y) * (z + (~x))), str(Cuaterniones(-4, 28, 8, 36)), "Se multiplica, se suma y se calcula la conjugada segun la definicion")
        self.assertEqual(+(z * y), 50.19960159204453, "Se multiplica y se calcula el valor absoluto del resultado")
        self.assertEqual(str(x * 3.0 + 7.0), str(Cuaterniones(10.0, 13.0, 16.0, 19.0)), "Se multiplica y se sumapor escalares")
        self.assertEqual(str((y + y) * (+z)), str(Cuaterniones(73.32121111929344, 54.99090833947008, 36.66060555964672, 18.33030277982336)), "Se multiplica, se suma y se calcula valor absoluto segun la definicion")
