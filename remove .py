from array import*
stu_roll = array ('i', [101,102,101,104,105])
n = len (stu_roll)
i = 0 
while (i<n):
    print (stu_roll[i])
    i+=1
print ("Array after Remove ")
stu_roll.remove (101)
n = len (stu_roll)
i = 0
while (i<n):
    print(stu_roll[i])
    i+=1    


from array import*
stu_roll = array ('i',[101,102,101,103,104,105])
print (stu_roll.index(104))    