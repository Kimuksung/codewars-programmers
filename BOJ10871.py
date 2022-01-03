N , X = map ( int , input().split(' ') )
k = list ( filter ( lambda x : x < X, list ( map( int , input().split(' ') ) ) ) )
for data in k :
    print ( data )
