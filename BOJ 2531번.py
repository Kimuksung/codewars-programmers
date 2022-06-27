#BOJ 2531번
belts , d , k , coupon= map(int,input().split())
datas = [int(input())for _ in range(belts)]
number = [0]*(d+1)

answer = 0
right = 0
cnt = 0 
current = 0
for i in range(belts) :
    #K칸 만큼 이동
    while cnt < k :
        if not number[datas[right]] :
            current += 1
        number[datas[right]] += 1
        right = (right+1) % belts
        cnt += 1
    #해당 쿠폰이 없어서 추가 제공
    if not number[coupon] :
        answer = max(answer,current+1)
    else :
        answer = max(answer,current)

    if number[datas[i]] > 1 :
        number[datas[i]] -= 1
    elif number[datas[i]] == 1 :
        number[datas[i]] -= 1
        current -= 1
    cnt -= 1
    
print(answer)