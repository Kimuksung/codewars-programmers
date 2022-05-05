#BOJ 1181번

import sys
import heapq
input = sys.stdin.readline

datas = set()
n = int(input())
for _ in range ( n ) :
    char_data = input().rstrip()
    datas.add ( (len(char_data) , char_data ) )

datas = list( datas )
heapq.heapify ( datas )

while datas :
    print ( heapq.heappop(datas)[1] ) 