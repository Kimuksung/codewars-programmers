#BOJ 1744번

import heapq

answer = 0
n = int(input())
plus_q = []
minus_q = []

for _ in range(n) :
    temp = int(input())
    if temp > 0 :
        heapq.heappush( plus_q , -1*temp )
    else :
        heapq.heappush( minus_q , temp )

len_plus_q = len(plus_q)
len_minus_q = len(minus_q)

while len_plus_q >= 2 :
    first , second = -1*heapq.heappop(plus_q) , -1*heapq.heappop(plus_q)
    multiple , plus = first*second , first+second
    if multiple > 0 and multiple > plus :
        answer += multiple
    else :
        answer += plus
    len_plus_q -= 2

for q in plus_q :
    answer += -1*q 
    
while len_minus_q >= 2 :
    first , second = -1*heapq.heappop(minus_q) , -1*heapq.heappop(minus_q)
    multiple , plus = first*second , first+second
    if multiple >= 0 :
        answer += multiple
    len_minus_q -= 2

for q in minus_q :
    answer += q 

print(answer)