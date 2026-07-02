"""
a dict is a special type of composite datatype that can contain
two values for a single item.
these two values are
1--key value
2--data value

1----------------
a key is an identifier for an data valuue
all the keysb available in the dictionary are immutable
while the data values attached with the key are mutable
a dict is defined with curly brackets
2nd~ the key and its data are defined by colon
3rd ~~ multip[ple of key and data are sepereted with a coma

"""

d={
    "key01":"value01",
    "India":"delhi",
    "uk" : "london"
}
print(d)
print(d.keys())
print(d.values())
print(d.items())



 #methods runs only in dictionary

"""
clear() removes all the elements from the dictionary
copy() Returns a copy of the dictionary
fromkeys()returns a dict with the specified 
get()
items()
keys()
pop()
popitem()
setdefault()
update()
values()
"""
