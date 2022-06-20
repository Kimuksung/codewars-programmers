def solution(id_list, reports, k):
    answer = []
    reports = list(set(reports))
    report_dict = dict()
    user_report = dict()
    
    #report
    for report in reports :
        report = report.split()
        if report[0] not in user_report :
            user_report[report[0]] = []
        user_report[report[0]].append(report[1])
        
        if report[1] not in report_dict :
            report_dict[report[1]] = 0
        report_dict[report[1]] += 1
        
    for id in id_list :
        if id not in user_report :
            answer.append(0)
        else :
            temp = 0
            for report_data in user_report[id] :
                if report_dict[report_data] >= k :
                    temp+=1
            answer.append(temp)
    
    return answer