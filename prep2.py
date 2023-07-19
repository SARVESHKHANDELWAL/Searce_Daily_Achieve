
# print(help(bool))
print(issubclass(bool,int))
print(type(False),id(False),int(False))
print(type(3<4), None is False)



a= None 

if a: 
    print(a[0])
else : 
    print("Nothing to see here !!!")


a = 10 
b =  1

if b and a/b>2: 
    print('a is atleast twice b')


import string 

a='C'
print(a in string.ascii_uppercase)
print(string.ascii_uppercase)



name = "Sarvesh"

for x  in name: 
    print(x)  


# Boolean 

s1 = None 
s2 = ''
s3 = 'Sarvesh'
print((s1 and s1[0]))
print((s2 and s2[0]))
print((s2 and s2[0]))

from fractions import Fraction
import math 

print(Fraction(22,7) > math.pi)


from fractions import Fraction
# Fraction(16, -10)
# Fraction(-8, 5)
# Fraction(123)
# Fraction(123, 1)
# Fraction()
# Fraction(0, 1)
# Fraction('3/7')
# Fraction(3, 7)
# Fraction(' -3/7 ')
# Fraction(-3, 7)
# Fraction('1.414213 \t\n')
# Fraction(1414213, 1000000)
# Fraction('-.125')
# Fraction(-1, 8)
# Fraction('7e-6')
# Fraction(7, 1000000)
# Fraction(2.25)
# Fraction(9, 4)
# Fraction(1.1)
print(Fraction(2476979795053773, 2251799813685248))
from decimal import Decimal
print(Fraction(Decimal('1.1')))
print(Fraction(11, 10))



# c = 3  not in [1,2,3]
c=  'key1' not in {'key1':1}
print(c)



print ('a'> 'A' > 'Z')


# Functional Parameters 

# A 'parameter'is the variable listed inside the parentheses in the function definition. 
# An 'argument' is the value that are sent to the function when it is called.



def func(a,b = 100):
    if (a%100 ==0):
        print("a is divisble by 100")
    else: 
        print("a is not divisble y 100")


l = [1,2,232]

def func1(a,b,c):
    print(a)
    print(b)
    print(c)


func1(*l)





print(func(200))
       
# dict
d= {'a': 1, 'b': 2, 'c' : 3, 'd': 4}
for a,b in d.items():
    print(a,b)


d1 = {'A': 2 , **d}


for a,b in d1.items():
    print(a,b)


s1 = {1, 2, 3, 4, 5, 6}
s2 = {4, 5, 6, 7, 8}
s1.union(s2)
print(s1)



print({*d1})

# iterable unpacking 
a,b,(c,d,*e) = [1,2,"python"]


print(c)

# l = [1,2 ,3, 4 , "python"]

# print(l[0],l[1:-1],l[-1][0],l[-1][1],l[-1][2:])


l = [10,20,30]

def func(a,b,c):
    print(a)
    print(b)
    print(c)

# args coding 
func(*l)

# putting together 


def func3(a, b=1,*args,d,e=True):
    print(a,b,c,d,e)


func3()



