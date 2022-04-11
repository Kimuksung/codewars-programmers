# 위상 정렬
# 기존의 그래프를 사용
# Indgree의 값을 보고 판단
'''
7 7
A B
D B
C B
C D
D E
E F
G E
'''
import sys
from collections import deque
input = sys.stdin.readline

n , m = map ( int , input().split() )
adj = [ [] for _ in range( m ) ]
indgree = [0]*m
queue = deque()
answer = []

for _ in range( n ) :
    start , end = map ( str , input().split() )
    adj[ord(start)-65].append(ord(end)-65)
    indgree[ord(end)-65] += 1

for index , graph in enumerate(indgree) :
    if not graph :
        queue.append(index)

while ( queue ) :
    temp = queue.popleft()
    answer.append(chr(temp+65))
    for data in adj[temp] :
        indgree[data] -= 1
        if not indgree[data] :
            queue.append(data)

print (answer)