# Python provides three different modules which allow us to serialize and deserialize objects :  

# Marshal Module
# Pickle Module
# JSON Moduleimport marshal 
 
import marshal 
 
data = {'name': 'sunny','age': 34,'address': 'nasik'}

bytes = marshal.dumps(data)   
print('After serialization : ', bytes)
 

new_data = marshal.loads(bytes)   
print('After deserialization : ', new_data)

d = dict(zip('abc',range(1,4)))

print(len(d),d.get('python'))



s ="When above code is executed, the dictionary object's byte representation will be stored in 'pickled.txt' file. The file must have 'write and binary' mode enabled."


counts = dict()
for c in s:
    counts[c] = counts.get(c,0) + 1
print(counts)

counts.pop('W')



if 'z' not in counts: 
    counts['z'] = 1000

print(counts)



d.setdefault('z',100)

print(d)


import string 
from itertools import chain 

def cat_key(c): 
    cat_1 = {' ':None}
    cat_2 = dict.fromkeys(string.ascii_lowercase,'lower')
    cat_3 = dict.fromkeys(string.ascii_uppercase, 'upper')
    categories  = dict(chain(cat_1.items(),cat_2.items(),cat_3.items()))

    return categories.get(c, 'other')


print(cat_key('a'),cat_key('A'))


# iterables onject for d.keys(), d.values(), d.items()

s1 = {'a','b','b','c'}

s2 = {'c','c','d'}



# s3 = s1 | s2
# s3 = s1 & s2


d1 = {'a': 1,'b': 2,'c': 3} 
d2 = {'b' : 4, 'f' : 6 , 't': 9}
s3 = s1 - s2

# for x in s3: 
#     print(x) 


union  = d1.keys() | d2.keys()

for x  in union:
    print(x)

intersection  = d1.keys() & d2.keys()
for y  in intersection: 
    print(x)

from functools import reduce
 
# lst1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
# lst2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]
 
# intersection = reduce(lambda acc, x: acc + [x] if x in lst2 and x not in acc else acc, lst1, [])
 
# print(intersection) 


dd = {'a': 1 , 'b' : 2}

dd.update(c = 30, x = 40, b = 20 )

for x,y in dd.items():
    print(x,y)

