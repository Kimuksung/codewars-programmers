#BOJ 5048번

datas = []
first_command = list ( map ( str , input().split() ) )
n = int ( first_command[0] )

if len( first_command ) > 1 :
    for temp in first_command[1:] :
        datas.append( int ( temp[::-1].lstrip('0') ) )

while True :
    if len(datas) >= n :
        break
    temps = input().split()
    for temp in temps : 
        datas.append( int ( temp[::-1] ) )
    
datas.sort()
print ( *datas )
