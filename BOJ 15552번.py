#BOJ 15552번
import sys
input = sys.stdin.readline

n = int(input())
answer = []
for _ in range( n ) :
    first , second = map( int , input().split())
    answer.append( first+second )

print ( *answer )