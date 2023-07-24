import random 


print(random.random())

l= [1,2,3]
sorted(l, key = lambda x : random.random())


print(l)

# functions re first class objects  -> they have __doc__ and __annotations__


def my_fun(a,b):
    return a + b

my_fun.cat = "sarvesh"
my_fun.name = "arth"

print(my_fun.cat)


# functional arguments 
def func(a, b= 1, *args,**kargs): 
    i =10
    b = min(i,b)
    return a*b

print(func.__code__.co_varnames)
print(func.__code__.co_argcount)

from inspect import *
import inspect 
print(isfunction(my_fun))

print(inspect.signature(my_fun).parameters.values())

class Myclass: 
    def f(slef): 
        pass


# print(isfunction(func))
# print(ismethod(func))

print(isfunction(Myclass))

sig = inspect.signature(my_fun)

for k,v  in sig.parameters.items():
    print(k,type(v))


print(divmod(4,3))
for param in inspect.signature(divmod).parameters.values():
    print(param.kind)

# print(x.first)

# callables 


str ="weqeqds"
print(callable(print))
print(callable(str.upper))
print(callable(print))


# high order function  -> function take parameter as function 

# map (func, *iterables)

l = [1,2,3]



    
r= map(lambda x : x*x,l)

# for x  in r: 
#     print(x)


l1 = [20,30,41]


r1 = map(lambda x,y:x+y,l,l1)


# for x in r1 :
#     print(x)

# filter function 

def iseven(x):
    return x%2 == 0

ans = list(filter(iseven,l1))


for x in ans:
    print(x)


l2 = ['a','b','c','d']


re = list(zip(l,l1,l2))


# for x in re: 
#     print(x)




l3 = range(10)

# for x in l3: 
#     print(x)

both = list(filter(lambda y : y<101,map(lambda x: x**2,l3)))


# for y in both: 
#     print(y)


c = list(filter(lambda x : x%3 == 0, range(25)))


# for x in c: 
#     print(x)


def fact(x):
    if(x<=1):
     return 1
    return x*fact(x-1)
results = [fact(n) for n in range(10)]


results1 = [ x + y for x,y in zip(l,l1)]

# for x in results1:
#     print(x)

# for x in results1: 
#     print(x)


# reducting functions 

max_value= lambda a,b : a if a>b else b

def max_seq(l):
    maxa = l[0]
    for x in l[1:]:
        maxa = max(x,maxa)
    return maxa


print(max_seq(l3))



from functools import reduce

maxa = reduce( lambda a,b : a if a>b else b , l1)

maxa1 = reduce( lambda a,b : a if a>b else b , "dwdwcxsxwqsxz")


print(maxa,maxa1)

# reduce func also have third para as initlizaer


sum = reduce(lambda x,y : x + y,l1)
sum1 = reduce(lambda x,y : x + y,l1,1000)
print(sum,sum1)



# reducing functions arguments 

def c(a,b,c):
    return a + b + c

def w(a,b):
    return c(1,a,b)



print(w(10,10))




# partails 

from functools import partial 

f = partial(c , 10)



print(f(20,200))


def pow(base,exp):
    return base ** exp 


sq = partial(pow,exp =2)
cube = partial(pow, exp=3)

print(sq(5),cube(5))

li = [(0,2),(9,10),(1,5),(5,6),(7,8),]

dist2 = lambda a,b : (a[0] - b[0])**2+ (a[1] - b[1])**2

print(dist2(li[0],li[1]))
origin = (0,0)

f = partial(dist2,origin)




li = sorted(li, key = f)



for x,y  in li : 
    print(x,y,)



# operator module 


import operator 
# print(dir(operator))



print(operator.add(34321,13213))

e = [1,2,3,4,5,2,3,4]

print(operator.indexOf(e, 2)) 



z = 100

def check():
    global z 
    z = 121
    print(z)



check()



def outer():
    x = "hello"

    def inner1(): 
        def inner2():
            
            x = 'python'
            
        inner2()
       
    print(x)
    inner1()
   

outer()



def outer(): 
    global x
    x = 'month'

    def inner(): 
        # global x
        x = 'hello'
    print(x)


# functions defined inside the other function an access he outer variables 

def outer(): 
    x = 'python' 

    def inner(): 
        print("{0} rocks!!".format(x))
    
    return inner()


outer() 

# multi scope variables 

def outer():
    x = "python"
    def inner(): 
        print(x)
    return inner

def counter(): 
    count = 0

    def inc1(): 
        nonlocal count
        count+=1
        return count
    
    def inc2(): 
        nonlocal count
        count+=1
        return count
    
    return inc1,inc2


# f1 = counter()
# f2 = counter()



# print(f1)
# print(f2)

adders = []
x =0
for n in range(1,4): 
    adders.append(lambda x : x + n)



print(adders[1](10))

print(adders[0][10])


def itemgetter(*items):
    if len(items) == 1:
        item = items[0]
        def g(obj):
            return obj[item]
    else:
        def g(obj):
            return tuple(obj[item] for item in items)
    return g 


def create_address(): 
    adders = []
    for n in range(1,4): 
        adders.append(lambda x,y = n : x + y)
    return adders



adders = create_address()

print(adders)

print(adders[0].__closure)


# Python closure is a nested function that allows us to access variables of the outer function even after the outer function is closed. 

