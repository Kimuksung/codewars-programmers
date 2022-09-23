from collections import defaultdict
import math

def solution(fees, records):
    answer = []
    in_dict = defaultdict(list)
    out_dict = defaultdict(list)
    id = set()
    
    for record in records :
        time,car,type = record.split(' ')
        id.add(car)
        if type == "IN":
            in_dict[car].append(time)
        else :
            out_dict[car].append(time)

    for car in sorted(id):
        time = 0
        fee = fees[1]
        if len(in_dict[car]) != len(out_dict[car]) :
            out_dict[car].append("23:59")
        for start,end in zip(in_dict[car],out_dict[car]):
            start_time , start_minute = map(int,start.split(':'))
            start=start_time*60+start_minute
            end_time , end_minute = map(int,end.split(':'))
            end = end_time*60+end_minute
            time += end-start
        
        if time <= fees[0]:
            answer.append(fee)
        else :
            add_tax = math.ceil( (time-fees[0])/fees[2])*fees[3] 
            answer.append(fee+add_tax)
                    
    return answer