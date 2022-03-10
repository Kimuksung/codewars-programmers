import sys
input = sys.stdin.readline
n = int(input())

arrs = []
cnt = 0
answer = 0

[arrs.append( int(input()) ) for _ in range(n)]
arrs.sort( reverse= True)

for arr in arrs :
    cnt += 1
    answer = max ( answer , cnt * arr )

print(answer)
