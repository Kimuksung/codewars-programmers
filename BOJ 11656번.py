#BOJ 11656번

import sys
input = sys.stdin.readline

data = input().rstrip()
answer = []

for i in range( len(data) ) :
    answer.append(  data[i:]   )

answer.sort()
[ print ( answers ) for answers in answer ]