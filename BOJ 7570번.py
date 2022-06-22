#BOJ 7570번

n = int(input())
datas = list(map(int,input().split()))

dp = [0]*(1000001)
# 최적의 선택을 통하여 맨 앞 맨 뒤로 이동시켜 순서를 유지하기 위해서는 정렬된 순서로 있어야 한다.
# 특히 연속되게
for data in datas :
    dp[data] = max(dp[data] , dp[data-1]+1)

print( n-max(dp) )