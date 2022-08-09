# Programmers-주차 요금 계산

from collections import defaultdict
def solution(fees, records):
    answer = []
    
    # value = [(OUT,시간)...]
    cars = defaultdict(lambda :[])
    
    #car transform
    for record in records :
        time,car_num,status=record.split()
        cars[car_num].append([status,time])
        
    for car in sorted(cars.keys()):
        time,money=0,0
        
        values=cars[car]
        if values[-1][0] != 'OUT':
            cars[car].append(['OUT','23:59'])
        values=values[::-1]
        # fee transform
        for end,start in zip(values[::2],values[1::2]):
            end_hour,end_minutes=end[1].split(':')
            end_time=int(end_hour)*60+int(end_minutes)
            start_hour,start_minutes=start[1].split(':')
            start_time=int(start_hour)*60+int(start_minutes)
            time+=end_time-start_time

        time=time-fees[0]
        money+=fees[1]
        if time>0 :
            money+= (time//fees[2])*fees[3] if time%fees[2]==0 else (time//fees[2]+1)*fees[3]
            
        answer.append(money)
        
    return answer