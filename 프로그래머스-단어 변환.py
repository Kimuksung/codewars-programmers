import sys
from collections import deque

def solution(begin, target, words):
    alphas = [chr(i) for i in range(97,97+26)]
    answer = 0
    word_dict = dict()
    n = len(begin)
    #visited 역할
    for word in words:
        word_dict[word] = sys.maxsize
        
    q = deque()
    q.append((begin,0))
    
    while q :
        word,cnt = q.popleft()
        # 종료 조건
        if word == target:
            answer=cnt
            break
        
        # 단어 변환
        for i in range(n):
            for alpha in alphas :
                temp = word[:i] + alpha + word[i+1:]
                if temp in word_dict and cnt+1 < word_dict[temp] :
                    word_dict[temp]=cnt+1
                    q.append( (temp,cnt+1))

    return answer

begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log"]	

solution(begin, target, words)