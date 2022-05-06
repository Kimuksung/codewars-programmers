#BOJ 2750번

n = int (input())
data = []

for _ in range( n ) :
    data.append( int(input() ) )

data.sort()

print(*data)