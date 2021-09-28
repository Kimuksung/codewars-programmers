def solution(s1 , s2):
    if s1 == '' and s2 == '':
        return False
    s1 = ''.join(sorted(s1))
    s2 = ''.join(sorted(s2))
    #print (s1 , s2)
    for s2_data in s2:
        print(s1 , s2 )    
        temp = s1.find(s2_data)
        if temp == -1:
            return False
        s1 = s1[:temp] + s1[temp+1:]

    return True

print ( solution('rnowothbrqpqrdgnx', 'kefbaiwnjo') )
