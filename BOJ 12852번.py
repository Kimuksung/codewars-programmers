import sys
input = sys.stdin.readline

N = int ( input() )

arr = [1000001] * (N)
S = [0] * (N)
arr.append(0)

answer = [1]

for i in range ( N , 0 , -1 ) :
    if arr[i] + 1 < arr[i-1] :
        S[i-1] = i
        arr[i-1] = min (arr[i-1] , arr[i] + 1)
    
    if i%2 == 0:
        if arr[i] + 1 < arr[i//2] :
            S[i//2] = i
        arr[i//2] = min (arr[i//2] , arr[i] + 1)
        
    if i%3 == 0:
        if arr[i] + 1 < arr[i//3] :
            S[i//3] = i
        arr[i//3] = min (arr[i//3] , arr[i] + 1)
        
while ( answer[-1] != N ) :
    answer.append(S[answer[-1]])

answer = list ( reversed ( answer ) )

print (arr[1])
[ print(i) for i in answer ]
