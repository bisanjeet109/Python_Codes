# COUNTING SUBSTRINGS FROM A STRING----------
# COUNT()
# STRING.COUNT(substring)
s1 ="we are learning python.python is fun"
s2 ="python"
print(f"occurence of {s2} is {s1.count(s2)}")    # it checks how many times the word is repeated in the sentence



# check particular letters instead of words,u can search anything in the sentence from comas to spaces
s1 ="we are learning python.python is fun"
s2 ="n"
print(f"occurence of {s2} is {s1.count(s2)}")


#changing case of a string
#upper(),lower(),title(),capitalize()
s1="pYthon is fun"
print(s1.upper())
print(s1.lower())
print(s1.title())       # it makes all the starting leter of the words capital
print(s1.capitalize())        # IT MAKES ONLY THE STARTING OF THE SENTENCE CAPITAL

# STARTING AND ENDING----------
#startwith()
#string.startwith(substring)
print(s1.startswith("d"))        # both of them checks whwther it starts or end with exact same word oor not
print(s1.endswith("n"))