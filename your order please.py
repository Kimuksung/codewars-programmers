def order(sentence):
    datas = sentence.split(' ')
    answer = ['' for i in range ( len(datas) )]

    for data in datas for char_data

    for data in datas:
        for char_data in data:
            if char_data.isnumeric() :
                answer[ int ( char_data ) - 1] = data

    print ( ' '.join(answer) )
                
                
order ("is2 Thi1s T4est 3a")