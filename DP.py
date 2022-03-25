students , k = [1] , 1

result = 0
n = (len(students) )
arr = [[0] * (k+1) for _ in range (n)]

if students[0] == 0 :
    arr[0][0] = 1 
else : 
    arr[0][1] = 1
    
for index in range( 1 , n ):
    if students[index] == 0 :
        arr[index][0] = arr[index-1][0] + 1
        for i in range( 1, k+1 ) :
            arr[index][i] = arr[index-1][i]
    for i in range( 1, k ) :
            arr[index][i] = arr[index-1][i]
    else :
        arr[index][0] = 0
        for i in range( 1, k+1 ) :
            arr[index][i] = arr[index-1][i-1]
        arr[index][1] += 1

print ( arr )