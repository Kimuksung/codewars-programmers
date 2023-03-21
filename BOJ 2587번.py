def solution():
    import sys
    input = sys.stdin.readline

    number_list = [int(input()) for _ in range(5)]
    number_list.sort()
    n = len(number_list)

    print(int(sum(number_list)/n))
    print(number_list[n//2])

if __name__ == "__main__":
    solution()