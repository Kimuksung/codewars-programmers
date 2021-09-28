def solution(s):
    answer = ''
    left , right  = 0 , 0
    temp = { 'zero' : '0' , 
            'one' : '1',
            'two' : '2',
            'three' : '3',
            'four' : '4',
            'five' : '5',
            'six' : '6',
            'seven': '7',
            'eight' : '8',
            'nine' : '9'
           }
    for idx , data in enumerate ( s ):
        #print ( left , idx ,  data)
        #print (s[left : idx ])
        if data.isdigit():
            left = idx + 1
            answer += data
        elif s[left : idx ] + data in temp.keys():
            answer += temp[s[left : idx ] + data ]
            left = idx + 1
        
    return int ( answer ) 
print ( solution ( "one4seveneight" ))