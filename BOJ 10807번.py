# BOJ 10807번
import sys
input = sys.stdin.readline

cnt = 0
n = int ( input() )
num_list = map ( int , input().split() )
target = int( input() )

for num in num_list :
    if target == num :
        cnt += 1
        
print ( cnt )