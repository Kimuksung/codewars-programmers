# BOJ 11328번

import sys
input = sys.stdin.readline

n = int( input() )
for _ in range ( n ) :
    word_a , word_b = map( str , input().split() )
    word_a = sorted(word_a)
    word_b = sorted(word_b)
    
    if word_a == word_b :
        print ( 'Possible')
    else :
        print ( 'Impossible')
    
