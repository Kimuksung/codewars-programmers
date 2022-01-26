def data_check ( n ) :
    n = n - 1
    return n

def data_check2 ( arr ) :
    arr[0] = 0
    return arr

def data_check3 ( arr ) :
    arr = [1,2,3]
    return arr

def solution ( ) :
    data = 5
    data2 = [5,4,3,2,1]
    data3 = [5,4,3,2,1]
    data_check ( data )
    data_check2(data2)
    data_check3(data2)
    print ( data )
    print ( data2 )
    print ( data3 )
    
solution()