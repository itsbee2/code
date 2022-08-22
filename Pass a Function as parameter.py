# Pass a Function as parameter
def disp (sh):
    print ("Disp Function" + sh())

def show ():
    return " Show function"

disp(show)    
