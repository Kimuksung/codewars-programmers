# quicksort
# 장점 : 별도의 공간을 안잡아도 된다.
# 실제 구현은 Merge sort로 하는게 재귀적으로 표현하기 쉽다.
# pivot 이라는 기준점을 잡은 뒤 좌 -> 우 / 우 -> 좌
# 평균적(중간쯤 오는 경우)으로 O(NlogN) But !! 최악 O(N^2)
# 공간 복잡도 = O(1)

# 라이브러리 내에서 퀵소트는 피벗 후보를 3개 중 중앙값 / 일정 Depth 이상 들어가면 힙소트로 구현되도록 되어있다 -> introspective sort

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