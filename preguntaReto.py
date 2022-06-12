import sympy
from math import *
f=lambda a,b,n:a if n<1 else b if n<2 else f(b,a+b,n-1)
n=int(input())
print(f(0,1,floor(log2(sympy.bell(n+1)))+1))