def func(a,b=2, *args,d): 
    print(*args)

func(1,3,34,45,d=2)

# **kargs ->keyword arguments
def func1(*args,**kargs):
    print(args,kargs)


func1(1,2,a=2,b=3)



def cal_avg(*args,log_to_console=False):
    hi =int(bool(args)) and max(args)
    lo =int(bool(args)) and min(args)
    avg = (hi + lo)/2
    if log_to_console:
        print("high={0}, low={1} , avg={2}".format(hi,lo,avg))
    return avg



def func3(a,b=2,*args,c=10,d): 
    print(a,b,args,c,d)

func3(10,20,'x','y','z',c = 4, d = 1)
func3(10,20,'x','y','z',d = 10)
func3(1,'x','y','z', d = 10) 

cal_avg(2,3,log_to_console=True)

print(1,2,3,sep='-')

# powers of a number 

import time 
def time_it(fn,*args,rep=1,**kargs):
    start = time.perf_counter()
    for i in range(rep): 
        fn(*args,**kargs)
    end =  time.perf_counter()
    return  (end - start)/rep


time_it(print, 1, 2, 3 , sep ='-',end = ' ***\n', rep = 5 )


def power_of_2(n,*,start = 1,end): 
    return list((n**i for i in range(start,end)))

time_it(power_of_2,n=2,start =0 ,rep =5,end = 20000)

def power_of_one(n,*,start = 1,end): 
    results = []
    for i in range(start,end): 
        results.append(n**i)
    return results

print(power_of_one(2,end=5))

def power_of_three(n,*, start = 1, end): 
    return [n**i for i in range(start,end)]
    
print(power_of_three(3, end = 5) )


def power_of_four(n,*,start=1,end): 
    return [n**i for i in range(start,end)]

print(power_of_three(4, end = 20))


from datetime import datetime 


def log(msg,*,dt=datetime.utcnow()):
    print('{0}:{1}'.format(dt,msg))


log('message 1')


def add_item(name,quantity, unit,grocery_list): 
    grocery_list.append("{0}({1} {2})".format(name,quantity,unit))
    return grocery_list

store1 = []
store2 = []

add_item('banana',2,'units',store1)
add_item('guava',3,'units',store1)
add_item('strawberry',5,'units',store1)

print(store1)


def factorial(n): 
    if n<1:
        return 1
    else:
        print('Calculating {0}!',format(n))
        return n*factorial(n-1)

print(factorial(6))

# cache 


def factcah(n,*,cache):
    if n<1:
        return 1
    else: 
        print('Calculating {0}!'.format(n))
        result = n* factcah(n-1,cache = cache)
        cache[n] = result
        return result
    

cache = {}


print(factcah(4,cache=cache)) 


print(cache)
 
