#BOJ 18869번

import sys
input=sys.stdin.readline
def sorted_index( lists ) :
    sorted_list = sorted( list(set(lists)))
    dictionary = dict()
    new_list = []
    for i , data in enumerate(sorted_list) :
        dictionary[data] = i
    for x in lists :
        new_list.append(dictionary[x])

    return new_list

n , m = map(int,input().split())
datas = [[] for _ in range(n) ]

for i in range(n) :
    datas[i] = sorted_index( list(map(int,input().split())) )

datas.sort()
cnt , answer= 1 , 0

for i in range(1,n) :
    if datas[i]==datas[i-1] :
        cnt += 1
    else :
        answer += (cnt*(cnt-1)) // 2
        cnt = 1
answer += (cnt*(cnt-1)) // 2

print(answer)