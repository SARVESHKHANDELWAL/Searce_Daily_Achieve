# Serialization and dE

# Serializes
import pickle
from typing import Any
f=open("pickled.txt","wb")
dct={"name":"Rajeev", "age":23, "Gender":"Male","marks":75}
# Pickle to file 
pickle.dump(dct,f) 
f.close()


# deserializes
f=open("pickled.txt","rb")
# Unpickle the file 
d=pickle.load(f)
print (d)
f.close()



# Pickling convert the python object into a character stream 
 
import pickle 


ser = pickle.dumps("My name is Sarvesh Khandelwal")

print(ser)

deser = pickle.loads(ser)

print(deser)

d1 = {'a' :1 , 'b' : 2}
d2 = {'c' : 3, 'b' : 5}

d1_ser = pickle.dumps(d1)
d2_ser = pickle.dumps(d2)


del d1 
del d2 

d1 = pickle.loads(d1_ser)
d2 = pickle.loads(d2_ser)

print(d1,d2)


class  Person: 
    def __init__(self,name,age): 
        self.name =  name 
        self.age =   age 
    
    def __eq__(self, other): 
        return self.name == other.name and self.age == other.age 
    
    def __repr__(self): 
        return f'Person(name={self.name},age={self.age})'
    

john  = Person("sarvesh", 21)
erun = Person("Wow", 24)



fav_peps ={
    'title': 'think of for india',
    'actors': [john,erun]
}


print(fav_peps)


ser1 = pickle.dumps(fav_peps)
print(ser1)



# Json Serialization

import json 
d1_jsonser = json.dumps(d1)


print(d1_jsonser)



d2_new = json.loads(d1_jsonser)

print(d2_new)

print(d1== d2_new  , d2_new is d1)


e = {'a' : (1,2,3)}


ser = json.dumps(e)

print(ser)



de_ser = json.loads(ser)


print(de_ser)


class  Person1: 
    def __init__(self,name,age): 
        self.name =  name 
        self.age =   age 
    
    def __repr__(self): 
        return f'Person(name={self.name},age={self.age})'
    
    def toJSON(self): 
        return dict(name=self.name,age = self.age)
    
p = Person1('john', 27) 

print(p.toJSON())


# to return the dict we use dump method 

print(json.dumps({'john': p.toJSON()}, indent= 2))


import json
 

data = {
    "user": {
        "name": "satyam kumar",
        "age": 21,
        "Place": "Patna",
        "Blood group": "O+"
    }
}

with open( "datafile.json" , "w" ) as write:
    json.dump( data , write )


from datetime import datetime 
current = datetime.utcnow()

print(json.dumps(str(current)))


def format_iso(df): 
    return df.strftime('%Y-%m-%dT%H:%M:%S')
print(format_iso(current))



log_record = {
    'time' : datetime.utcnow(), 
    'messgae' : 'testing'
}
print(json.dumps(log_record,default=format_iso))


class  Person2: 
    def __init__(self,name,age): 
        self.name =  name 
        self.age =   age 
        self.create_dt = datetime.utcnow()
    
    def __repr__(self): 
        return f'Person(name={self.name},age={self.age})'
    
    def toJSON(self): 
        return {
            'name': self.name, 
            'age' : self.age, 
            'create_dt' : self.create_dt.isoformat()
        }
    

p1 = Person2('Sarvesh',21)



print(p1.toJSON)




def custom_json_fromatter(arg): 
    if isinstance(arg,datetime):
        return arg.isoformat()
    elif isinstance(arg,set): 
        return list(arg)
    else: 
        try:
            return arg.toJSON()
        except AttributeError: 
            try: 
                return vars(arg)
            except TypeError:
                return str(arg)
            


# def_coder =  json.JSONEncoder()
# def_coder.encode(1,2,3)


# class CustomJSONEncoder(json.JSONEncoder):
#     def default(self,arg): 
#         if isinstance(arg,datetime):
#             return arg.isoformat()
#         else:
#             return super.default(arg)

# custom_encoder = CustomJSONEncoder()

# print(custom_encoder.encode([1,2,3]))


d = {
    'name': 'Sarvesh', 
    'age' : 27, 
    'created_by' : 'Chirag Gupta',
    'list' : [1,2,3]
}



print(json.dumps(d,indent = '-----'))




