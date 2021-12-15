# Python 기초 재정리

# 자료형

참조 : [https://velog.io/@modolee/floating-point](https://velog.io/@modolee/floating-point)

- Char
1byte = 1bit로 이루어진 단위로써 맨 앞자리는 음수로 표현 -> - 2^7 ~ 2^7-1 = -128 ~ 127
- unsigned char
1byte = 1bit로 이루어진 단위로써 맨 앞자리는 양수로 표현 -> 2^0 ~ 2^8-1 = 0 ~ 255

```python
a = float (0.1 + 0.1 + 0.1)
b = float ( 0.3)
if ( 0.1 + 0.1 + 0.1 == 0.3 ) :
    print('True')

if ( abs(a-b) < 1e-12 ) :
    print('True')
```

- Int ( 4byte )

3 = 2^1 + 2^0 = 11(2)

- Float ( 4byte )

![https://media.vlpt.us/images/modolee/post/a830c5e9-ec15-4937-b2d8-6e0dd0ae4370/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202020-09-08%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%2011.57.48.png](https://media.vlpt.us/images/modolee/post/a830c5e9-ec15-4937-b2d8-6e0dd0ae4370/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202020-09-08%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%2011.57.48.png)

![https://habrastorage.org/r/w1560/webt/9r/rs/uu/9rrsuu7iiox5bcryce66twupg5q.png](https://habrastorage.org/r/w1560/webt/9r/rs/uu/9rrsuu7iiox5bcryce66twupg5q.png)

3.75 = 2+1+0.5+0.25 = 11.11(2)

- Double

Python 은 Double 형태를 지원하지 않는다.

파이썬3 에서는 Int overflow error 발생하지 않는다 ( 단, Numpy , Pandas에서는 나타남 )
파이썬2 에서는 Int ( 4byte ) 를 넘어가면 자동으로 long으로 변경

파이썬3에서는 long type이 사라지고 arbitrary precision( fixed-precision과 달리, 현재 남아있는 만큼의 가용 메모리로 표현 )을 지원

[https://ahracho.github.io/posts/python/2017-05-01-everything-in-python-is-object-integer/](https://ahracho.github.io/posts/python/2017-05-01-everything-in-python-is-object-integer/)

[https://ahracho.github.io/posts/python/2017-05-09-python-integer-overflow/](https://ahracho.github.io/posts/python/2017-05-09-python-integer-overflow/)