# Accessing Array
from array import*
stu_roll = array ('i', [101,102,103,104,105])
for el in stu_roll:
    print (el)
n = len (stu_roll)
print (n) 

# range 
n1 = len (stu_roll)
range (n1)
print (n1)

# loop
n1 = len (stu_roll)
for i in range (n1):
    print (stu_roll[i])

# Index
for i in range (n):
    print ("Index",i,"=",stu_roll[i])