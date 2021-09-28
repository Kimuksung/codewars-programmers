import math 

def gcd(a, b):
    while (b != 0):
        temp = a % b
        a = b
        b = temp
    return abs(a)

def is_prime(num):
    if num in [ 0 , 1]:
        return False
    for i in range ( 2, int ( math.sqrt(num) ) + 1):
        if gcd( i , num ) != 1:
            return False
    return True

print ( is_prime(8) ) 
