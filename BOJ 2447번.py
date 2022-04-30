#BOJ 2447번
n = int( input() )

maps = [ ['*']*n for _ in range(n) ]

def recursion( x , y , n ) :
    if n == 1 :
        return
    
    medium = n//3
    for i in range( x+medium , x+2*medium ) :
        for j in range( y+medium , y+2*medium ) :
            maps[i][j] = ' '
    recursion ( x , y , medium)
    recursion ( x , y+medium , medium)
    recursion ( x , y+2*medium , medium)
    recursion ( x+medium , y , medium)
    recursion ( x+medium , y+medium , medium)
    recursion ( x+medium , y+2*medium , medium)
    recursion ( x+2*medium , y , medium)
    recursion ( x+2*medium , y+medium , medium)
    recursion ( x+2*medium , y+2*medium , medium)

recursion(0,0,n)

[print( ''.join(map )) for map in maps]