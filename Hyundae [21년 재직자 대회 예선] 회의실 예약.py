# Hyundae [21년 재직자 대회 예선] 회의실 예약

import sys
input = sys.stdin.readline

n,m = map(int,input().split())

room_list = dict()

for _ in range(n):
    room_list[input().rstrip()] = [1]*9

for _ in range(m):
    room,start,end = input().rstrip().split()
    start,end=int(start),int(end)

    for i in range(start,end):
        room_list[room][i-9]=0

print(room_list)

def available_room(data):
    answer = []
    check = False
    temp = []
    for i in range(len(data)):
        if data[i] and not check:
            check=True
            temp.append(i)

        if not data[i] and check :
            temp.append(i)
            check=False
            answer.append(temp)
            temp=[]

    if check :
        temp.append(len(data))
        answer.append(temp)
    return len(answer) , [ (a+9,b+9) for a,b in answer ] , list(map( lambda x:(x[0]+9,x[1]+9), answer)) 
    #return [ (a+9,b+9-1) for a,b in zip(*answer) ]

for room in sorted(room_list.keys()):
    print( room , available_room(room_list[room]) )