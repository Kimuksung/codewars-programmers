#BOJ 13335번

from collections import deque

time , bridge_weight , bridge_cnt = 0 , 0 , 0
n , length , weight = map( int , input().split() )

trucks = deque( map( int , input().split() ) )
bridge = [0] * length

while trucks :
    #print( time , bridge , trucks )
    truck = bridge[0]
    if truck != 0 :
        bridge_cnt -= 1
        bridge_weight -= truck

    bridge = bridge[1:] + [0]

    if bridge_weight + trucks[0] <= weight and bridge_cnt+1 <= length :
        truck = trucks.popleft()
        bridge_cnt += 1
        bridge_weight += truck
        bridge[-1] = truck

    time += 1

print(time+length)