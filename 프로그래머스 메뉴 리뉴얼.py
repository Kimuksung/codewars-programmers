from itertools import combinations
# idea 
# 1. 각각의 course 내에 있는 것으로 combination 후 갯수 세기

orders = ["XYZ", "XWY", "WXA"]
courses = [2,3,4]

answer = []
for course in courses :
    temp = dict()
    for order in orders :
        for data in list( map( ''.join , list ( combinations ( order , course) )  ) ) :
            data = ''.join( sorted ( data ) )
            if data in temp :
                temp[data] += 1 
            else :
                temp[data] = 1

    answer.extend ( [k for k,v in temp.items() if v == max(temp.values()) and v>1] )

print ( sorted( answer , reverse=False ) )
    
