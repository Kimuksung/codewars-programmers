from itertools import permutations
def calculate ( stack , yunsan) :
    for yunsanja in yunsan :
        while (stack) :
            try :
                operator_index = stack.index ( yunsanja )
                operator_first_value = stack.pop( operator_index-1 )
                operator_operator_value = stack.pop( operator_index - 1)
                operator_second_value = stack.pop( operator_index - 1 )
                #print ( stack , operator_index ,operator_first_value , operator_operator_value ,operator_second_value)
                if operator_operator_value == '+' :
                    stack.insert ( operator_index - 1 , operator_first_value + operator_second_value )
                elif operator_operator_value == '-' :
                    stack.insert ( operator_index - 1 , operator_first_value - operator_second_value )
                elif operator_operator_value == '*' :
                    stack.insert ( operator_index - 1 , operator_first_value * operator_second_value )

            except :
                break
    return abs(stack[0])
                
def solution(expression):
    answer = []
    
    stack = []
    temp_data = ''
    yunsan = list ( map ( ''.join ,  permutations ( ['+','-','*'] , 3) ) )
    
    
    for data in expression :
        if data not in ( '+' , '-' , '*' ) :
            temp_data += data
            continue

        stack.append(int ( temp_data) )
        stack.append(data)
        temp_data = ''
    stack.append( int ( temp_data) )
    
    #print ( yunsan )            
    #print ( stack )
    
    for yunsanja in yunsan :
        answer.append( calculate ( stack.copy() , yunsanja ) )
    
    return max(answer)