a , b = 4 , 5
answer = 1
a , b = a + 1 , b + 1
for i in range ( 20 ) :
    if a != 1 :
        a = a // 2 + 1
    if b != 1 :
        b = b // 2 + 1
    if a == b :
        break
    answer += 1

print ( answer )