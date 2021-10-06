# 기초문법 정리

# Lambda
함수 = class를 통해 생성된 Object
`def function(parameter) :
	return 결과`
	-> 
	`labmda parameter : 결과`

# Or
무조건 | 로 사용하는 것이 좋음( 특히 dataframe 시 필수 )

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

sorted( iterator , key = lambda x : ( - x[0] , x[1] ) )
reversed( iterator )

## Dictionary get() / keys() / values() /items()
key가 없다면 뒤 파라미터 값으로 return
`Data = {'a' : 1 , 'b' :2 }`
`Data.get('a' , 'no_data')`
-> 1
`Data.get('c' , 'no_data')`
-> no_data
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

# 이진
bin()

# combination / permutation

# stack

# Tree

# Heap

# * 연산자 / *args / **kargs

# decorator
- other function을 조작하여 new function을 생성
- 코드를 간결하게 해준다 ( refactoring )
-

참고 https://3months.tistory.com/344?category=753896