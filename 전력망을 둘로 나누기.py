def solution(n, real_wires):
    answer = []
    #한개일때 부터
    for index in range ( len(real_wires) ) :
        N , M = real_wires[index]
        wires = real_wires[:index] + real_wires[index+1:]
        stack_left = [ [N,0] ]
        visited_left = []
        cnt_left = 0
        while(stack_left) :
            a,b = stack_left.pop()   
            for wire in wires :
                if ( a in wire or b in wire ) and wire not in visited_left:
                    cnt_left += 1
                    stack_left.append(wire)
                    visited_left.append(wire)

        stack_right = [ [M,0] ]
        visited_right = []
        cnt_right = 0
        while(stack_right) :
            a,b = stack_right.pop()
            for wire in wires :
                if ( a in wire or b in wire ) and wire not in visited_right:
                    cnt_right += 1
                    stack_right.append(wire)
                    visited_right.append(wire)
                    
        answer.append( abs ( cnt_left - cnt_right ) )
        
    return min( answer ) 

print ( solution ( 9 , [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]) )