print("*************first code**************")
a = "%s" % (432)
print (a)
print (type(a))

print("**************Second******************")
b = ("%(nm)s%(ag)d"% {"ag":432,"nm":"geekyshow"})
print(b)
print(type(b))

print("**************Thrid code***************")
print("%d"%432)
print("%d+d"%432)

print("*************Four code******************")
C = ("%f"%432.123)
print(C)
print(type(C))
print ("%.3f"% 432.123)
