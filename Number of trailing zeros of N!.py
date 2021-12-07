def findTrailingZeros(n):
    # Negative Number Edge Case
    if(n < 0):
        return -1
 
    # Initialize result
    count = 0

    while(n >= 5):
        n //= 5
        count += n
 
    return count
 
print ( findTrailingZeros(25) )