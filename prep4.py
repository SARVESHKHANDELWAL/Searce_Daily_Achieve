# HOF - High Order Functions  -> Take argument as function and can also return function.
# annotations 
def my_func(a:str,b=2): 
    return a*b

print(my_func("sarvesh"))

print(my_func.__annotations__)
print(my_func.__doc__)



x = 5 
y = 3
def func(a):
    return a*max(x,y)



print(func(5))


# def my_func(a: str,b:'int > 0'=1, *args: 'some extra postional args', k1: 'keyword -only agr 1', k2: 'key 2'=100, **kargs: 'some extra arguments key-words args'):
#     print(a,b,args,k1,k2,**kargs)


lambda x: x**2 
lambda x,y :  x + y
lambda : 'hello'
lambda s: s[::-1].upper()



funcl = lambda x: x**2 



#passing a func as argument 
def apply_func(x,fn): 
    return fn(x)

print(apply_func(4,funcl))



xyz = lambda y : y*3
def st(y):
    print(xyz(y))


st("sarvesh")

g = lambda x,y=10:x + y

print(g(4,5))
print(g(5))



f = lambda x,*args,y,**kargs : (x,args,y,kargs)
print(f(10,1,2,y=100, a= 20 , b=33443))


def apply_func(fn,*args,**kargs): 
    return fn(*args,**kargs)

print(apply_func(lambda x:x**2,45))


print(apply_func(lambda *args: sum(args), 1,2,3,4))



# sorting

l = ['a','e','q','S','Y']

print(sorted(l))
print(sorted(l,key=lambda s : s.upper()))

# sorted(l,key=lambda s : s.upper())


d = {'c':1 ,'b': 2, 'a': 3}

for a,b in d.items(): 
    print(a,b)


print(sorted(d,key = lambda e : d[e]))



def dist(x):
    return (x.real)**2 + (x.imag)**2




r = [12 + 1j,1 + 1j,2,6 + 7j]

# sorted(r,key = dist)
sorted(r,key = lambda x : (x.real)**2 + (x.imag)**2)

print(sorted(r,key = lambda x : (x.real)**2 + (x.imag)**2))


l = ['Cleese','Gilliam','Jones','Idle']

print(sorted(l,key = lambda  s : s[-1]))






# print(dist(1 + 3j))


