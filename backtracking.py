# backtracking
# 재귀적인 구조를 이용하여 모든 경우의 수를 추적

# 기본 형태
arr_list = []
move_list = [1,2,3,4]

def backtracking ( cnt ) :
    if cnt == 5 :
        print( *arr_list )
        return

    for move in move_list :
        arr_list.append(move)
        backtracking(cnt+1)
        arr_list.pop()

backtracking( 0 )
        