def next_bigger(n):
    # 1. 거꾸로
    n = str(n)
    data = [i for i in n ] 

    if n == ''.join(sorted ( data , key= lambda x : -int(x) ) ) :
        return - 1

    # 2. 순서대로 정렬
    if n == ''.join(sorted ( data , key= lambda x : x ) ) :
         return int ( ''.join(data[:-2]) + data[-2] + data[-1] )
        
    # 3. 
    cnt = 0
    for a , b in zip ( data[::-1] , data[-2::-1] ) :
        cnt += 1
        if a > b :
            print ( data , b, a , cnt )
            temp = data[ len(data) - cnt - 1:].copy()
            min_data = min ( list ( filter ( lambda x:x > b , temp ) ) )
            temp.remove(min_data)
            temp.append(b)
            temp = sorted( temp , key = lambda x : x)
            left = data[:len(data) - cnt - 1]
            left.append( min_data )
            return int ( ''.join(left + temp )  )
        

print ( next_bigger( 12 )     )
