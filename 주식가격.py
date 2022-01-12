prices = [1, 2, 3, 2, 3]
stack = [0]

length = len (prices)
answer = [ i for i in range (length - 1, -1, -1)]
print ( answer)
print ('start--')
for i in range (1, length):
    print(i, stack)
    while stack and prices[stack[-1]] > prices[i]:
        j = stack.pop()
        answer[j] = i - j
        print(i, j, stack)
    stack.append(i)

print('--')
print(stack)
print(answer)
