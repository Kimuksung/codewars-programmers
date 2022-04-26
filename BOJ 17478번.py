#BOJ 17478번

n = int ( input() )
char_data = '____'
print ( '어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.')

def second_function( number ) :
    if number == 0 :
        print ( '라고 답변하였지.')
        return
    temp = char_data * number
    print ( temp + '라고 답변하였지.')
    second_function ( number - 1 )

def first_function ( number ) :
    temp = char_data * number
    print ( temp + '"재귀함수가 뭔가요?"')
    if number != n :
        print ( temp + '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.' )
        print ( temp + '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
        print ( temp + '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
        first_function ( number + 1 )
    else :
        print ( temp + '"재귀함수는 자기 자신을 호출하는 함수라네"')
        second_function( number )
    
first_function ( 0 )