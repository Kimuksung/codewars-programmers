def solution ( datas , n ) :
    temp = [0] * 100
    
    for data in datas : # N
        if temp[100-data] != 0 :
            return True
        temp[data] += 1

    return False
    
print ( solution ( [1,52,48] , 3 ) )
print ( solution ( [50,42] , 2 ) )