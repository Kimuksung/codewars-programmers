def sum_pairs(ints, s):
    check_data = set()
    for data in ints :
        #print ( data , s-data , s , check_data)
        if data in check_data :
            return [ s-data , data  ]
        check_data.add( s- data)
    return None

print ( sum_pairs ( [1, 4, 8, 7, 3, 15] , 8) )