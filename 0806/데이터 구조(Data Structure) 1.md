# 데이터 구조(Data Structure) 1

> 데이터에 편리하게 접근, 변경하기 위해 데이터를 저장하거나 조작하는 방법

## 문자열(String)

> 변경x(immutable) / 순서o(ordered) / 순회o(iterable)

### 조회/탐색

#### .find(x)

* x의 첫 번째 위치를 반환
* 없으면, -1을 반환

```python
'apple'.find('p')  -> 1
```

#### .index(x)

* x의 첫 번째 위치를 반환
* 없으면, 오류

```python
'apple'.index('p')  -> 1
'apple'.index('k')  -> 에러
```

### 값 변경

#### .replace(old, new[, count])

* 바꿀 글자를 새로운 글자로 바꿔서 반환
* count -> 해당 갯수만큼 시행

```python
'wooooowoo'.replace('o', '', 2)  -> 'wooowoo'
```

#### .strip([chars])

* 특정 문자 기준, 양쪽을 제거
* 왼쪽 제거(lstrip), 오른쪽 제거(rstrip)
* 지정x -> 공백 제거
* 양쪽 끝에 해당 문자가 있으면 제거, 없으면 제거x

```python
'    oh!\n'.strip()  -> 'oh!' (지정x->공백제거)
'hehehihihihihi'.rstrip('hi')  -> 'hehe'
```

#### .split()

* 문자열을 특정 단위로 나눠 리스트로 반환

```python
'a_b_c'.split('_')  -> ['a', 'b', 'c']

inputs = input().split()  -> 5 3
print(inputs)  -> ['5', '3']
```

#### 'seperator'.join(iterable)

* 특정 문자열 반환
* iterable한 컨테이너의 요소들을 seperator를 구분자로 합쳐 문자열로 반환

```python
'!'.join('안녕')  -> '안!녕'

'!'.join(['1', '2', '3', '4', '5'])  -> '1!2!3!4!5'
'!'.join([1, 2, 3, 4, 5])  -> 에러남, 숫자는 iterable 하지 않음

```

### 문자 변형

#### .capitalize()

* 앞글자를 대문자로 만들고 반환

#### .title()

* ' 나 공백 이후를 대문자로 만들고 반환

#### .upper()

* 모두 대문자로 만들고 반환

```python
a = 'hi! Everyone. I\'m kim.'

a.capitalize()  -> Hi! everyone, i'm kim. (앞글자 h만 변형)
a.title()  -> Hi! Everyone, I'M Kim. (제일 앞글자도 되는듯..? ''이거 뒤라서 그런가...?)
a.upper()  -> HI! EVERYONE, I'M KIM.
print(a)  -> hi! Everyone. I\'m kim (변형시키고 반환만 하기 때문에 a는 그대로)
```

#### .lower()

* 모두 소문자로 만들고 반환

#### .swapcase()

* 대소문자 변경 후 반환

```python
a = 'hi! Everyone. I\'m kim.'

a.lower()  -> hi! everyone, i'm kim.
a.swapcase()  -> Hi! eVERYONE, i'M KIM.
```

### 문자열 관련 검증 메소드 : 참/거짓 반환

#### .isalpha()

* 문자열이 문자인지 검증 후 True/False로 반환

#### .isdecimal()

* 문자열이 숫자인지 검증 후 True/False로 반환
* 음수는 False

#### .isdigit()

* 0~9 사이의 숫자로 이루어진 문자열인지 검증 후 True/False로 반환

#### .isnumeric()

* 문자열이 숫자인지 검증 후 True/False로 반환
* 지수도 가능
* 음수는 False

#### .isspace()

* 문자열이 공백으로만 되어있는지 검증 후 True/False로 반환

#### .isupper()

* 문자열이 모두 대문자로만 되어있는지 검증 후 True/False로 반환

#### .istitle()

* 문자열이 대문자로 시작하고 이후로는 소문자인지 검증 후 True/False로 반환

#### .islower()

* 문자열이 모두 소문자로만 되어있는지 검증 후 True/False로 반환

```python
a = 'Hello '
b = '3.5'  -> 문자열을 검증하므로 ''안에 넣어줘야함

print(a.isalpha())  -> False (공백 포함하기 떄문)
print(b.isdecimal())  -> False
print(b.isdigit())  -> False
print(b.isnumeric())  -> False
print(a.isspace())  -> False
print(a.isupper())  -> False
print(a.istitle())  -> True
print(a.islower())  -> False
```

## 리스트(List)

> 변경o(mutable) / 순서o(ordered) / 순회o(iterable)

### 값 추가 및 삭제

#### .append(x)

* 리스트에 값 추가

```python
a = ['a', 'b', 'c', 'd']
print(a.append('e'))  -> None (append 함수는 반환값x, 변형만 해주는거)
print(a)  -> ['a', 'b', 'c', 'd', 'e']
```

#### .extend(iterable)

* 리스트에 **iterable 값**(list, range, tuple, string) 추가

```python
a = ['a', 'b', 'c', 'd']
b = ['a', 'b', 'c', 'd']

a.extend(['e'])
a.extend('f')
a.extend(['gh'])
a.extend('ij')
b.append(['e'])
b.append('fg')

print(a)  -> ['a', 'b', 'c', 'd', 'e', 'f', 'gh', 'i', 'j']
print(b)  -> ['a', 'b', 'c', 'd', ['e'], 'fg']
```

#### .insert(i, x)

* 위치 i에 x 값을 추가
* 리스트 길이를 넘어서는 인덱스는 마지막에 추가

```python
a = ['a', 'b', 'c', 'd']
a.insert(0, 'z')
a.insert(len(a), 'y')
print(a)  -> ['z', 'a', 'b', 'c', 'd', 'y']
```

