#BOJ 2467번

n = int(input())
datas = list(map(int,input().split() ) )
n = len(datas)
answer = []

for index , data in enumerate(datas) :
    start , end = index , n
    while start < end :
        middle = (start+end)//2+1 
        temp = index+middle

        if temp > n-1 :
            temp = n-1
            break
        
        if datas[start]+datas[temp] > 0 :
            end = middle
        else :
            start = middle
    answer.append( ( data , datas[start] , abs(datas[start]+data) ) )

print(answer)
