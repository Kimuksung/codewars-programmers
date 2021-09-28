def solution(new_id):
    answer = ''
    # 1단계
    new_id = new_id.lower()
    print ( '1단계 : ' , ''.join(new_id))
    # 2단계
    new_id = [id for id in new_id if id.isalnum() or id in ( '.' , '_' , '-') ]
    print ( '2단계 : ' , ''.join(new_id))

    # 3단계
    temp = 0
    temp_list = []
    for id in new_id :
        if (id != '.') :
            temp_list.append(id)
            temp = 0
        elif id == '.' and temp == 0  :
            temp_list.append(id)
            temp += 1
    new_id = temp_list

    print ( '3단계 : ' , ''.join(new_id))
    # 4단계
    while ( len(new_id) > 1 and new_id[0] == '.'):
        new_id = new_id[1:]
    while ( len(new_id) > 1 and new_id[-1] == '.'):
        new_id = new_id[:-1]
    if new_id == ['.']:
        new_id = []
    print ( '4단계 : ' , ''.join(new_id))    
    # 5단계
    if new_id == []:
        new_id.append('a')
    print ( '5단계 : ' , ''.join(new_id))
    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    print ( '6단계 : ' , ''.join(new_id))
    # 7단계
    while len(new_id) <= 2:
        new_id += new_id[-1]
    print ( '7단계 : ' , ''.join(new_id)) 
    answer = ''.join(new_id)   
    return answer

solution('abcdefghijklmn.p')