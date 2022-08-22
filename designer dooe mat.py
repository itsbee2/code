a = int ()
b = int ()
x = int ((a-1)/2)
y = int ((b-7)/2)
for i in range (x,0,-1):
    for j in range (3*i):
        print (end="-") 
    for j in range (2*(x-1)+1):
        print (end=".|.")
    for j in range (3*i):
        print (end="-")
    print()
for j in range (1,2):
    for j in range (y):
        print(end="-")
    for j in range (1):
        print(end="WELCOME" )
    for j in range (y):
        print(end="-")
    print() 
for i in range (1,x+1):
    for j in range (3*i):
        print (end="-") 
    for j in range (2*(x-1)+1):
        print (end=".|.")
    for j in range (3*i):
        print (end="-")
    print()    
    