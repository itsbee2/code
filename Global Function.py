a = 50
def show ():
    a = 10
print ("local variable:A",a)
x = globals() ["a"]
print ("x:", x)
show ()
print ("Global variable:B",a)
