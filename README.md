
# 기초문법 정리

  

# 자료형

  

> Boolean

>

False = 0 , None , 빈 Containter ( List , tuple .. )

True = 1 등 False를 정의하는 외 모든 값

  

> List

>

List = 여러 자료형을 저장할 수 있는 자료형으로 element / index로 이루어져 있다.

List는 하나의 오브젝트 형태로 파라미터 인자값으로 넘겨주어도 해당 값이 변경된다.

Min / Max / Sum / Reversed / Enumerate / Join

  

리스트 내포(List comprehension)

  

[i for i in range(5)]

[i for i in range(5) if i > 2]

[i if i > 2 else None for i in range(5) ]

  

추가

Append = 하나의 element

Insert = 특정 index에 하나의 element 추가

Extend = List 추가

  

a = [1,2,3,4,5] # a=list()

a.append(1)

a.insert(3,10)

a.extend([1,2,3]

  

삭제

Del = 여러 값 삭제 가능

Pop = 하나의 값 삭제 ( Default = -1 )

Remove = 특정 Value 처음 나오는 index 삭제

Clear = List 비우기

  

a.pop() # -1 default

del a[3]

del a[4:5]

a.remove(5)

a.clear()

  

문자열 변환

''.join ( list() ) # 이때 List내 자료형은 문자열이여야 한다

  

> dictionary

>

Dictionary get() / keys() / values() /items()

a = {'name' : 'uksung' }

#key 추가

a[new_key] = 'new_value'

#삭제

del a[new_key]

#key checking

if key in dictionary

Data = {'a' : 1 , 'b' :2 }

Data.get('a' , 'no_data')

-> 1

Data.get('c' , 'no_data')

-> no_data

dictionary.get(key) ## key가 없다면 뒤 파라미터 값으로 / None return

  
  

>range

>

range(A,B,C) 로 일반적으로 B에 Int형으로 B//2 와 같은 형태로 쓴다.

break : 반복문 종료

continue : 현재 반복 생략

  

> tuple

>

List와 유사하지만 한번 결정된 값은 변경 불가

괄호는 생략 가능

함수에서 Return 시 일반적으로 Tuple 형태 E.g ) enumerate , divmod , map , filter

  

#tuple 하나 선언 시에는

(293 , )

문자열 여러 줄에 걸치는 용도와 헷갈리지 않도록

a = ( 'hi' 'hello' 'check' )

b = ( a, b,c )

  

# 연산자

- '+' : 덧셈 / containter 결합 / 원본 데이터에 영향 X

- '*' : 곱셈 / 반복연산자 / 원본 데이터에 영향 X

- '//' : 몫

- -'%' : 나머지

  

python time 은 unix time으로써, UTC 기준 특정 날짜로부터 몇초가 지난지로 구별

  

# And / Or

And는 앞이 True 인 경우에만 뒤에를 본다

OR은 무조건 | 로 사용하는 것이 좋음( 특히 dataframe 시 필수 )

  

# 함수

>가변 매개변수

  

def name ( parameter , ... , * parameter )

#가변 매개 변수 앞에는 기본 매개 변수 X

  

>기본 매개 변수

  

def name ( a , b, c )

#키워드 매개변수

def name ( a=2 , b=2 , c=2 ) 와 같은 형태

  

> 재귀 함수

>

memoization(dictionary 에 특정 값을 넣어둔다던지 ) 을 필수로 생각하고 있어야 한다.

많은 연산이 필요한 경우 중복으로 발생 가능

  

# Lambda

함수를 간단하게 구현

  

lambda 매개변수 : return v값

lambda x : x**2

map(int , input().split() )

filter ( lambda x > 3 , [1,2,3,4,5] )

  
  

# Zip

  

- iterable한 Object를 parameter로 받고 원소를 차례로 접근할 수 있는 iterator 반환

`numbers = [1, 2, 3]

letters = ["A", "B", "C"]

for pair in zip(numbers, letters)`

- 이를 이용하여 행렬 전환 가능

`list(map(list , zip ( * data) ) )`

- Dictionary 용이

`dict(zip(key , value ))`

주의 사항 => iterable한 Object 길이가 다르면 짧은거를 기준

  

## Rjust / Ljust / Zfill

  

Rjust = 오른쪽 정렬 / 총 n 개를 나머지 값을 data로 채운다

`str.rjust( n , data)`

` "33".rjust( 5 , "0") `

-> 00033

  
  

Zfill = 0을 왼쪽으로 채워주는 역할

`str.zfill( n )`

`"123".zfill(5)` -> 00123

  
  

## Sorted / reversed

reversed 는 결과가 **generator**로 한번 호출한 값은 다시 호출이 불가능

Why ? python은 memory를 우선하기 위해 주소값 접근 후 next() 함수를 이용하여 접근

```
sorted( iterator , key = lambda x : ( - x[0] , x[1] ) )
reversed( iterator )
b = reversed([1,2,3,4])

#호출 가능
for i in b :
	print ( i )
# 호출 불가
for i in b :
	print ( i )
```

