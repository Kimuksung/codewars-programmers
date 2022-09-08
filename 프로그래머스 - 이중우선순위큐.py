import heapq

def solution(operations):
    min_heap = []
    max_heap = []
    
    for operation in operations :
        command , value = operation.split(' ')
        value = int(value)
        
        if command == 'I' :
            heapq.heappush( min_heap , value )
            heapq.heappush( max_heap , -value )
        
        # 최소 삭제
        elif value==-1 :
            # Balancing
            while min_heap and max_heap and -min_heap[0] not in max_heap:
                heapq.heappop(min_heap)
            if min_heap:
                heapq.heappop(min_heap)
        # 최대 삭제     
        else :
            # Balancing
            while max_heap and min_heap and -max_heap[0] not in min_heap:
                heapq.heappop(max_heap)
            if max_heap:
                heapq.heappop(max_heap)

    # 서로가 빼낸 값들은 제외시켜준다
    while max_heap and min_heap and -max_heap[0] not in min_heap:
            heapq.heappop(max_heap)

    while min_heap and max_heap and -min_heap[0] not in max_heap:
            heapq.heappop(min_heap)

    if not min_heap or not max_heap:
        return [0,0]
    
    return [-max_heap[0] , min_heap[0]]

operations = ["I 4", "I 3", "I 2", "I 1", "D 1", "D 1", "D -1" , "D -1"]
print(solution(operations))