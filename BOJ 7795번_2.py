#BOJ 7795번

import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n) :
    answer = 0
    A , B = map ( int ,  input().split() )
    A_num = list(map ( int , input().split() ) )
    B_num = list(map ( int , input().split() ) )
    A_num.sort() , B_num.sort()
    B_num_len , B_index= len(B_num) , 0
    
    for index ,value in enumerate( A_num ) :
        while True :
            if B_index >= B_num_len :
                answer += B_index
                break
            elif value <= B_num[B_index] :
                answer += B_index
                break
            B_index += 1

    print ( answer )