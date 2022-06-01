#BOJ 2847번

n = int(input())
datas = []

for _ in range(n) :
    datas.append(int(input()))

datas = datas[::-1]
current ,answer  = 1 , 0

for before_data , after_data in zip(datas,datas[1:]) :
    if after_data > before_data-1 :
        answer += after_data-(before_data-1)
        datas[current] = before_data-1
    current+=1

print(answer)