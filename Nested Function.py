# Nested Fuction
def disp():
    def show():
        print ("show function")
    print ("Disp Function")
    show()
disp()

# OR
def disp():
    def show ():
        return "show fuction"
    result = show() + " Disp Function"
    return result     
a = disp()
print (a)        

