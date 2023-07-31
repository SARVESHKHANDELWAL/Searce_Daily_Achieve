conf_dev ={
    'host': 'localhost',
    'user': 'test', 
    'pwd' : 'test'
}

conf_prod = {
    'host': 'prodz@searce.com',
    'user' : '@prod_user',
    'pwd' : '$prod_pwd', 
    'database': 'deeptive_prod'
}

conf = {**conf_dev, **conf_prod}

for x,y in conf.items():
    print(x,y)

d = {'a' : [1,2] , 'b' : [3,5]} 

d['a'].append(100)


for x,y in d.items(): 
    print(x,y)



class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

  def __hash__(self): 
     return hash(self.name)

p1 = Person("John", 36)
p1.myfunc()


p1.age = 40 
# del p1.age 

print(p1.name) 
print(p1.age)

p2  = p1


print(p2 == p1)

import pickle
print(pickle.HIGHEST_PROTOCOL,pickle.DEFAULT_PROTOCOL)


import marshal
person={"name":"Krishna", "age":22, "marks":[45,56,78]}
data=marshal.dumps(person)
obj= marshal.loads(data)
print (obj)
string = """
a=10
b=20
print ('multiplication=',a*b)
"""
code = compile(string, "script", "exec")
f=open("marshal.pyc","wb")
marshal.dump(code, f)
f.close()
import json
data=['Rakhee',{'marks':(50,60,70)}]
s=json.dumps(data)
print(s)


data={"marks":50, "age":20, "rank":5}
s=json.dumps(data, sort_keys=True)
print(s)

