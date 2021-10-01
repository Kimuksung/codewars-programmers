def solution(price, money, count):
    answer = sum(range(1, count + 1)) * price - money
    return max ( 0 , answer )
print ( solution ( 3, 20 , 4 ))