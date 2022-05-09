#BOJ 10814번

import sys
input = sys.stdin.readline

n = int( input() )
age_list = [[] for _ in range(201) ]

for _ in range(n) :
    age , name = map(str , input().split())
    age_list[int(age)].append( name )

for index , values in enumerate( age_list ) :
    if values :
        for value in values :
            print( index , value )