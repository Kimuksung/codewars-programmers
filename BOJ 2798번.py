def solution():
    import sys
    input = sys.stdin.readline

    n,target = map(int, input().split(' '))
    number_list = list(map(int , input().strip().split(' ') ))

    answer = 0
    for i in range(n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                temp = number_list[i]+number_list[j]+number_list[k]
                if temp > answer and temp <= target :
                    answer = temp

    print(answer)

if __name__ == "__main__":
    solution()