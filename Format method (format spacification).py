# Integer
print ("{num:5d}".format(num=15))
print ("{num:05d}".format(num=15))
print ("{num:+5d}".format(num=15))
print ("{num:<5d}".format(num=15))
print ("{num:*<5d}".format(num=15))
print ("{num:*>5d}".format(num=15))
print ("{num:^5d}".format(num=15))

# float
print ("{num:8f}".format(num=15.62))
print ("{num:8.3f}".format(num=15.65))
print ("{num:+8.2f}".format(num=15.65))
print ("{num:<8.2f}".format(num=15.65))
print ("{num:*<8.2f}".format(num=15.65))
print ("{num:*>8.2f}".format(num=15.65))
print ("{num:^8.2f}".format(num=15.65))

# String 
print ("{:8s}".format("Ankush"))
print ("{:<8}".format("Ankush"))
print ("{:*<8}".format("Ankush"))
print ("{:>8}".format("Ankush"))
print ("{:*>8s}".format("Ankush"))
print ("{:^8s}".format("Ankush"))

# Truncating String 
print ("{:.3s}".format("Bittu"))
print ("{:8.3}".format("Bittu"))
print("{:*<8.3}".format("Bittu"))
print ("{:>8.3}".format("Bittu"))
print ("{:*>8.3s}".format("Bittu"))
print ("{:^8.3s}".format("Bittu"))