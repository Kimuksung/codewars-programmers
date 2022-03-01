#Idea
# 짝수 인경우 : 가장 뒤에 있는 0을 1로
# 홀수 인경우 : 가장 뒤에 있는 0을1로 후 그 뒤의 1을 0으로 바꾼다.

def solution(numbers):
    answer = []
    
    for n in numbers :
        n = int(n)
        num_bit = list ( '0' + bin(n)[2:] )
        if n % 2 == 0 :
            for index in range( len(num_bit)-1 , 0-1 , -1 ):
                if num_bit[index] == '0' :
                    num_bit[index] = '1'
                    break
        else :
            for index in range( len(num_bit)-1 , 0-1 , -1 ):
                if num_bit[index] == '0' :
                    num_bit[index] = '1'
                    num_bit[index+1] = '0'
                    break
        answer.append ( int ( ''.join( num_bit ) , 2 ) )

    return answer

print ( solution( [7] ) )