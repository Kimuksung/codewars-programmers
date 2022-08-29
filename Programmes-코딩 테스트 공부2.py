# Programmes-코딩 테스트 공부2
import sys
def solution(alp, cop, problems):  
    #Init
    max_x,max_y=max(list(map(lambda x:x[0],problems))),max(list(map(lambda x:x[1],problems)))
    dp = [[sys.maxsize] *(max_y+1) for _ in range(max_x+1)]
    # why? DP 값 범위가 max_x,max_y 인데 이것보다 크게 설정되면 index error
    alp = min(alp,max_x)
    cop = min(cop,max_y)
    dp[alp][cop]=0
    
    # DP
    # x의 범위 max_x+1 ? 4,4가 타겟이라고 한다고 할 때 3,3 에서 만약 +5,+5해주는 게 있다면 이게 더 빠르니 적용해주어야함 
    for i in range(alp,max_x+1):
        for j in range(cop,max_y+1):
            # 1. 코딩력 증가
            if j+1<=max_y:
                dp[i][j+1] = min(dp[i][j]+1, dp[i][j+1])
            # 2. 알고력 증가
            if i+1<=max_x:
                dp[i+1][j] = min(dp[i][j]+1, dp[i+1][j])
            
            for start_x,start_y,nx,ny,time in problems :
                if i>= start_x and j>=start_y:
                    dx,dy=i+nx,j+ny
                    if dx>max_x:
                        dx=max_x
                    if dy>max_y:
                        dy=max_y
                    
                    dp[dx][dy] = min(dp[dx][dy],dp[i][j]+time)
                
    return dp[-1][-1]

problems=[[0,0,2,1,2],[2,3,2,1,4],[6,13,2,2,2]]
alp,cop=10,10

print( solution(alp, cop, problems) ) 
