#BOJ 2003번

answer = 0 
n , target = map(int,input().split())
datas = list(map(int,input().split()))

left , right = 0 , 0
sum_value = 0

for i in range(n) :
    while sum_value <= target :
        if sum_value == target :
            answer += 1
            break
        if right == n :
            break
        sum_value += datas[right]
        right += 1

    sum_value -= datas[left]
    left += 1

print(answer)