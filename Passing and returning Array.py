# Passing & returning Array:
from array import*
def show (ar):
    print("Passing Array ar:",ar)
    print (type(ar))
    for i in ar:
        print (i)
    return ar
a = ("i",[101,102,103,104]) 
y = show (a)
print ("Returning Array y:",y)
print (type(y))
for i in y:
    print (i)   