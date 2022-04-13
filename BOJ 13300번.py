# BOJ 13300번

import sys
input = sys.stdin.readline

students = [[0,0] for _ in range( 6 )]
answer = 0

n , k = map( int , input().split() )
for _ in range( n ) :
    sex , age = map( int , input().split() )
    students[age-1][sex] += 1

for student in students :
    for data in student :
        if not data :
            continue
        if data % k :
            answer += data//k +1
        else :
            answer += data//k

print ( answer )