#### .remove(x)

* 리스트에서 값이 x인 것 삭제
* 지울 값이 없으면 오류 발생

```python
a = ['a', 'b', 'c', 'd', 'a', 'b']
a.remove('a')
print(a)  -> ['b', 'c', 'd', 'a', 'b'] (하나만 삭제)
a.remove('a')
print(a)  -> ['b', 'c', 'd', 'b']
```

#### .pop(i)

* 위치 i에 있는 값 삭제  후 그 항목 반환
* i 지정하지 않으면 마지막 항목 삭제 후 반환

```python
a = ['a', 'b', 'c', 'd']
print(a.pop(0))  -> a
print(a)  -> ['b', 'c', 'd']
```

#### .clear()

* 리스트 내 모든 항목 삭제

```python
a = ['a', 'b', 'c', 'd']
a.clear()
print(a)  -> []
```

### 탐색 및 정렬

#### .index(x)

* x 값을 찾아 해당 인덱스 값을 반환

```python
a = ['a', 'b', 'c', 'd']
print(a.index('b'))  -> 1
print(a)  -> ['a', 'b', 'c', 'd']
```

#### .count(x)

* 해당 값의 개수를 확인

```python
a = ['a', 'b', 'c', 'd', 'a', 'b']
print(a.count('b'))  -> 2

# 해당 값 모두 삭제
a = ['a', 'b', 'c', 'd', 'a', 'b']
target_value = 'a'
for i in range(a.count('a')):
    a.remove(target_value)
    
print(a)  -> ['b', 'c', 'd', 'b']
```

#### .sort()

* 정렬
* 내장함수 sorted() 와는 다르게 **원본을 변형**시키고 **None을 반환**

```python
a = ['z', 'c', 'a', 'r', 'v']
a.sort()
print(a)  -> ['a', 'c', 'r', 'v', 'z']
```

#### .reverse()

* 반대로 뒤집기
* **정렬 아님**

```python
a = ['a', 'b', 'c', 'd', 'e']
a.reverse()
print(a)
```

### 데이터의 분류

`mutable` vs `immutable`

#### 변경 불가능한(immutable) 데이터

* 단일 데이터(숫자, 글자, 참/거짓)
* range()
* tuple()
* frozenset()

#### 변경 가능한(mutable) 데이터

* list
* dict
* set

### 리스트 복사 방법

#### (1) slice 연산자 사용 [:]

```python
a = [1, 2, 3]
b = a[:]  -> 원본 변경 x, 새로운 값 반환
```

#### (2) list() 활용

```python
a = [1, 2, 3]
b = list(a)
```

```python
a = [1, 2, [1, 2]]
b = a[:]

b[2][0] = 3
print(a)  -> [1, 2, [3, 2]] (얕은 복사 - 중첩된 상황(내부 객체)에서는 불가)
```

#### (3) 깊은 복사

```python
import copy

a = [1, 2, [1, 2]]
b = copy.deepcopy(a)

b[2][0] = 3
print(a)  -> [1, 2, [1, 2]]
```

### List Comprehension

* 표현식과 제어문을 통해 리스트 생성

* 한 줄로 표현 가능

* `[식 for 변수 in iterable]`

  `list(식 for 변수 in iterable)`

```python
numbers = range(1, 11)
cubic_list = [number ** 3 for number in numbers]
```

### List Comprehension + 조건문

* 조건문에 참인 식으로 리스트 생성

* `[식 for 변수 in iterable if 조건식]`

  `[식 if 조건식 else 식 for 변수 in iterable]`

  `[식 if 조건식 else 식 if 조건식 else 식 if ... else ... for 변수 in iterable]`

##### 짝수리스트

```python
even_list = [number for number in range(1, 11) if number%2==0]
print(even_list)  -> [2, 4, 6, 8, 10]
```

##### 곱집합

```python
girls = ['jane', 'ashley', 'mary']
boys = ['justin', 'eric', 'david']

pair = [(i,j) for i in boys for j in girls]
print(pair)  -> [('justin', 'jane'), ('justin', 'ashley'), ('justin', 'mary'), ('eric', 'jane'), ('eric', 'ashley'), ('eric', 'mary'), ('david', 'jane'), ('david', 'ashley'), ('david', 'mary')]
```

##### 피타고라스 정리

```python
result = [(x, y, z) for x in range(1, 50) for y in range(1, 50) for z in range(1, 50) if (x**2)+(y**2)==(z**2) and x<y<z]
print(result)
```

##### 모음 제거하기

```python
result = [w for w in words if w not in vowels]
for i in result:
    print(i, end='')
```

### 데이터 구조에 적용가능한 Built-in Function

* 순회가능한(iterable) 데이터 구조에 적용
* `list`, `dict`, `set`, `str`, `bytes`, `tuple`, `range`

#### map(function, iterable)

* 모든 요소에 function을 적용
* return : `map_object`형태

```python
numbers = [1, 2, 3]
result = list(map(str, numbers))
print(result)
```

#### filter(function, iterable)

* iterable에서 function의 반환된 결과가 `True`인 것들만 구성하여 반환

```python
# 홀수 판별
def odd(n):
    return n % 2

numbers = [1, 2, 3]
new_numbers = list(filter(odd, numbers))
print(new_numbers)  -> [1, 3]
```

#### zip(*iterables)

* 복수의 iterable 객체를 모아줌
* 결과 : 튜플의 모임

```python
girls = ['jane', 'ashley', 'mary']
boys = ['justin', 'eric', 'david']

pair = list(zip(girls, boys))
print(pair)  -> [('jane', 'justin'), ('ashley', 'eric'), ('mary', 'david')]
```









