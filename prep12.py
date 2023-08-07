p1 = {  
    "employee": {  
        "name":       "sonoo",   
        "salary":      "56000",   
        "married":    "true "
    }  
}   


print(p1)


# import yaml 


# data = '''

# ---
# # A list of tasty fruits
# - Apple
# - Orange
# - Strawberry
# - Mango
# ...

# '''


# d=yaml.load(data)


# print(d)



import serpy

class Foo(object):
   
    y = 'hello'
    z = 9.5

    def __init__(self, x):
        self.x = x


class FooSerializer(serpy.Serializer):
    
    x = serpy.IntField()
    y = serpy.Field()
    z = serpy.Field()

f = Foo(1)
FooSerializer(f).data


fs = [Foo(i) for i in range(100)]
FooSerializer(fs, many=True).data
# [{'x': 0, 'y': 'hello', 'z': 9.5}, {'x': 1, 'y': 'hello', 'z': 9.5}, ...]


Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'} 
print("Dictionary:") 
print(Dict)
print(Dict[1])


from collections import OrderedDict
 

od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
for key, value in od.items():
    print(key, value)
 

od['c'] = 5
for key, value in od.items():
    print(key, value)


from collections import Counter

a = [12, 3, 4, 3, 5, 11, 12, 6, 7]
 
x = Counter(a)
 
print(x)

for i in x.keys():
      print(i, ":", x[i])

x_keys = list(x.keys())
x_values = list(x.values())
 
print(x_keys)
print(x_values)



import collections

dic1 = { 'a' : 1, 'b' : 2 }
dic2 = { 'b' : 3, 'c' : 4 }

chain = collections.ChainMap(dic1, dic2)

print ("All the ChainMap contents are : ")
print (chain.maps)

print ("All keys of ChainMap are : ")
print (list(chain.keys()))
  

print ("All values of ChainMap are : ")
print (list(chain.values()))


class Base:
    def __init__(self):
        self.a = "GeeksforGeeks"
        self.__c = "GeeksforGeeks"
 
# Creating a derived class
class Derived(Base):
    def __init__(self):
 
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self.__c)
 
 
# Driver code
obj1 = Base()
print(obj1.a)