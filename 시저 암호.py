def solution(s, n):
    answer = ''
    alphabet = dict()
    alpha = 'abcdefgijklmnopqrstuvwxyz'
    for i in s.lower() :
        print ( i )
        print ( alpha.index(i) )
        #answer += alpha[( alpha.index(i) + n ) % 24 ] 

solution ( "AB" , 1 )