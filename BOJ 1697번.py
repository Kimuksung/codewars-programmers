from collections import deque

N , M = map ( int , input().split() )

if N == M :
    print (0)
    exit(0)
subin , sister = [0] * 100001 , [0] * 100001
move = [-1 , 1 , 2]

que = deque()
que.append( [ N , 0 ] )

while ( que ) :
    #print ( que )
    #print ( subin[:10])
    x , num = que.popleft()
    change_x = subin[x] + 1
    for i in range ( 3 ) :
        if i == 2 :
            nx = x * 2
        else :
            nx = x + move[i]
        
        if nx == M :
            print ( change_x )
            exit(0)

        if 0 <= nx <= 100000  and subin[nx] == 0 :
            que.append ( [nx,change_x])
            subin[nx] = change_x


        


