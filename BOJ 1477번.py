#BOJ 1477번

answer = 0
n , cnt , road = map(int,input().split())
arr = [0]+sorted(list(map(int,input().split())) ) + [road]
minus_arrs = []
for v1,v2 in zip(arr,arr[1:]) :
    minus_arrs.append(v2-v1-1)

left , right = 1 , road-1

while left <= right :
    gap = (left+right)//2

    temp_cnt = 0
    for minus_arr in minus_arrs :
        if minus_arr >= gap :
            temp_cnt+=minus_arr//gap
    if temp_cnt > cnt :
        left = gap+1
    else :
        answer = gap
        right = gap-1

print(answer)