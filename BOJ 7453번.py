#BOJ 7453번
import bisect
import sys
input = sys.stdin.readline

answer = 0
n = int(input())
A , B , C , D = [] , [] , [] , []
AB , CD = dict() , dict()

for _ in range(n) :
    a,b,c,d = map(int,input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

for a in A :
    for b in B :
        if a+b not in AB :
            AB[a+b] =1
        else :
            AB[a+b] +=1
for c in C :
    for d in D :
        if -(c+d) in AB :
            answer += AB[-(c+d)]
print(answer)