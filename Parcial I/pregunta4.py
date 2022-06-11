# Daniela Ramirez 16-10940

# Programa sobre cuaterniones y sus operaciones

import math

class Cuaterniones(object):

    a: int | float
    b: int | float
    c: int | float
    d: int | float

    def __init__(self, a: int | float, b: int | float, c: int | float, d: int | float):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __add__(self, cuaternion):
        if type(cuaternion) == Cuaterniones:
            return Cuaterniones(self.a + cuaternion.a, self.b + cuaternion.b, self.c + cuaternion.c, self.d + cuaternion.d)
        elif type(cuaternion == int or cuaternion == float):
            return Cuaterniones(self.a + cuaternion, self.b + cuaternion, self.c + cuaternion, self.d + cuaternion)

    def __conjugate__(self):
        return Cuaterniones(self.a, -self.b, -self.c, -self.d)

    def __mul__(self, cuaternion):
        if type(cuaternion) == Cuaterniones:
            return Cuaterniones(self.a * cuaternion.a - self.b * cuaternion.b - self.c * cuaternion.c - self.d * cuaternion.d, 
                                self.a * cuaternion.b + self.b * cuaternion.a + self.c * cuaternion.d - self.d * cuaternion.c,
                                self.a * cuaternion.c - self.b * cuaternion.d + self.c * cuaternion.a + self.d * cuaternion.b,
                                self.a * cuaternion.d + self.b * cuaternion.c - self.c * cuaternion.b + self.d * cuaternion.a)
        elif type(cuaternion == int or cuaternion == float):
            return Cuaterniones(self.a * cuaternion, self.b * cuaternion, self.c * cuaternion, self.d * cuaternion)

    def __absolute__(self):
        return math.floor((self.a ** 2 + self.b ** 2 + self.c ** 2 + self.d ** 2) ** 0.5)

    def __str__(self) -> str:
        if self.b < 0 and self.c < 0 and self.d < 0:
            return f'({self.a} - {abs(self.b)}i - {abs(self.c)}j - {abs(self.d)}k)'.format(self=self)
        elif self.b < 0 and self.c < 0:
            return f'({self.a} - {abs(self.b)}i - {abs(self.c)}j + {self.d}k)'.format(self=self)
        elif self.b < 0 and self.d < 0:
            return f'({self.a} - {abs(self.b)}i + {self.c}j - {abs(self.d)}k)'.format(self=self)
        elif self.c < 0 and self.d < 0:
            return f'({self.a} + {self.b}i - {abs(self.c)}j - {abs(self.d)}k)'.format(self=self)
        elif self.b < 0:
            return f'({self.a} - {abs(self.b)}i + {self.c}j + {self.d}k)'.format(self=self)
        elif self.c < 0:
            return f'({self.a} + {self.b}i - {abs(self.c)}j + {self.d}k)'.format(self=self)
        elif self.d < 0:
            return f'({self.a} + {self.b}i + {self.c}j - {abs(self.d)}k)'.format(self=self)
        else:
            return f'({self.a} + {self.b}i + {self.c}j + {self.d}k)'.format(self=self) 