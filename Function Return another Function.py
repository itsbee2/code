def disp():
    def show ():
        return "show function"
    print ("disp function")
    return show 

r_show = disp()
print (r_show())         