clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"],["sample","arms"]]
data=dict()
answer = 0

for items in clothes :
    if items[1] not in data :
        data[items[1]] = 0
    data[items[1]] += 1
    
cloth=list(data.values())
check = [0]*len(cloth)

def recursion(temp , number , target , current) :
    global answer
    if number == target :
        #print(check , temp )
        answer += temp
        return

    for i in range(current , len(cloth)) :
        if not check[i] :
            check[i] = 1
            recursion( temp*cloth[i] , number+1 , target , i )
            check[i] = 0

for i in range(2,len(cloth)+1) :
    recursion(1 , 0 , i , 0)   
         
answer += sum(cloth)
print(answer)