# 프로그래머스 풍선 터트리기
def solution(a):
    answer = 0
    n = len(a)
    left_dp = [0]*n
    right_dp = [0]*n
    
    # left
    min_value = 1000000000
    for i in range(n):
        min_value= min(min_value,a[i])
        left_dp[i]=min_value
    
    # right
    min_value = 1000000000
    for i in range(n-1,-1,-1):
        min_value= min(min_value,a[i])
        right_dp[i]=min_value
        
    for data,left,right in zip(a,left_dp,right_dp):
        if data>left and data>right :
            continue
        answer+=1
        
    return answer