def solution(s):
    answer = False
    number = [ '0' , '1' , '2', '3' ,'4','5','6','7','8','9']
    n = len ( s )
    if n not in [4,6] :
        return answer
    
    for i in s :
        if i not in number  :
            return answer
    return True