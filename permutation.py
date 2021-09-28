def permutations(string):
    #your code here
    n = len(string)
    answer = [ [] for i in range( n + 1 )]
    answer[0] = ['']

    for i in range ( n ):
        print ( 'i:' , i)
        print (answer)
        print ( ''.join(answer[i]) + string[i] )
        print ( string[i] + ''.join(answer[i]) )
        answer[i+1].append(''.join(answer[i]) + string[i])
        answer[i+1].append(string[i] + ''.join(answer[i])) 
        answer[i+1] = list( set(answer[i+1]) )
        #print ( answer[i] + string[i])
        #answer[i].append( answer[i-1] + string[n] )
        #answer[i].append( answer[i-1] + string[n] )
    #print (answer)
        
permutations( 'aabb' )