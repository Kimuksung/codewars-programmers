def solution(dartResult):
    answer = 0
    stack = []
    char_data = ''
    for dart in dartResult :
        if dart.isdigit() :
            char_data += dart
        elif dart == 'S':
            stack.append( int (char_data) )
            char_data = ''
        elif dart =='D' :
            stack.append( int (char_data) * int (char_data) )
            char_data = ''
        elif dart == 'T':
            stack.append( int (char_data) * int (char_data) * int (char_data) )
            char_data = ''
        elif dart == '*':
            temp = stack.pop()
            temp2 = 0
            if stack != [] : 
                temp2 = stack.pop()
                stack.append(temp2 * 2)
            stack.append(temp*2)
        elif dart == '#' :
            temp = stack.pop()
            stack.append(temp * -1)
    return answer

solution( '1D2S3T*' )