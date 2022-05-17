#BOJ 7490번
m = int(input())
for _ in range(m) :
    n = int(input())

    data = [str(i) for i in range(1,n+1) ]
    char_list = []
    expression = [' ' ,'+' , '-']

    temp = []
    def backtracking( number ) :
        if number == n :
            if eval ( ''.join(temp[:-1]).replace(' ' , '') ) == 0 :
                char_list.append( ''.join(temp[:-1]) )
            return

        temp.append(data[number])
        for i in range(3) :
            temp.append(expression[i])
            backtracking(number+1)
            temp.pop()
            if number+1 == n :
                break
        temp.pop()

    backtracking(0)        
    [print( char_lists ) for char_lists in char_list ]
    print()