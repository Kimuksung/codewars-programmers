def solution(s1 , s2):
    if s1 == '' and s2 == '':
        return False

    for s1_data in s1: 
        temp = s2.find(s1_data)
        if temp != -1:
            s2 = s2[:temp] + s2[temp+1:]
    print(s2)
    if s2 == '':
        return True
    else:
        return False

print ( solution('rkqodlw', 'world') )
