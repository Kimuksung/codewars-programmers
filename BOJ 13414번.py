#BOJ 13414번
import sys
input = sys.stdin.readline
cnt , n = map(int,input().split())

student = dict()
for i in range(n) :
    student[input().rstrip()] = i

[print(data[0]) for data in list( sorted(student.items() , key=lambda x:x[1]))[:cnt] ]