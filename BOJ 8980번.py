#BOJ 8980번
import sys
input = sys.stdin.readline

answer = 0
n , weight = map(int,input().split())
k = int(input())
box = [weight]*(n+1)

datas = sorted( [ list( map(int,input().split()) ) for _ in range(k) ] , key = lambda x :x[1] )

for data in datas :
    move = min( data[2] , min(box[data[0]:data[1]]) )
    for j in range( data[0] , data[1] ) :
        box[j] -= move
    answer += move

print(answer)