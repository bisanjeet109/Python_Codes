d1={"nine":9,"seven":7,"eight":8}
print(d1)
 #allowed----- (immutable Datatyppes)
#inteeger can be keys
# float are also allowed as keys
#boolean ares also allowed
#tuples are aALLOWED as the keys

        #not allowed-------------------------------(mutable)
           #list are not allowed as the keys
           #sets are not allowed as  keys
           #a dictionary cannot be a key of another dictonary



                  # keys can only be immuatble datatypes------------=

student1={'id':1001,'name':'john','marks':{'maths':88,'eng':98,'chem':45}}
print(student1['marks']['eng'])    #using indexing we can  find each part

#fetch only the keys----------------
#keys()---------------------------
print(student1.keys(),type(student1.keys()))
#values()--------------------------
print(student1.values(),type(student1.values()))
#items-------------------------------
print(student1.items(),type(student1.items()))