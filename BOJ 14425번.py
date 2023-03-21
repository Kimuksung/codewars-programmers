def solution():
    import sys
    input = sys.stdin.readline

    n,m = map(int,input().split(' '))

    target_list = [input() for _ in range(n) ]
    check_lists = [input() for _ in range(m) ]

    print( sum( [1 for check_list in check_lists if check_list in target_list] ) )

if __name__ == "__main__":
    solution()