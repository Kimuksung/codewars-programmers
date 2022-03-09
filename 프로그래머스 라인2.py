from collections import Counter

#reasearch , n , k = [ 'yxxy' , 'xxyyy' , 'yz'] , 2 , 1
#reasearch , n , k = [ 'yxxy' , 'xxyyy' ] , 2 , 1
#reasearch , n , k = [ 'abaaaa' , 'aaa' , 'abaaaaaa' , 'fzfffffffa' ] , 2 , 2
reasearch , n , k = [ 'xy' , 'xy' ] , 2 , 1

def check_data ( reasearch , n , k , length) :
    answer = dict()
    for i in range ( length - n + 1) :
        set_datas = set ( reasearch[0] )
        for temp in reasearch[i:i+n] :
            set_datas = set_datas and set ( dict( filter ( lambda x : x[1] >= k , Counter( temp ).items() ) ).keys() )
            
        cnt_data = ''.join(reasearch) 
        for i in set_datas :
            if cnt_data.count(i) >= n*k*2 :
                if i in answer :
                    answer[i] += 1
                else :
                    answer[i] = 1
    if not answer :
        return "None" 
            
    return sorted( answer.items() , key = lambda x : ( - x[1] , x[0] ) )[0][0] 
    

length = len(reasearch) 
print ( check_data ( reasearch , n , k , length) )