## Map / filter / reduce

  

Map = list의 element에 함수를 적용

map(function_to_apply, list_of_inputs)

`items = [ 1 , 2 , 3 , 4 , 5 ]`

`list ( map( lambda x : x **2 , items) )`

  

filter = list의 element에서 함수 조건에 일치하는 값만 추출

`list ( filter ( lambda x: x>3 , items )`

  

reduce = list의 computation 결과 축약

`reduce( (lambda x,y : x+y) , items )`

  
  

# isdigit() / isalpha() / isalnum()

isdigit() = 문자열이 숫자인지

isnumberic() = 숫자처럼 생긴 글자

isdecimal() = int 타입 가능한 문자

  

isalpha() = 문자열이 문자로만 이루어진지

isalnum() = 문자열이 영어,한글,숫자로만

  

# 이진 / 자릿수 올림 내림

bin(number) `bin(10)[2:] -> 1010`

math.ceil(number) : 올림

math.floor(number) : 내림

math.trunc(number) : 버림

  

2의 N제곱

  

1<<N # Left shit를 이용

  

# Iterator

List / Dictionary /

# Generator
python의 특수한 문법 구조로 iterator를 직접 만들 때 사용
yield keyword로 iterator와 generator를 구별할 수 있다.
```
def test() :
    print('test1')
    yield 'check1'
    print('test2')
    yield 'check2'

temp = test()
print( 'step1')
a = next(temp)
print(a)
print( 'step2' )
b = next(temp)
print(b)
```
  

# combination / permutation

> permutation = 순열로써, 순서까지도 생각될 때

>

nPr = n!/(n-r)!

>combination 조합로써 순서는 생각 X

>

nCr=nPr/r!

  

from itertools import permutations

from itertools import combinations

a = [1,2,3]

permutations ( a, 2 )

combinations(a,2)

  
  

# stack

FIFO 형태로 한쪽으로 쌍 찾는 문제에서 주로 사용

List를 이용하여 풀면 된다.

쌍을 찾거나 갯수 세는데 주로 사용

  

# Queue , Deque

pop , append O(1)
VFS에 주로 사용되면 단계로 진행되는 탐색에서 주로 사용

시작점을 모두 deque에 넣는게 특징

```
from collections import deque
VFS에 사용
```

# Tree

  

# Heap

이진 트리로써 파이썬에서 제공하는 Heapq는 Minheap

````
import heapq
heap = []
#push O(logN)
heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 7)
heapq.heappush(heap, 3)
print(heap) # [1, 3, 7, 4]

#Pop O(logN)
heapq.heappop(heap)
 
# heap 만들기 O(n)
heap = [4, 1, 7, 3, 8, 5]
heapq.heapify(heap)

# max heap
nums = [4, 1, 3, 8, 5]
heap = []
for num in nums:
	heapq.heappush(heap, (-num, num)) # (우선 순위, 값)

while heap:
	print(heapq.heappop(heap)[1])
````

# Counter

  

````
from collections import Counter
Counter1 = Counter(str1_lst)
Counter2 = Counter(str2_lst)

inter = list((Counter1 & Counter2).elements()) # 교집합 중복 값 포함
union = list((Counter1 | Counter2).elements()) # 합집합 중복 값 포함
str1 = 'FRANCE'
str1_data = []

for i in range ( len(str1) - 1 ) :
	str1_data.append( str1[i]+str1[i+1] )
print ( str1_data) # ['FR', 'RA', 'AN', 'NC', 'CE']
print ( Counter(str1_data) ) # Counter({'FR': 1, 'RA': 1, 'AN': 1, 'NC': 1, 'CE': 1})
print ( Counter(['FR'])) # Counter({'FR': 1})
print ( Counter(str1_data)&Counter(['FR','DD']) )

  

````

  

# * 연산자 / *args / **kargs

  

-* operator = Packing

List를 한번에 나타날 경우에도 사용한다.

```
T1 = [[0]*N]*M
T2 = [[0] for M _ range ( M ) ]
위 둘의 차이는 ?
-> T1 = Packing 되어 동일한 Memory 값을 바라보게 된다.
-> T2 = 각각이 다른 list Object이기 때문에 다른 값 설정 가능하다.

arr = [1,2,3]
[*arr ] -> [1,2,3] 으로 표현 가능

# 참조 : https://pythontutor.com/visualize.html#mode=display
```

- *args

```

Tuple을 Object로 받아 사용

```

- **kargs

```

Dictionary를 Object로 받아 사용

```

  
  

# decorator

- other function을 조작하여 new function을 생성

- 코드를 간결하게 해준다 ( refactoring )

-

  

참고 https://3months.tistory.com/344?category=753896

  # 정렬
## Python Sort ( timsort )
>MergeSort + InsertSort => Stable Sort , O(NlogN ) 빠르면 O(N)을 보장

구현시 주의점
- sort는 같은 우선순위 비교 시 False !


