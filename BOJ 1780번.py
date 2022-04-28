# BOJ 1780번

n = int ( input () )

maps = [ [0] * n for _ in range ( n ) ]
minus_one_cnt , plus_one_cnt , zero_cnt = 0 , 0 , 0 

for i in range ( n ) :
    for j , value in enumerate ( input().split() ) :
        maps[i][j] = int(value)

def answer ( x , y , n ) :
    global minus_one_cnt , plus_one_cnt , zero_cnt
    check_data = maps[x][y]

    for i in range ( x , x+n ) :
        for j in range ( y , y+n ) :
            if maps[i][j] != check_data :
                answer( x , y , n //3 )
                answer( x , y + n//3 , n //3 )
                answer( x , y + (n*2) // 3 , n //3 )
                answer( x + n//3, y , n //3 )
                answer( x + n//3, y + n//3 , n //3 )
                answer( x + n//3 , y + (n*2) // 3 , n //3 )
                answer( x + (n*2) // 3, y , n //3 )
                answer( x + (n*2) // 3, y + n//3 , n //3 )
                answer( x + (n*2) // 3, y + (n*2) // 3 , n //3 )
                return

    if check_data == -1 :
        minus_one_cnt += 1
    elif check_data == 1 :
        plus_one_cnt += 1
    else :
        zero_cnt += 1

answer(0,0,n)
print ( minus_one_cnt , zero_cnt , plus_one_cnt )