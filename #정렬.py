# 기초 정렬
arr = [ 3 , 2 , 7 , 116 , 62 , 235 , 1 , 23 , 55 , 77]
n = len(arr)

for i in range ( n-1 , 0 - 1 , - 1) :
    max_index = arr.index( max(arr[:i+1]) )
    arr[i] , arr[max_index] = arr[max_index] , arr[i]


# 버블 정렬 
# O(N^2)
arr = [ 3 , 2 , 7 , 116 , 62 , 235 , 1 , 23 , 55 , 77]
n = len(arr)
for i in range ( n -1 , 0-1 , -1 ) :
    for j in range( i ) :
        if arr[j] > arr[j+1] :
            arr[j] , arr[j+1] = arr[j+1] , arr[j]

# merge sort
# O(NlogN)
# list -> N , M 의 List로 1 + 2 + 4 + .. 2^n = 2N - 1 = O(N)
# N , M 의 List -> list 합치기 N*K = O(NlogN)
#Merge sort
# N -> 1  O(N)
# 1 -> N  O(NK) = O(NlogN)

arr = [ 3 , 2 , 116 ,7 , 62 , 235 , 1 , 23 , 55 , 77]
n = len(arr)
temp_arr = [0] * n

def merge( start , end ) :
    mid = ( start + end ) // 2
    left_idx = start
    right_idx = mid 

    for i in range( start , end ) :
        if right_idx == end :
            temp_arr[i] = arr[left_idx]
            left_idx += 1
        elif left_idx == mid or arr[left_idx] > arr[right_idx]:
            temp_arr[i] = arr[right_idx]
            right_idx += 1
        else:
            temp_arr[i] = arr[left_idx] 
            left_idx += 1

    arr[start:end] = temp_arr[start:end]

def merge_sort ( start , end ) :
    # 재귀 end조건
    if end == start + 1 : 
        return
    mid = ( start + end ) // 2
    merge_sort( start , mid )
    merge_sort( mid , end )
    merge(start,end) 

merge_sort( 0 , 3 )
print ( arr )

# quicksort
# 장점 : 별도의 공간을 안잡아도 된다 / cache hit rate 높음
# 실제 구현은 Merge sort로 하는게 재귀적으로 표현하기 쉽다.
# pivot 이라는 기준점을 잡은 뒤 좌 -> 우 / 우 -> 좌
# 평균적(중간쯤 오는 경우)으로 O(NlogN) But !! 최악 O(N^2)

arr = [ 3 , 2 , 116 ,7 , 62 , 235 , 1 , 23 , 55 , 77]
def Quicksort( start ,end ) :
    #재귀 종료
    if end == start + 1 : return

    pivot = arr[start]
    left = start+1 
    right = end
    while ( True ) :
        # 1. 좌 -> 우
        print (pivot , left , right )
        while( left <= right and arr[left] <= pivot ) : left += 1
        # 2. 우 -> 좌
        while( left <= right and arr[right] >= pivot ) : right -= 1
        # 4. right < left 종료 조건
        if right < left :
            break
        # 3. 둘다 멈추면 swap
        arr[left] , arr[right] = arr[right] , arr[left]
    arr[start] , arr[right] = arr[right] , arr[start]    
    
    #재귀 이용
    Quicksort( start , right )
    Quicksort( right + 1 , end )
    
Quicksort( 0 , 3 )     
print ( arr )