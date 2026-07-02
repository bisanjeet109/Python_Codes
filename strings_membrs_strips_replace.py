s1="python is love"
print(s1*3)      #in string "*" is repetation operatior

# membership operation--------- in this we use ( in ) keyword
print("i love " in s1)     #false

print("love" in s1)       #true  love is present in the s1




# (not in )-----
print("i love " not in s1)       # TRUE--here in (not in) it gives true when the line is not present

print("love" not in s1)          #FALSE---here in (not in) it gives false when the line is present



# comparision of strrings---------       it checks the value
print("python"==" python")      # there should be no space otherwise it will give error




# REMOVING SPACES FROM A STRING ----STRIP()------------!
s1="guddu                         "
s2=s1.strip()
print(s2)
print(s1.strip()=="guddu")      # BY usng this strip it removes the space so it shows true when comparing both the same words



# REPLACE FUNCTION--------replace()
s1="we are learning python"
print(s1)
print(s1.replace("python","java"))
print(s1)   # it will not print the replaced one ,it is replacing not reassigning


# example 2---------
s1="we are learning python"
print(s1)
print(s1.replace("e","E",3))     # it will change all the e present in the line
print(s1)

#if u want to change only one e then write (1) or (2)