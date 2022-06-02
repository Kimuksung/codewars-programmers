#BOJ 1439번

datas = input()
zero_cnt , one_cnt = 0,0
current = int(datas[0])
if current :
    one_cnt += 1
else :
    zero_cnt += 1

for data in datas :
    data = int(data)
    if current != data :
        if data :
            one_cnt += 1
        else :
            zero_cnt += 1    
        current = data
    
print( min(zero_cnt,one_cnt) )