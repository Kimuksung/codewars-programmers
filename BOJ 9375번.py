#BOJ 9375번

n = int(input())

for i in range(n) :
    m = int(input())
    passion = dict()
    answer = 1
    for _ in range(m) :
        value , key = input().split()
        if key not in passion :
            passion[key] = 0
        passion[key] += 1

    for i in list( passion.values() ) :
        answer *= i+1

    print(answer-1)