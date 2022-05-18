#BOJ 1822번

import bisect
import sys
input = sys.stdin.readline

n , m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a.sort() , b.sort()
answer = []

for target in a :
    if b[-1] < target :
        answer.append(target)
        continue
    index = bisect.bisect_left( b ,target)
    if b[index] == target :
        continue

    answer.append(target)

if not answer :
    print(0)
    exit()

print(len(answer))
print(*answer)