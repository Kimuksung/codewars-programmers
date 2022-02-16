#Merge sort
# 나누는 경우 N -> 1  O(N)
# 병합하는 경우 1 -> N  O(NK) = O(NlogN)
# 공간 복잡도 = O(N)
# Stable Sort = 같은 값이라 하여도 순서를 보장

# 코딩 테스트에서 정렬 필수 사용

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

