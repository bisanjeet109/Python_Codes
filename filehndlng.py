"""
  1-file handling is a way of to create delete and modify a file that can store a group of values.
  with the use of file handling processes we can read,write and modify the contents of a file.
 2- for python the 3 major steps for file handling are
   A-open the file
   B-process the file i.e perform read and write operations
   C-close the file
usually a file provides nodes for diff operations

mode           use                          description
r           read only default             set file pointer at the beginoing of the file
r+          read and write                set file pointer at the begining of the file
w           write only                    overwrites existing data.otherwise creates a new file.
w+          write and read                overwrites existing data.otherwise creates a new file.for both reading and writting
a           append only                   adds data to the end.otherwise creates a new file.
a+          append and read               set file pointer at the end of the file.otherwise creates a new file.for both reading and writting

"""
#programs---------------------------------------------
"""
f=open("MCA-VIT.txt",'a+')
print(f.closed)
print("name of the file is ",f.name)
f.close()
print(f.closed)




f=open("MCA-VIT.txt",'w')
line1="this is mca batch 2025"
f.write(line1)
line2="\n we are learning python"
f.write(line2)
f.close()

f=open("MCA-VIT.txt",'r')
text=f.read()
print(text)
f.close()
"""

#questian
#wap to create a file name my pat processes.inside the file,write the name of the companies that interview u have already attended,as well as write the name of cources that u r completing for the pat process.close the file and open it again in the read mode to display the details

"""
f=open("MY_PAT_PROCESSES",'w')
line1="NAME OF THE COMPANIES"
f.write(line1)
Line2="\n HSBC,NETAPP"
f.write(Line2)
Line3="\n i am not elligible in any of the companies"
f.write(Line3)
f.close()

f=open("MY_PAT_PROCESSES",'r')
text=f.read()
print(text)
f.close()    """
"""
f=open("a.txt","r+")
line1="apple \t"
f.write(line1)
line2="\n we are learning file handling "
f.write(line2)
f.close()

f=open("a.txt","r")
text=f.read()
print(text)
f.close()

f=open("a.txt","w")
line1="banana \t"
f.write(line1)
line2="\n we are learning file handling "
f.write(line2)
f.close()

f=open("a.txt","r")
text=f.read()
print(text)
f.close()
"""
"""
f=open("a.txt",'a+')
print(f.closed)
print("name of the file is ",f.name)
f.close()
print(f.closed)
f=open("a.txt","r+")
line1="To,\n "
line2="The Director,\n "
line3="sub:\tLeave for one day\n"
line4="respectfully"
f.write(line1)
f.write(line2)
f.write(line3)
f.write(line4)
f.close()
f=open("a.txt","r")
text=f.read()
print(text)
f.close()

"""
""" 
1.readline([size]):Read no of char from file if size is mentioned till eof.
                   it reads till new line character.
                   it returns empty strings on eof.
2.readlines([size]):read no of lines from file if size is mentioned or all contents if size is not mentioned.             
   """

#frist program-------------
"""
f=open("MCA-VIT.txt",'a+')
print(f.closed)
print("name of the file is ",f.name)
f.close()
print(f.closed)

f=open("MCA-VIT.txt",'w')
line1="this is the first line"
f.write(line1)
line2="\nthis is the second line"
f.write(line2)
f.close()
f=open("MCA-VIT.txt",'r')
#text=f.readline()
#print(text)
#text=f.readline()
#print(text)
f.close()

#open the activatiop file and displqay the statemeents line by line.display only first 3 lines.
f=open("MCA-VIT.txt",'r')
text=f.readlines(24)
print(text)
f.close()"""

#wap to  input your name class dob and the current cgpa.
#using the readlines function display the output till your name only
f=open("MCA-VIT.txt",'a+')
print(f.closed)
print("name of the file is ",f.name)
f.close()
print(f.closed)
"""
f=open("MCA-VIT.txt",'w')
line1=input("write your name")
f.write(line1)
line2=input("your class:")
f.write(line2)
line3=str(input("write the dob"))
f.write(line3)
line4=str(input("write your cgpa"))
f.write(line4)
f.close()
print(f.closed)
f=open("MCA-VIT.txt",'r')
text=f.readline(4)
print(text)

#text=f.readline()
#print(text)
f.close()
"""


#text.split functions--------------------------------------------
"""
f=open("MCA-VIT.txt",'w')
for text in f.readlines():
    for word in text.split(  "i want to go home" ):
       
        print(word)
f.close()
print(f.closed)

"""

#open the personal details file and write all the personal details
#done in upp

"""
getting & resetting the file position
1-tell(): it tells us the current position within the file.
2-seek(offset[,from]):it changes the current file posistion.if from is 0

the tell  and seek function works with binary conditions with files.to read the binary values we should a very specisl file mode
rb+---read binary value mode.as the cursor is the binary value to read its position we requires rb+ mode
"""
#questian------------
#open the personal details file and display first 20 char
#,check the correct cursor position and display all the vlues present in the files with the current position.........

#os.rename
"""
remove()
mkdir()create the directory in the current directory
chdir() method to change the current directory
getcwd() method displays the current directory
rmdir() method delete the directory



"""



