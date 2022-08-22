# Dsfault Argument
def show (name, age =27):
    print (name, age)
show (name= "geeky shows" ,age= 65) 

# variable length Argument 
def add (*num):
    z= num [0]+ num[1] + num[2]
    print (z)
    print("Addition:",z)
add (5,4,2)    

# keyword variable length Argument 
def add (**num):
    z= num['a']+num['b']+num['c']
    print ("Addition:",z)
add (a=5,b=2,c=4)    






