# Programmes-코딩 테스트 공부

import sys
def solution(alp, cop, problems):
    answer = sys.maxsize
    max_x,max_y=max(list(map(lambda x:x[0],problems))),max(list(map(lambda x:x[1],problems)))
    dp = [[sys.maxsize] *(251) for _ in range(251)]
    dp[alp][cop]=0

    problems = sorted(problems,key=lambda x:(x[0],x[1]))
    for i in range(251):
        dp[i][0]= min(dp[i][0],dp[i-1][0]+1)
    for j in range(251):
        dp[0][j]= min(dp[0][j],dp[0][j-1]+1)
        
    for i in range(1,251):
        for j in range(1,251):
            # 1. 알고력 증가 / 코딩력 증가
            dp[i][j] = min(dp[i][j],dp[i-1][j]+1,dp[i][j-1]+1) 
            
            # 2. 문제 있는 경우로 단축 시킬 수 있는 경우
            for problem in problems :
                if i>=problem[0]+problem[2] and j>=problem[1]+problem[3]:
                    dp[i][j]= min( dp[i][j], dp[i-problem[2]][j-problem[3]]+problem[4] )
            if i>=max_x and j>=max_y :
                answer=min(answer,dp[i][j])

    return answer