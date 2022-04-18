# BOJ 2164번

from collections import deque

card = deque()
n = int(input())

[ card.appendleft(i) for i in range( 1, n+1 ) ]

while ( len(card) != 1) :
    card.pop()
    card.appendleft( card.pop() )

print ( card[0] )