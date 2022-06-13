#BOJ 1700번
import sys

n , m = map(int,input().split())
digital = list( map(int,input().split()) )
multitap = [0]*n
answer = 0

for index , data in enumerate(digital) :
    # 꼽혀있는 경우
    if data in multitap :
        continue
    # 멀티탭이 비어있는 경우
    if 0 in multitap :
        multitap[multitap.index(0)] = data
        continue

    # 빼야 하는 경우
    # 멀티탭에 있는 것중에서 가장 뒤에 나오거나 안나오는 애들
    target_index = -1*sys.maxsize
    check = False
    temp = digital[index:]
    for multitaps in multitap :
        if multitaps not in temp :
            multitap[multitap.index(multitaps)] = data
            check = True
            break
        else :
            target_index = max(temp.index(multitaps) , target_index )

    if target_index != -1*sys.maxsize and not check :
        multitap[multitap.index(temp[target_index])] = data
    answer += 1

print(answer)    