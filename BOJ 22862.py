#BOJ 22862
n , k = map(int,input().split())
datas = list( map(int,input().split()) )

right = 0 
cnt = int(datas[0]%2==1)
answer = 0

for left in range(n) :
    
    while right < n-1 and cnt+int(datas[right+1]%2==1) <= k :
        right+=1
        cnt += int(datas[right]%2==1)

    answer = max(answer , right-left+1-cnt)
    cnt -= int(datas[left]%2==1)

print(answer)