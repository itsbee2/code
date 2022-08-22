def show(a):
    print (a(8))
show (lambda x:x)    

# Returing lambda function
def add ():
    y = 20
    return(lambda x:x+y)

a = add()
print (a(10))  

