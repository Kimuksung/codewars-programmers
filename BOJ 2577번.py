# BOJ  2577번

import sys
input=sys.stdin.readline
number_list = [0] * 10
a = int(input())
b = int(input())
c = int(input())

temp = str( a*b*c )
for i in temp :
    number_list[int(i)] += 1

print ( *number_list )