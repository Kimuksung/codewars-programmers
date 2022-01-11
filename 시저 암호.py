def solution(s, n):
    answer = ''
    for data in s :
        temp = ord(data)
        if data == ' ' :
            answer += ' '
        
        elif temp >= 97 :
            temp += n
            if temp > 122 :
                temp = temp % 123 + 97
            answer +=  chr(temp)
            
        else:
            temp += n
            if temp > 90 :
                temp = temp%91 + 65
            answer +=  chr(temp)
            
    return answer