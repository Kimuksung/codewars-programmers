#BOJ 12015번
import sys
import bisect
input = sys.stdin.readline
# LIS 이분탐색
n = int(input())

datas = list(map(int,input().split()))
dp = [datas[0]]

for data in datas :
    if data > dp[-1] :
        dp.append(data)
    else :
        dp[bisect.bisect_left(dp , data)] = data

print( len(dp) )