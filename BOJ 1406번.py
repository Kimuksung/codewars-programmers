#BOJ 1406번
# Idea1. 문자열 나열 뒤 값이 지정하려하였으나 500000이라는 크기 때문에 시간 복잡도 초과
# Idea2. stack으로 나타내어 O(N) -> O(1) 로 처리
import sys
input = sys.stdin.readline

word = list ( input().strip() )
stack = []

n = int(input())
for _ in range ( n ) :
    data = list ( map( str , input().split() )  )
    if data[0] == 'L' and word:
        stack.append(word.pop())

    if data[0] == 'D' and stack :
        word.append(stack.pop())

    if data[0] == 'B' and word :
        word.pop()

    if data[0] == 'P' :
        word.append( data[1] )

while stack :
    word.append(stack.pop())
print ( ''.join( word ) )