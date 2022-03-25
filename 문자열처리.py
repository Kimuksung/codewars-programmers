#n = 9 
arr = [ i+1 for i in range(12) ]

def sosu ( n ) :
    if n == 1 :
        return 1
    for i in range( 2 , n ) :
        if i*i > n :
            break
        if n % i == 0 :
            return i
    return 1

def change_data ( arr ) :
    n = len(arr)
    p = sosu ( n )
    answer = []

    if p == 1 :
        return arr
    temp = [0]*n

    for index , value in enumerate ( arr ) :
        temp[index%p * n//p + index//p] = value

    for i in range ( index%p + 1) :
        #answer.extend ( change_data ( temp[(n//p)*i:(n//p)*(i+1)] )  )
        for data in change_data ( temp[(n//p)*i:(n//p)*(i+1)] ) :
            answer.append( data )
    return answer

print ( change_data( arr) )