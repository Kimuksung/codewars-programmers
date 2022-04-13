#BOJ 1919번
#공통되는 단어를 찾는다.
from collections import Counter

cnt = 0
word_a , word_b = input() , input()
len_word_a , len_word_b= len(word_a) , len(word_b)
word_a , word_b = Counter( word_a ) , Counter( word_b )

for key , value in word_a.items() :
    if key in word_b :
        cnt += min( value , word_b[key])

print ( len_word_a + len_word_b - 2 * cnt )
