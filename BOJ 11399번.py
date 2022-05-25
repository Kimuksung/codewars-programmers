#BOJ 11399번

cnt , answer = 0 , 0
n = int(input())
datas = list(map(int,input().split()))
datas.sort()

for data in datas :
    cnt += data
    answer += cnt

print( answer )