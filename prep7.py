# Python program to explain os.path.join() method

# importing os module
import os

# Path
path = "/home"

# Join various path components
print(os.path.join(path, "User/Desktop", "file.txt"))


# Path
path = "User/Documents"

# Join various path components
print(os.path.join(path, "/home", "file.txt"))

# In above example '/home'
# represents an absolute path
# so all previous components i.e User / Documents
# are thrown away and joining continues
# from the absolute path component i.e / home.


# Path
path = "/User"


print(os.path.join(path, "Downloads", "file.txt", "/home"))


# Path
path = "/home"


print(os.path.join(path, "User/Public/", "Documents", ""))



# Importing the package
import importlib

# Function to import module at the runtime
# def dynamic_import(module):
# 	return importlib.import_module(module)

# if __name__ == '__main__':

# 	custom = input("Enter module name: ")


# 	module = dynamic_import(custom)
	

# 	print(module.__name__)
# 	print(module.__doc__)
# 	print(dir(module))
    
from importlib import resources

with resources.open_text("texts", "sample.txt") as t:
    txt = t.readlines()
  
# Printing the contents of file
print("".join(txt[:7]))


print("hello in cpp")

# Associative array 
# Hash map 

def h(key,num_slots):
	return len(key)%num_slots

print(h('sarvesh',11))


def h(key,num_slots):
	total = sum(ord(c)for c in key)
	return total%num_slots

print(h('sarvesh',11))


print(hash("sarvesh"))


# Immutable objects can be hashable 
# Mutable objects can't be hashable 

d ={}
for i in range (1,10): 
	d[i] = i**2
	
for x,y in d.items(): 
	print(x,y)
	
t1 = (1,2,3)
t2 = (1,2,3)



print(hash(t1) == hash(t2))
print(id(t1) == id(t2))

d = {'a' : 100 , 'b' : 2000}

d1 = d


print(d1)


print(d is d1)


print(d1['a'] and d['a']  == 1 )

import math
print(math.hypot(1,1))



x_cords = [1,2,3,4,5]
y_cords = [3,4,5,6,7]

grid = [(x,y)
	   for  x in x_cords
       for y in y_cords]

for x,y in grid:
	print(x,y)
	
# grid_extended = [((x,y): math.hypot(x,y) for x,y in grid)]

# for x,y,z in grid_extended:
# 	print(x,y,z)

