#BOJ 17219번

import sys
input = sys.stdin.readline

n , m = map(int,input().split())
login = dict()

for _ in range(n) :
    id , pw = input().split()
    login[id] = pw

for _ in range(m) :
    id = input().rstrip()
    print(login[id])
