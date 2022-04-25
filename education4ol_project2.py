import random
import array
import re

'''
Name= Anand Bharti
Intern ID: 4045
'''
#Enter the length  of the Password
MAX_LEN=int(input('Enter the length of Password'))
temp_pass=[]
flag = 0
#Taking Words as a input from user
for i in range(MAX_LEN):
    temp_pass.append(input())
#shuffleing given words to generatre a random passeord
random.shuffle(temp_pass)
password = ""
for x in temp_pass:
		password = password + x
print('Your Password is:',password)
# you can enter your own txt file address for saving the assress
file_name=r'C:\Users\Anand Bharti\Documents\PWD.txt'
text_file=open(file_name, 'w')
#write password to the txt file
text_file.write("Your Password is",password)
text_file.close()
#Checking if the Password is Strong
'''
Password Must have 
lenth should be 8
1-Uppercasse Alphabet 
1-Lowercase Alphabet
1-Number
1-Symbol(_@$)
'''
if (len(password)<8):
    flag = -1
    print("Minimum Lenth should be 8")

if not re.search("[a-z]", password):
    flag = -1
    print("Include at Least one lower case alphabet")

if not re.search("[A-Z]", password):
    flag = -1
    print("Include at least one UPPER case alphabet")
if not re.search("[0-9]", password):
    flag = -1
    print("Include at least one Number")
if not re.search("[_@$]", password):
    flag = -1
    print("Include at least one symbol")
if re.search("\s", password):
    flag = -1
if (flag == 0):  
    print("Password is Strong")  
else:
    print("Password is Not Strong ")
