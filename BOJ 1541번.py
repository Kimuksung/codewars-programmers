#BOJ 1541번

def plus_answer( data ) :
    temp_data = data.split('+')
    temp = 0
    for data in temp_data :
        temp += int(data.lstrip('0'))
    return temp

datas = input().split('-')
answer = plus_answer( datas[0] )
for data in datas[1:] :
    answer -= plus_answer( data )

print(answer)