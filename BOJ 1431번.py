N = int ( input() )

arr = []
for i in range( N ) :
    arr.append( input() )

def str_sum_digit ( datas ) :
    return sum ( [int(data) for data in datas  if data.isdigit()] )

arr = sorted(arr , key = lambda x : ( len(x) , str_sum_digit(x) , x) )

for answer in arr :
    print ( answer )