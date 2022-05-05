#BOJ 11931번

import sys
input = sys.stdin.readline

datas = [False] * 2000001
n = int(input())

for _ in range( n ) :
    datas[int(input()) + 1000000] = True
  
for i in range ( 2000000 , -1 , -1 ) :
    if datas[i] :
        print(i-1000000 )