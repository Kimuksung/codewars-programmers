#BOJ 10799번
# Idea : 막대의 갯수를 세고 레이저가 발사되면 갯수 추가

stack = []
char_datas = input()
answer = 0
for index , char_data in enumerate ( char_datas ) :
    if char_data == '(' :
        stack.append('(')
    elif char_data == ')' :
        if index > 0 and char_datas[index-1] =='(' :
            stack.pop()
            answer += len(stack)
            continue
        elif stack and stack[-1] == '(' :
            answer += 1
            stack.pop()

print ( answer )