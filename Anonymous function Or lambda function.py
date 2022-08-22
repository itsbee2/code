def  show(x):
    print (x)
show(5) 

show = lambda x: print(x)
show(5)

# Multiple value:
add_sub = lambda x,y : (x+y, x-y)
a , s = add_sub(5,2)
print (a)
print (s)  





