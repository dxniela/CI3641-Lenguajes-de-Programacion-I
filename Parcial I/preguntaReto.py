# Daniela Ramirez 16-10940
import time
from sympy import *
import math
inicio = time.time()
def Fib(N):
    if(N==0 or N==1):
        return N
    else:
        return (Fib(N-2)+Fib(N-1))
def evil(N):
    return Fib(math.floor(math.log2(bell(N+1)))+1)
n = int(input("N: "))
print(evil(n))
final = time.time()
print("Tiempo: ", final-inicio)