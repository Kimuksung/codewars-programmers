N = int ( input() )

#Counting sort
arr = [0] * ( 2000001 )
for i in range( N ) :
    temp = int ( input() )
    temp += 1000000
    arr[temp] += 1

#print ( '-' * 10)
for i in range( 2000001 ) :
    while arr[i] :
        print ( i - 1000000 )
        arr[i] -= 1
    #if arr[i] != 0 :
        #for j in range( arr[i] ) :
            #print ( i - 1000000 )
