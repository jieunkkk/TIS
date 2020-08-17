# 데이터 구조(Data Structure) 2

> 순서가 없는(unordered) 데이터 구조
>
> * 세트(Set)
> * 딕셔너리(Dictionary)

## 세트(Set)

> 변경o(mutable), 순서x(unordered), 순회o(iterable)

* 순서가 없다.

```python
a = {'a', 'b', 'c', 'd'}
print(a)  -> {'c', 'a', 'd', 'b'}
```

* 중복 허용 x

```python
sample_set2 = {1, 2, 3, 4, 5, 1, 2, 3}
print(sample_set2)  -> {1, 2, 3, 4, 5}
```

* immutable한 요소만 추가/수정 가능

```python
sample_set3 = {1, 'a', (1, 3)}  -> 리스트([1, 2])같은 mutable한 요소 추가하면 에러
print(sample_set3)
```

### 추가 및 삭제

#### .add(elem)

* elem을 세트에 추가

```python
a = {1, 2, 3}
a.add(4)
print(a)  -> {1, 2, 3, 4}
```

#### .update(*others)

* 여러 개의 값 추가
* 인자 -> 반드시 iterable 데이터 구조

```python
a = {1, 2, 3}
a.update([4, 5], {6, 7}, (7, 8))
print(a)  -> {1, 2, 3, 4, 5, 6, 7, 8}
```

#### .remove(elem)

* elem를 세트에서 삭제
* 해당 값이 없다면 KeyError

```python
a = {1, 2, 3}
# a.remove(4)  -> KeyError
a.remove(2)
print(a)  -> {1, 3}
```

#### .discard(elem)

* elem를 세트에서 삭제
* 해당 값이 없어도 에러발생x

```python
a = {1, 2, 3}
a.discard(4)  -> 에러 발생하지 않음
a.discard(2)
print(a)  -> {1, 3}
```

#### .pop()

* 임의의 원소 제거 후 반환

```python
a = {1, 2, 3}
print(a.pop())  -> 1  -> 여기에 인자 넣으면 에러남
print(a)  -> {2, 3}
```

## 딕셔너리(Dictionary)

> 변경o(mutable), 순서x(unordered), 순회o(iterable)

* Key: Value : 페어(pair)의 자료구조

```python
a = {'1':'일','2':'이','3':'삼'}

for i in a:
    print(f'{i} {a[i]}')  -> 1 일
							 2 이
							 3 삼

for i in a.keys():
    print(i)  -> 1
				 2
				 3
    
for i in a.values():
    print(i)  -> 일
				 이
				 삼
    
for i in a.items():
    print(i)  -> ('1', '일')
				 ('2', '이')
				 ('3', '삼')
    
for i, j in a.items():
    print(i)
    print(j)  -> 1
				 일
				 2
				 이
				 3
				 삼
```

### 조회

#### .get(key[, default])

* key를 통해 value 가져옴
* 에러발생 하지 않음
* 디폴트값은 기본적으로 None

```python
a = {'1':'일','2':'이','3':'삼'}
print(a.get('4'))  -> None
print(a.get('2'))  -> 이
print(a.get('4',1))  -> 1
print(a)  -> {'1': '일', '2': '이', '3': '삼'}
```

### 추가 및 삭제

#### .pop(key[, default])

* key가 딕셔너리에 있으면 제거하고 그 값 반환
* 딕셔너리에 없으면 default 반환
* default가 없는 상태에서 key 없으면 KeyError 발생

```python
a = {'1':'일','2':'이','3':'삼'}
print(a.pop('2'))  -> 이
print(a)  -> {'1': '일', '3': '삼'}
print(a.pop('4','없음'))  -> 없음
print(a)  -> {'1': '일', '3': '삼'}
```

#### .update()

* 값을 제공하는 key, value로 덮어씀

```python
a = {'일':'1','이':'2','삼':'3'}
a.update(일='5', 사 ='4')  -> 추가도 가능
print(a)  -> {'일': '5', '이': '2', '삼': '3', '사': '4'}
```

### 딕셔너리 순회(반복문 활용)

```python
#1. dictionary 순회 (key 활용)
for key in dict:
    print(key)
    print(dict[key])
    
#2. .keys() 활용
for key in dict.keys():
    print(key)
    print(dict[key])
    
#3. .values() 활용
for val in dict.values():
    print(val)
    
#4. .items() 활용
for key, val in dict.items():
    print(key, val)
```

```python
blood_types = {'A': 40, 'B': 11, 'AB': 4, 'O': 45}
#1
for key in blood_types:
    print(f'{key}형은 {blood_types[key]}명입니다.')
    
#2
for key in blood_types.keys():
    print(f'{key}형은 {blood_types[key]}명입니다.')
    
#4
for key, value in blood_types.items():
    print(f'{key}형은 {value}명입니다.')  -> A형은 40명입니다.
										   B형은 11명입니다.
										   AB형은 4명입니다.
										   O형은 45명입니다.
```

```python
blood_types = {'A': 40, 'B': 11, 'AB': 4, 'O': 45}
#3
total = 0
for val in blood_types.values():
    total += val
print(total)  -> 100
```

#### 딕셔너리 구축하기

```python
book_title =  ['great', 'expectations', 'the', 'adventures', 'of', 'sherlock', 'holmes', 'the', 'great', 'gasby', 'hamlet', 'adventures', 'of', 'huckleberry', 'fin']

book_dict = {}
cnt = 1
for book in book_title:
    if book not in book_dict:
        book_dict[book] = cnt
    else:
        book_dict[book] += 1
        
print(book_dict)
```

```python
book_title =  ['great', 'expectations', 'the', 'adventures', 'of', 'sherlock', 'holmes', 'the', 'great', 'gasby', 'hamlet', 'adventures', 'of', 'huckleberry', 'fin']

book_dict = {}
cnt = 1

for book in book_title:
    book_dict[book] = book_title.count(book)
    
print(book_dict)
```

### Dictionary comprehension

* `{키: 값 for 요소 in iterable}`

  `dict({키: 값 for 요소 in iterable})`

```python
numbers = [1, 2, 3, 4, 5]
cubic = {n: n**2 for n in numbers}
print(cubic)  -> {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

```python
blood_types = {'A': 40, 'B': 11, 'AB': 4, 'O': 45}
neg_blood = {'-'+i: blood_types[i] for i in blood_types}
print(neg_blood)  -> {'-A': 40, '-B': 11, '-AB': 4, '-O': 45}
```

### Dictionary comprehension + 조건

* `{키: 값 for 요소 in iterable if 조건식}`

  `{키: 값 if 조건식 else 값 for 요소 in iterable}`

  * `elif`는 아래와 같이 `if else`로 쓴다.
  * `{키: 값 if 조건식 else 식 if 조건식 else 식 if ... for 변수 in iterable}`

```python
dusts = {'서울': 72, '대전': 82, '구미': 29, '광주': 45, '중국': 200}

result = {d: dusts[d] for d in dusts if dusts[d]>80}  -> {'대전': 82, '중국': 200}
print(result)

result2 = {d: '나쁨' if dusts[d]>80 else '보통' for d in dusts}
print(result2)
```



