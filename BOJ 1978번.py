#BOJ 1978번

def sosu(n) :
    if n == 1 :
        return False
    for i in range(2,n) :
        if i*i > n :
            break
        if n%i == 0 :
            return False

    return True

n = int(input())
datas = list(map(int,input().split()))
print ( len( list( filter( sosu , datas ) ) ) )