# 첫번째 별을 기준으로는
n = int( input() )

maps = [[' '] * n*2 for _ in range(n) ]

def fill_star ( x, y ) :
    maps[x][y] = '*'
    maps[x+1][y-1] , maps[x+1][y+1] = '*' , '*' 
    for i in range( y-2 , y+3) :
        maps[x+2][i] = '*'

def recursion ( x, y , n ) :
    if n== 3 :
        fill_star ( x,y)
        return
    
    recursion ( x , y , n//2 )
    recursion ( x+n//2 , y-n//2 , n//2 )
    recursion ( x+n//2 , y+n//2 , n//2 )
    
recursion ( 0,n-1,n)

[ print ( ''.join( map ) ) for map in maps ]