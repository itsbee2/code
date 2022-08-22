def prime_number(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True


n = 97
print(prime_number(n))