# 알고리즘(Algorithm Problem Solving)

: 어떠한 문제를 해결하기 위한 절차

  => 컴퓨터가 어떤 일을 수행하기 위한 단계적 방법

#### 시간 복잡도(Time Complexity)

> 알고리즘의 작업량을 표현할 때 사용

* 실제 걸리는 시간을 측정
* 실행되는 명령문의 개수를 계산

**빅-오(Big-O) 표기법**

* 가장 큰 영향력을 주는 n 항만 표시

* 계수 생략

  ex) O(2n² + 10n +100) = O(n²) / O(4) = O(1)



### 배열(Array)

> 일정한 자료형의 변수들을 하나의 이름으로 열거하여 사용하는 자료구조

**1차원 배열** 

선언 : `Arr = list()`   `Arr[]`

접근 : `Arr[idx]=10`



### 완전 검색 (Exaustive Search)

> 문제의 해법으로 생각할 수 있는 모든 경우의 수를 나열, 확인하는 기법



### 탐욕 알고리즘 (Greedy Algorithm)

> 최적해를 구하는데 사용되는 근시안적인 방법

**동작 과정**

1. 해 선택 : 부분 문제의 최적 해를 구해 부분해 집합(Solution Set)에 추가
2. 실행 가능성 검사 : 부분해 집합이 실행 가능한지 확인
3. 해 검사 : 부분해 집합이 문제의 해가 되는지 확인, 전체 문제의 해가 완성되지 않았다면 1번 부터 다시 시작



### 정렬(Sort)

> 자료를 특정 기준에 의해 오름차순/내림차순으로 재배열하는 것

* 키 : 정렬 기준이 되는 특정 값

#### 버블 정렬 (Bubble Sort) 

: 인접한 두 개의 원소를 비교하며 자리를 계속 교환하는 방식

* O(n²)

```python
num = [6, 4, 1, 5, 2, 3]

def BubbleSort(n):
    for i in range(len(n)-1, 0, -1):
        for j in range(i):
            if n[j] > n[j+1]:
                n[j], n[j+1] = n[j+1], n[j]
    return n

print(BubbleSort(num))  -> [1, 2, 3, 4, 5, 6]
```

#### 카운팅 정렬 (Counting Sort) 

: 집합에 각 항목이 몇 개씩 있는지 세어 선형 시간에 정렬하는 효율적인 알고리즘

* O(n+k) _ n : 리스트 길이, k : 정수 최대값

**제한 사항**

* 정수(or 정수로 표현 가능한 자료)에만 적용 가능
* 카운트를 위한 공간 할당을 위해 가장 큰 정수를 알아야 함

```python
num = [0, 4, 1, 3, 1, 2, 4, 1]


def CountingSort(a):
    temp = [0] * len(a)
    a_set = set(a)
    count = len(a_set)
    counts = [0] * count

    for i in range(len(a)):
        counts[a[i]] += 1

    for i in range(1, len(a_set)):
        counts[i] += counts[i - 1]

    for i in range(len(a) - 1, -1, -1):
        counts[a[i]] -= 1
        temp[counts[a[i]]] = a[i]

    return temp


print(CountingSort(num))  -> [0, 1, 1, 1, 2, 3, 4, 4]
```



### 2차 배열

> 1차원 List를 묶어놓은 List

**2차원 배열의 접근**

* 배열 순회

  : 모든 원소를 조사하는 방법

* 행 우선 순회

* 열 우선 순회

* 지그재그 순회

  ```python
  Array = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
  
  for i in range(len(Array)):
      for j in range(len(Array[0])):
          print(Array[i][j + (len(Array[0])-1-2*j) * (i%2)], end=" ")  -> 1 2 3 4 8 7 6 5 9 10 11 12
  ```

* 델타를 이용한 2차 배열 탐색

  ```python
  dx = [0, 0, -1, 1]  # 상하좌우
  dy = [-1, 1, 0, 0]
  ```

**2차원 배열의 활용**

* 전치 행렬

  ```python
  Array = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
  
  for i in range(len(Array)):
      for j in range(len(Array[0])):
          if i < j:
              Array[i][j], Array[j][i] = Array[j][i], Array[i][j]
  
  print(Array)  -> [[1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 16]]
  ```



### 부분집합 합(Submit Sum)

집합의 원소가 n개일 때 부분집합의 수 : 2^ n

**비트연산자**

* `& `: 비트 단위로 AND 연산
* `|` : 비트 단위로 OR 연산
* `<<` : 피연산자의 비트 열을 왼쪽으로 이동
* `>>`: 피연산자의 비트 열을 오른쪽으로 이동

**`1<<n`** : 원소가 n개인 집합의 모든 부분집합의 수

**`i&(1<<j)`** : i의 j번째 비트가 1인지 아닌지 리턴

```python
a = len(array)

for i in range(1<<a):
    for j in range(a+1):
        if i & (1<<j):
            print(array[j], end=", ")
    print()
print()
```

### 검색

**순차 검색(sequential search)**

> 일렬로 되어 있는 자료를 순서대로 검색하는 방법

* O(n)

**이진 검색(binary search)**

> 자료의 중앙 항목의 키 값과 비교한 뒤 다음 검색 위치를 결정하는 방법

* 자료가 정렬된 상태에서 가능

```python
array = [23, 7, 9, 11, 2, 19, 4, 5, 29, 16]
l = len(array)

# array 정렬
for i in range(l-1):
    for j in range(0, l-1-i):
        if array[j+1] < array[j]:
            array[j], array[j+1] = array[j+1], array[j]

# 이진 검색

def binarySearch(n, li):
    start_n = 0
    end_n = l - 1
    cnt = 0

    while start_n <= end_n:
        middle_n = (start_n + end_n)//2
        if n < li[middle_n]:
            end_n = middle_n-1
            cnt += 1
        elif n > li[middle_n]:
            start_n = middle_n+1
            cnt += 1
        else:
            cnt += 1
            return cnt
    return '검색 실패'

print(binarySearch(50, array))  -> 검색 실패
print(binarySearch(23, array))  -> 3
```



### 셀렉션 알고리즘(Selection Algorithm)

















 





