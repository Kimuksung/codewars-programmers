def solution(s):
    for i in s :
        print ( i , ord ( i ))
    answer =  ''.join( sorted ( s , key = lambda x : ord(x) )[::-1])
    return answer

print ( solution('Zbcdefg') )