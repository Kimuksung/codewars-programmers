def solution(arr, divisor):
    answer = []
    
    answer = sorted([data for data in arr if data % divisor == 0])
    if len(answer) == 0:
        return [-1]

    return answer

