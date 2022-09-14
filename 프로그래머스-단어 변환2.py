from collections import deque

# 문자 목록에서 현재 단어와 한개의 문자만 다른 경우
def check_with_generator( current , words ) :
    for word in words :
        count = 0
        for c,w in zip(current,word) :
            if c!=w :
                count+=1

        if count==1 :
            yield word
            
def solution(begin, target, words):
    make_word = {begin:0}
    q = deque([begin])

    while q :
        current = q.popleft()
        for word in check_with_generator(current,words):
            # 방문 한적이 없다면 추가 visited 역할
            if word not in make_word :
                make_word[word] = make_word[current]+1
                q.append(word)
                
    return make_word.get(target , 0 )