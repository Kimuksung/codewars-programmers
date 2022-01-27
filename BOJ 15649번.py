N , M  = map ( int , input().split(' ') )

arr = [0] * M
data_set = [0] * N

def solution( num ) :
    if num == M :
        print ( ' '.join(map(str , arr )) )
        return 

    for idx , data in enumerate ( data_set )  :
        if not data : 
            arr[num] = idx + 1
            data_set[idx] = 1
            solution( num + 1) 
            data_set[idx] = 0

solution( 0 )