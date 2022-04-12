#BOJ  1475번
numbers = input()
number_list = [0] * 9

for num in numbers :
    num = int(num)
    if num == 9 :
        num = 6
    number_list[num] += 1

if number_list[6] %2 :
    number_list[6] += 1

number_list[6] = number_list[6] // 2

print ( max(number_list) )