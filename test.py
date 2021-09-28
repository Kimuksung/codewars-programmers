from functools import reduce
sum = 0
n = 3
start = 2 * reduce ( lambda x , y : x+y , [i for i in range(n)] ) + 1 
add = reduce ( lambda x , y : x + y , [2*i for i in range(0,n)])

print ( n * start + add )
