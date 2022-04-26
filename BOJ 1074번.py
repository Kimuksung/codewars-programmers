#BOJ 1074번

# Idea 재귀를 이용하여 계속하여 탐색
# 좌표가 2 ^ (n-1) 보다 큰지 여부를 통해 좌표 탐색
n , r , c = map ( int , input().split() )
answer = 0

def recursion ( n , r , c ) :
    global answer
    if n == 1 : # 종료조건
        answer += 2*r+c
        return

    devide_x , devide_y = 0,0
    if r >= 2**(n-1) :
        devide_x = 1
    if c >= 2**(n-1) :
        devide_y = 1

    answer += ( devide_x*2+devide_y )*2**( 2 *(n-1) )
    if devide_x :
        r = r - 2**(n-1)
    if devide_y :
        c = c - 2**(n-1)

    recursion ( n-1 , r , c )

recursion ( n , r , c)
print ( answer )