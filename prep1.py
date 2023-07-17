import time 
import string 


# print(string.ascii_letters)


char_list = list(string.ascii_letters)


print(char_list[0])


# list,set -> mutable 
# tuple ->immutable 

import sys 

print(sys.getsizeof(0))


def cal(a):
    for i in range(100000):
        a * 2

start = time.perf_counter()
cal(10)
end= time.perf_counter()
# print(end - start)



print(type(5.0))


import math

print(math.floor(-3.4400))


print(int("01010111",2))


a= 12345
digits =[]

while a>0:
    m = a%10
    a = a//10
    digits.insert(0,m)

for i in digits:
    print(i)

print(bin(10))

from fractions import Fraction

print(float(Fraction(22/7)))
x = float(Fraction(22/7))
print(format(x,'0.6f'))


x =0.00001 
y=0.00002


from math import isclose 
print(isclose(x,y,rel_tol=0.01,abs_tol=0.01))

from math import trunc 
 


print(trunc(-10.4))


print(round(1.9,0))

import decimal 
from decimal import Decimal

decimal.getcontext().prec = 6

a = Decimal("0.12345")
b = Decimal("0.12345")
print(a+b) 


with decimal.localcontext() as ctx: 
    ctx.prec = 2
    c = a + b
    print(c)



a= Decimal('0.1')
print(a.ln())
print(a.exp())
print(a.sqrt())

print(math.sqrt(a))


a = 1 + 1j
b = complex(1,2)

import cmath
print(cmath.phase(a))


print(cmath.pi/4  == cmath.phase(a))