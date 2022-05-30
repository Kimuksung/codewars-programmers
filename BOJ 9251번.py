#BOJ 9251번

A = input()
B = input()

len_A , len_B= len(A) , len(B)
dp = [[1]*len_A for _ in range(len_B)]

#init
for i in range(len_A) :
    if A[i] != B[0] :
        dp[0][i] = 0
    else :
        break

for i in range(len_B) :
    if B[i] != A[0] :
        dp[i][0] = 0
    else:
        break

for i in range(1,len_B) :
    for j in range(1,len_A) :
        if B[i]==A[j] :
            dp[i][j] = max(dp[i-1][j] , dp[i][j-1] , dp[i-1][j-1]+1)
        else :
            dp[i][j] = max(dp[i-1][j] , dp[i][j-1])

print(dp[len_B-1][len_A-1])