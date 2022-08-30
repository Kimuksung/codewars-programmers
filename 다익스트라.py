# 다익스트라
import sys
graphs = [[1,2,3],[1,3,2],[1,4,5],[2,3,2],[2,5,8],[3,4,2],[4,5,6],[5,6,1]]

#init
start = 1
n = 6
table = [sys.maxsize]*(n+1)
visited = [0]*(n+1)

table[start]=0
visited[start]=1
visited[0]=1
node = [[] for _ in range(n+1)]

#graph
for st,ed,value in graphs :
    node[st].append((ed,value))

for i in range(n-1):
    # 최단 거리 Table 갱신
    for end,value in node[start]:
        table[end] = min( table[start]+value , table[end] )

    index = sorted( [ (index,table[index]) for index,visit in enumerate(visited) if not visit ] , key = lambda x:(x[1],x[0]) )[0][0]
    visited[index]=1
    start=index
    print(i,table,visited)

