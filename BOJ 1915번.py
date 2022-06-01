#BOJ 1915번

answer = 0
n , m = map(int,input().split())
maps = [[0]*m for _ in range(n)]
dp_maps = [[0]*m for _ in range(n)]

for i in range(n) :
    for j,data in enumerate(input()) :
        if data == '1' :
            maps[i][j] = 1
    
for i in range(n) :
    for j in range(m) :
        if maps[i][j]== 1:
            if 0 <= i-1 < n  and 0<= j-1 < m :
                dp_maps[i][j] = min(dp_maps[i][j-1] , dp_maps[i-1][j-1] , dp_maps[i-1][j])+1
            else :
                dp_maps[i][j] = maps[i][j]

        answer = max(dp_maps[i][j] , answer )
        
print(answer*answer)