#BOJ 1158번

n , k = map( int , input().split() )
num_list = [i for i in range( 1 , n+1) ]
start = 0
answer = []

for _ in range( n ):
    start += k-1
    if start >= len(num_list) :
        start = start%len(num_list)

    answer.append ( str( num_list[start] ) )
    num_list.pop(start)

print ( '<' + ', '.join(answer) + '>')