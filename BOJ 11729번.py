# 귀납적 사고법 가지기
# 아이디어 : a에서 b로 가는데 n-1개로 간다
# 1,2,3 3개니 나머지 하나의 기둥은 6-a-b

n = int ( input() )
def solution ( a , b , n ) :
    # 종료 조건
    if n == 1 :
        return print ( a , b)
    solution ( a, 6-a-b , n-1)
    print ( a, b )
    solution ( b , 6-a-b , n-1)


solution ( 1 , 3 , n )