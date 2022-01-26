# N 부터 1 까지 재귀로 출력하기

def recursive ( N ) :
    if N == 0 :
        return 0
    return N + recursive(N-1)
  
def solution ( ) :
    a = recursive ( 5 )
    print ( 'sum : ' , a )

solution()