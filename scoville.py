def change( data ):
    data = sorted(data)
    data.insert(2 , data[0] + data[1] * data[1])
    return data[2:]
    
def solution(scoville, K):
    answer = 0
    
    while ( len (list ( filter( lambda x : x < K , scoville ) ) ) > 0 ):
        answer += 1
        scoville = change(scoville)
        
    return answer

print ( solution( [1] , 7) ) 