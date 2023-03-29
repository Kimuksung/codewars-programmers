def solution(sequence):
    answer = 0
    n = len(sequence)
    sequence1 = [0]+[-sequence[i] if i%2==0 else sequence[i] for i in range(n)]
    sequence2 = [0]+[-sequence[i] if i%2==1 else sequence[i] for i in range(n)]
    
    for i in range(1,n+1):
        sequence1[i] = max( sequence1[i-1]+sequence1[i] , sequence1[i] )
        sequence2[i] = max( sequence2[i-1]+sequence2[i] , sequence2[i] )
        
    return max(max(sequence1[1:]),max(sequence2[1:]))