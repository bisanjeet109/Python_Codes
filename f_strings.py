name="guddu"
age=22
language="python"
hours=3
#now print guddu is 22 years old .he studies python 3 hours a day
print(name,"is",age,"years old.","he studies",language,hours,"hours a day")



#doing this again and again is hectic so
#fstring concept is introduced
print(f"{name} is {age} years old.he studies {language} {hours}hours a day.")
# here for the concept or the use of fstring we write the code as i had done but before all after the double quotes we should assign or write   f    so the the compiles understands.


# lets take an example
sub1=78
sub2=87
sub3=83
print(f"{name} scored  {sub1+sub2+sub3} total marks.")
percent=(sub1+sub2+sub3)/3
print(f"{name} got {round(percent,2)}%.in exams")  #here i used the round to round of the numbers after decimal to 2 digits.
