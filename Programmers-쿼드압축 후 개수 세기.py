import math
def solution(arr):
    def check_data(x,y,n):
        zero_cnt,one_cnt=0,0
        check=True
        if n==0:
            return [int(not arr[x][y]),int( arr[x][y])]
        data=arr[x][y]
        for i in range(x,x+int(math.pow(2,n))):
            for j in range(y,y+int(math.pow(2,n))):
                if arr[i][j]!=data:
                    check=False
                    break
        if check :
            return [int(not arr[x][y]),int(arr[x][y])]
        else:
            temp=check_data(x,y,n-1)
            zero_cnt+=temp[0]
            one_cnt+=temp[1]
            
            temp=check_data(x+int(math.pow(2,n-1)),y,n-1)
            zero_cnt+=temp[0]
            one_cnt+=temp[1]
            
            temp=check_data(x,y+int(math.pow(2,n-1)),n-1)
            zero_cnt+=temp[0]
            one_cnt+=temp[1]
            
            temp=check_data(x+int(math.pow(2,n-1)),y+int(math.pow(2,n-1)),n-1)
            zero_cnt+=temp[0]
            one_cnt+=temp[1]
        
        return [zero_cnt,one_cnt]

    one_cnt,zero_cnt=0,0
    pow=-1
    n=len(arr)
    while n>0:
        pow+=1
        n=n//2
 
    zero_cnt+=check_data(0,0,pow)[0]
    one_cnt+=check_data(0,0,pow)[1]

    return [zero_cnt,one_cnt]

print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))