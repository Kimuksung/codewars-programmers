def solution():
    import sys
    input = sys.stdin.readline

    _,k = map(int,input().split(' '))
    number_list = list(map( int ,input().strip().split(' ')))

    answer = []
    def merge_sort(L):
        if len(L) == 1:
            return L
        
        mid = (len(L)+1)//2
        left = merge_sort(L[:mid])
        right = merge_sort(L[mid:])
        temp = left+right
        temp.sort()
        [answer.append(l) for l in temp]

        return temp

    merge_sort(number_list)

    if k>len(answer) :
        print(-1)
    else:
        print(answer[k-1])

if __name__ == "__main__":
    solution()