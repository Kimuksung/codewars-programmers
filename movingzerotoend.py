def move_zeros(array):
    cnt = 0
    answer = []
    for data in array:
        if data != 0:
            answer.append(data)
        else:
            cnt += 1
    for i in range(cnt) :
        answer.append( 0 )
    return answer

print ( move_zeros ( [1, 2, 0, 1, 0, 1, 0, 3, 0, 1] ))
'''
array = [1, 0, 1, 2, 0, 1, 3]
cnt = 0
print ( 
list ( map ( lambda x , y : x if x != 0 else y += 1, array ) ) 
)
#else cnt = cnt + 1 
'''