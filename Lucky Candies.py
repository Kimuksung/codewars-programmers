import itertools

def lucky_candies(prizes, k):
    for i in range ( len(prizes) , 0 , -1) :

        temp = []
        for data in list ( map ( list , itertools.combinations(prizes , i) ) )  :
            print ( data , sum(data))
            temp.append ( sum(data) )
        #print ( i , list ( filter( lambda x : x%k == 0 , temp ) ) )
        answer = list ( filter( lambda x : x%k == 0 , temp ) )
        
        if list ( filter( lambda x : x%k == 0 , temp ) ) != [] :
            return max(answer)
    
    return  0
print ( lucky_candies( [6,5] , 5) )