###  Merge Sort
- 나누는 경우 N -> 1 O(N)
- 병합하는 경우 1 -> N O(NK) = O(NlogN)
- 공간 복잡도 = O(N)
- Stable Sort ( 같은 값이라 하여도 순서를 보장 )
- Comparsion sort (값을 비교 )
```
arr = [ 3 , 2 , 116 ,7 , 62 , 235 , 1 , 23 , 55 , 77]
n = len(arr)
temp_arr = [0] * n

def merge( start , end ) :
    mid = ( start + end ) // 2
    left_idx = start
    right_idx = mid 

    for i in range( start , end ) :
        if right_idx == end :
            temp_arr[i] = arr[left_idx]
            left_idx += 1
        elif left_idx == mid or arr[left_idx] > arr[right_idx]:
            temp_arr[i] = arr[right_idx]
            right_idx += 1
        else:
            temp_arr[i] = arr[left_idx] 
            left_idx += 1

    arr[start:end] = temp_arr[start:end]

def merge_sort ( start , end ) :
    # 재귀 end조건
    if end == start + 1 : 
        return
    mid = ( start + end ) // 2
    merge_sort( start , mid )
    merge_sort( mid , end )
    merge(start,end) 

merge_sort( 0 , 3 )
print ( arr )

```
### Quick Sort
- 실제 구현은 Merge sort로 하는게 재귀적으로 표현하기 쉽다.
- pivot 이라는 기준점을 잡은 뒤 좌 -> 우 / 우 -> 좌
- 평균적(중간쯤 오는 경우)으로 O(NlogN) But !! 최악 O(N^2)
- 공간 복잡도 = O(1)라이브러리 내에서 퀵소트는 피벗 후보를 3개 중 중앙값 / 일정 Depth 이상 들어가면 힙소트로 구현되도록 되어있다 -> introspective sort
- Comparsion sort (값을 비교 )
```
arr = [ 3 , 2 , 116 ,7 , 62 , 235 , 1 , 23 , 55 , 77]
def Quicksort( start ,end ) :
    #재귀 종료
    if end == start + 1 : return

    pivot = arr[start]
    left = start+1 
    right = end
    while ( True ) :
        # 1. 좌 -> 우
        print (pivot , left , right )
        while( left <= right and arr[left] <= pivot ) : left += 1
        # 2. 우 -> 좌
        while( left <= right and arr[right] >= pivot ) : right -= 1
        # 4. right < left 종료 조건
        if right < left :
            break
        # 3. 둘다 멈추면 swap
        arr[left] , arr[right] = arr[right] , arr[left]
    arr[start] , arr[right] = arr[right] , arr[start]    
    
    #재귀 이용
    Quicksort( start , right )
    Quicksort( right + 1 , end )
    
Quicksort( 0 , 3 )     
print ( arr )
```
### counting sort
- 미리 값의 범위를 지정하고 공간을 이용하여 접근 ( 한정적인 경우에만 )
- Non-Comparsion sort ( 값을 비교 X )
```
N = int ( input() )

#Counting sort
arr = [0] * ( 2000001 )
for i in range( N ) :
    temp = int ( input() )
    temp += 1000000
    arr[temp] += 1

#print ( '-' * 10)
for i in range( 2000001 ) :
    while arr[i] :
        print ( i - 1000000 )
        arr[i] -= 1
```

### radix sort
- 1 의 자리  -> 10의 자리 -> ... 자리 수  별로 0 - 9 계속하여 정렬
- counting sort를 N자리수로 한것과 같다고 생각하면 된다.
- Non-Comparsion sort ( 값을 비교 X )

# 시뮬레이션

  

> BOJ 15683과 같이 특정 단계에서 경우의 수를 permutation과 같이 나타내서 check가 필요한 경우 ( 삼성 아카데미 기출 문제 )

-> 경우의 수를 bit 형태로 나누어 푼다. / https://www.acmicpc.net/problem/15683

10진법인 경우
3491 -> 349 -> 34 -> 4
1 / 9 / 4 / 3

4진법인 경우
39 -> 9 -> 2
3 / 1 / 2
```
def all_target ( N ) : #N진법 경우의 수 나타내기
answer = []
for i in range ( 1<<2*N ) :
	temp = i
	target_data = ''
	for j in range( N ) :
		target_data = str ( temp % 4 ) + target_data
		temp //= 4
		answer.append( target_data )

return answer
```

# 예외처리
### syntax Error
- 구문 자체 오류
### Exception
Finally 
-	주로 service , daemon 에서 connection 연결 끊을 때 사용
-	Try Logic 내에 return 값이 있더라도 Finally logic은 실행이 된다.
```
try:
	예외 발생 가능성
except :
	예외 발생 실행
else:
	예외 발생하지 않았을 때
finally:
	무조건 실행
```


# File

> stream = 외부 파일 및 네트워크와 통신 할 때 흐르는 길이라고 생각하면 된다.

>

  
  

> Text file

>

  
```
fileobject = open ( 'foo.txt' , 'rw+' )
with open ( 파일경로 , 모드 ) as object :
	code

fileobject.close()
fileobject.write()
fileobject.read()
```
  

> Binary file