def avg(): 
    total =0
    count =0
    def add(number): 
        nonlocal total 
        nonlocal count 
        total = total + number
        count =count + 1
        return total/count
    return add


a = avg()


print(a(30))
print(a(20))


def avg1(): 
    total =0
    count =0
    def add1(number=90): 
        nonlocal total 
        nonlocal count 
        total = total + number
        count =count + 1
        return total/count
    return add1


a1 = avg1()


print(a1())
print(a1())



# DECORATORS 
# takes a function as an argument 
# returns a closure 
# the closure usually accepts ny combination of parameters


# In Python, a decorator is a design pattern that allows you to modify the functionality of a function by wrapping it in another function.


def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

def ordinary():
    print("I am ordinary")

decorated_func = make_pretty(ordinary)

decorated_func()



def make_pretty(func):

    def inner():
        print("I got decorated")
        func()
    return inner

@make_pretty
def ordinary():
    print("I am ordinary")

ordinary()  


# Chaining Decorators in Python

def star(func):
    def inner(*args, **kwargs):
        print("*" * 15)
        func(*args, **kwargs)
        print("*" * 15)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 15)
        func(*args, **kwargs)
        print("%" * 15)
    return inner


# way -1 
# @star
# @percent
# def printer(msg):
#     print(msg)


# way -2
def printer(msg):
    print(msg)
printer = star(percent(printer))

printer("Hello")
printer("sarvesh")


import collections
 

Student = collections.namedtuple('Student', ['name', 'age', 'DOB'])
 

S = Student('Nandini', '19', '2541997')
 

print("The Student age using index is : ", end="")
print(S[1])

print("The Student name using keyname is : ", end="")
print(S.name)
 

print("The Student DOB using getattr() is : ", end="")
print(getattr(S, 'DOB'))


# named tuples 

from collections import namedtuple
 
Point = namedtuple('Point', ['x', 'y'])
p = Point(x=1, y=2)
print(p.x, p.y)


keys = set()



data_list = [
    {'key1': 1, 'key2': 2},{'key1': 3 , 'key2': 4}
]
for d in data_list: 
    for key in d.keys(): 
        keys.add(key)

print(keys)


# struct =  namedtuple('Struct',sorted())


# python modules 

import math 

print(math)

junk =  math 

b = junk is math

print(b)


import sys 

print(sys.prefix, sys.exec_prefix)



# from fibo import fib as fibonacci
# print(fibonacci(500)) 



# import sys 

# print(sys.ps1)

import fibo
print(dir(fibo)) 





