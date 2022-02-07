def solution(arrs):
    answer = []
    real_answer = 1
    #100 이하의 소수
    sosu_arr = []
    for i in range ( 2 , 100 ) :
        cnt = 0
        for j in range ( 2 , int ( i ** (1/2) ) + 1 ) :
            if i % j == 0 :
                cnt += 1
        if cnt == 0:
            sosu_arr.append( i )
    
    for sosu in  sosu_arr :
        while ( True ) :
            cnt = 0
            for index , arr in enumerate ( arrs ) :
                if arr != 1 and arr % sosu == 0 :
                    cnt += 1
                    arrs[index] /= sosu
            if cnt == 0 :
                break
            answer.append( sosu )

    for data in answer :
        real_answer *= data
    return real_answer

    #default를 맨앞의 수로 잡고 곱한다음에 최대 공약수로 나누면 있는 최대한의 값이 나온다..
    #gcd를 활용..
print ( solution ( [1,2,1] ))