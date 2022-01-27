n , m = map(int , input().split() ) # 3, 5 

datas = list ( map(int , input().split() ) ) # [ 1,2,3]
answer = 0 

def solution ( count , total ) :
    global answer
    if count == n :
        if total == m :
           answer += 1 
        return
    solution ( count + 1 , total + datas[count])
    solution ( count + 1 , total )

solution( 0 , 0 )
if m == 0 :
    answer -= 1
print (answer )