# 스티커 붙일 수 있는지 여부
def paste_note ( x , y , maps , page_maps ) :
    R , V = len( page_maps ) , len( page_maps[0] )
    for i in range ( R ) :
        for j in range ( V ) :
            if maps[x+i][y+j] == 1 and page_maps[i][j] == 1 :
                return False
    
    # 스티커 붙이기                
    for i in range ( R ) :
        for j in range ( V ) :
            if page_maps[i][j] == 1 :
                maps[x+i][y+j] = 1
    return True
    

# X , Y -> Y , N - 1 - X
def Roate90( maps ) :
    N , M = len(maps) , len ( maps[0] )
    new_maps = [ [0] * N for _ in range (M)]

    for i in range ( N ) :
        for j in range ( M ) :
            if maps[i][j] == 1 :
                new_maps[j][N-1-i] = 1
    
    return new_maps , len(new_maps) , len ( new_maps[0] )

#solution
N , M , K = map( int , input().split(' ') ) 
maps = [ [0] * M for _ in range (N)]

for _ in range ( K ) :
    page_N , page_M = map ( int , input().split(' ') )
    page_maps = [ [0] * page_M for _ in range ( page_N ) ]

    for i in range ( page_N ) :
        commands = list ( map ( int,  input().split(' ') ) )
        for j in range( page_M ) :
            page_maps[i][j] = commands[j]
    

    
    #data checking
    # 0 , 90 , 180 , 270
    try :
        for i in range(4) :
            # 1.스티커의 가로 , 세로보다 커야댄다.
            if not ( N >= page_N and M >= page_M ):
                page_maps , page_N , page_M = Roate90(page_maps)
                continue
            # 2. 붙일 수 있는지 여부
            for x in range ( N - page_N + 1 ) :
                for y in range ( M - page_M + 1 ) :
                    if paste_note ( x , y , maps , page_maps ) :
                        raise NotImplementedError

            page_maps , page_N , page_M = Roate90(page_maps)
    except:
        pass

#print ( '-' * 10)
#[ print ( map ) for map in maps ]   

print ( sum ( [1 for i in range ( N ) for j in range ( M ) if maps[i][j] ] ) ) 

