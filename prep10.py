# n=10_000_000

# s=set(range(n))
# l=list(range(n))
# t=tuple(range(n))



# # def test_set(s,value):
# #     return value in s

# # def test_list(l,value):
# #     return value in l


# # def test_tuple(t,value): 
# #     return value in t

# # import timeit

# # print(timeit('test_set(s,value)',globals = globals(),number=10_000))
# # print(timeit('test_list(l,value)',globals = globals(),number=10_000))
# # print(timeit('test_tuple(t,value)',globals = globals(),number=10_000))



# s = {'a',300,(1,2)}
# print(type(s))

# # d = set(1,2,3)

# s.add(4)
# s.remove((1,2))

# for x in s: 
#     print(x)

# # methods -> s1.intersection(s2) -> s2 could be an interable 
# # operators -> s1 & s2 both must be sets 


# r = {(1,2)}.intersection([(1,2),(3,4)])


# for x  in r: 
#     print(x) 


# s1 =  {1 , 2 , 3} 
# s1.update([3,4,5], (6,7,8), 'abc')


# for x in s1: 
#     print(x) 


# def combine(string,target): 
#     target.update(string.split(' '))


# def fun_generator():
#     yield "Hello world!!"
#     yield "Geeksforgeeks"
 
 
# obj = fun_generator()
 
# print(type(obj))
 
# print(next(obj))
# print(iter(obj))


# def inf_sequence():
#     num = 0
#     while True:
#         yield num
#         num += 1
         
# for i in inf_sequence():
#     print(i, end=" ") 



# Frozen Sets 
# Sallow copy 
s1 = frozenset([1,2,3])
s2 = frozenset(s1)


print(s1 is  s2)



s1 = {1,2,3}
s2 = set(s1)

print(s1 is s2)

from copy import deepcopy

s2 = deepcopy(s1)

print(s1 is s2) 


s1 =frozenset('ab') 
s2 = {1,2}
s3 = s1 | s2 

s4 = s2 | s1 


print(s4)


import copy

li1 = [1, 2, [3,5], 4]
 

li2 = copy.copy(li1)
 

print ("The original elements before shallow copying")
for i in range(0,len(li1)):
    print (li1[i],end=" ")
 
print("\r")
 

li2[2][0] = 7
 

print ("The original elements after shallow copying")
for i in range(0,len( li1)):
    print (li1[i],end=" ")

