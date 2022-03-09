student , k = [0,1,0,0,1,1,0] , 3

n = len(student)
arr = [0] * (n+1)
answer = 0

for index , value in enumerate( student ) :
    arr[index+1] = arr[index] + value

print ( arr )

for i in range ( 1, n+1 ) :
    for j in range ( i , n+1 ) :
        if arr[j] - arr[i-1] == k :
            answer += 1

print ( answer )