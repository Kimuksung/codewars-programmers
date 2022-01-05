def solution(a, b):
    answer = ['THU' ,'FRI' , 'SAT' ,'SUN' , 'MON','TUE' , 'WED']
    month = [0,31,29,31,30,31,30,31,31,30,31,30,31]

    n = ( sum(month[:a]) + b ) % 7
    return answer[n]

print ( solution(1,1) )
print ( solution(1,2) )
print ( solution(5,24) ) # 화
print ( solution(9,30) ) # 금
print ( solution(10,1) ) #토
