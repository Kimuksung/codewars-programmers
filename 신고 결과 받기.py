from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    report_dict = defaultdict(set)
    mail_dict = defaultdict(int)
    # 신고 유저
    for user,report_user in report :
        report_dict[report_user].add(user)
    
    for report_user,user in report_dict.items():
        if len(user) >= k:
            for u in user:
                mail_dict[u]+=1
    return [mail_dict[id] for id in id_list] 

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k=2
solution(id_list, report, k)