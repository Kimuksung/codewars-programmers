import sys
input = sys.stdin.readline

n = int(input())
number_list = list(map(int,input().split(' ')))
operator_list = list(map(int,input().split(' ')))
answer = []
cur_num = number_list[0]

def trace( number ):
    global cur_num
    if number == n :
        answer.append(cur_num)
        return

    for i in range(4):
        if operator_list[i]<=0:
            continue

        operator_list[i]-=1
        temp = cur_num
        if i == 0:
            cur_num = cur_num+number_list[number]
        elif i == 1:
            cur_num = cur_num-number_list[number]
        elif i == 2:
            cur_num = cur_num*number_list[number]
        else :
            if cur_num < 0 and number_list[number] > 0 :
                cur_num = (-cur_num) // number_list[number] * -1
            else:
                cur_num = cur_num//number_list[number]

        trace(number+1)
        operator_list[i]+=1
        cur_num = temp

trace(1)
print(max(answer))
print(min(answer))