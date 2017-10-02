'''
The password generator will take the length of password (always greater than 3) and output a random password containing at least:
       1. An Aphabet( either lowercase or uppercase) 
       2. A number. 
    
       3. A special character. 

The postion of all these characters will also be random i.e. the number might be the first to come. 
Constraints: 
The length of password is at least 3 and maximum will be 100.

'''
from random import choice,sample

l=0
while l<3 or l>100 or int(l)!=l:
    l=int(input('Enter password length (an integer between 3 and 100)\n'))

num=list(range(48,58))
char=list(range(65,91))+list(range(97,123))
spec=list(range(33,39))+list(range(60,65))+list(range(91,96))+list(range(123,126))
all=num+char+spec

passw=[choice(num),choice(char),choice(spec)]

while len(passw)<l:
    passw.append(choice(all))
passw=sample(passw,l)
password=''
for i in range(l):
    password+=chr(passw[i])
print('This is your password: ',password)
