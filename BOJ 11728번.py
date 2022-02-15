from collections import deque
N , M = map(int , input().split(' ') )
N_list = deque ( map(int , input().split(' ') ) )
M_list = deque ( map(int , input().split(' ') ) )

answer = []
while ( N_list and M_list ) :
    if N_list[0] > M_list[0] :
        answer.append(M_list[0])
        M_list.popleft()
    else :
        answer.append(N_list[0])
        N_list.popleft()

if N_list :
    answer.extend(N_list)

if M_list :
    answer.extend(M_list)

[ print ( data ) for data in answer ]