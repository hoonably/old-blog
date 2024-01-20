---
title: "[백준] [Python] 🧩 N-Queen (Easy) 30242번"	#대괄호를 쓰려면 ""로 감싸주면 된다.
date: 2024-01-07 01:50:00 +09:00

categories: [Baekjoon, Gold]

# Algorithm : 시간복잡도, 자료구조, 정렬, 탐색, 백트래킹, 탐욕알고리즘, 정수론, 그래프, 트리, 조합, 다이나믹프로그래밍
# Language : Java, Python, C++
# Blog : Markdown, Just_blog
# Baekjoon : Bronze, Silver, Gold, Platinum, Diamond, Ruby

tags: [Algorithm, Baekjoon, Python, 백트래킹]

# Algorithm, Baekjoon, Python, Java, DB, Blog
# 백트래킹

image: https://github.com/hoonably/hoonably.github.io/assets/77783081/a773640b-78c4-45a6-91f0-62a8604a5958
# 링크 달면 됨

---

<br/>

## 💡 문제 설명

---

[🧩 N-Queen (Easy)](https://www.acmicpc.net/problem/30242){:target="_blank"}

<img width="1132" alt="image" src="https://github.com/hoonably/hoonably.github.io/assets/77783081/15d1d8b6-3e2d-4942-97da-088bbf7e23cf">

전에 했던 문제와 다르게, 이미 퀸이 놓여져 있을 수 있다.

그리고, 한번의 가능한 경우일때 퀸들의 자리를 출력하면 되는 문제다.

전형적인 백트래킹 문제로, 이 문제도 꼭 풀어보면 좋다.

<br/>



## 💡 느린 풀이 (통과는 받음)

---

이 풀이법은 보통 백트래킹을 통해 n-queen을 푼다면 풀어보는 문제다.

대입을 해준 후 check할때마다 가로, 세로, 대각선에 겹치는게 있는지 확인해준다.

여기서 quit() 는 아예 프로그램을 종료시켜준다.

```python
import sys


def q_check(x):
    # 이미 기록된 0 ~ N 범위 보기
    for i in range(N):

        # 본인 단계 제외
        if i==x:
            continue

        # 아직 안쓴거는 대각선 영향갈수있으니 제외
        if row[i]==0:
            continue

        # row (가로)체크
        # 체크하려는 row == 기록된 row(q_list[i]) 일때 False
        if row[x] == row[i]:
            return False
        # 대각선 체크
        # 체크하려는 row 와 이미 기록된 row 의 차가
        # 체크하려는 column 과 기록된 column 의 차랑 같다면 대각선이니 False
        if abs(row[x]-row[i]) == abs(x-i): # abs() = 절댓값 함수
            return False
    # 두 경우 다 피해가면 True
    return True


def n_queen(n):
    # 끝까지 완성한 경우
    if n==N:
        print(*row)
        quit() # 아예 종료

    # 이미 써있는경우 바로 다음단계로
    if row[n]!=0:
        n_queen(n+1)
        return

    # 1부터 N까지 넣어보기
    for i in range(1,N+1):
        # 해당 숫자를 사용하지 않았을 때만 넣기
        if visited[i] == False:
            temp = row[n]
            row[n] = i
            if q_check(n):
                visited[i]=True
                n_queen(n+1)
                visited[i]=False
            row[n] = temp

N = int(sys.stdin.readline())
row = list(map(int, sys.stdin.readline().split()))
visited = [False] * (N+1)

# 이미 놓아진 퀸의 값
for i in range(N):
    if row[i] != 0:
        visited[row[i]] = True

n_queen(0) # 0번째 줄부터 함수 실행
print(-1)

```





<br/>

## 💡 더 빠른 풀이법

---

이전의 글을 보면 알 수 있지만, 확인하는 과정에서 for문을 사용하지 않고, 바로 확인 할 수 있다.

이전의 글을 보지 않았다면 아래로 내려가 설명을 보자.

```python
import sys

def backtracking(n):

    # 다 도달했을 때
    if n==N:
        print(*arr)
        quit()

    # 이미 써있는경우 바로 다음단계로
    if arr[n] != 0:
        backtracking(n + 1)
        return

    for i in range(N):
        # 놓을 수 있으면
        if row[i] and x1[i+n] and x2[i+((N-1)-n)]:

            arr[n] = i+1
            row[i]=False # 가로줄 제거
            x1[i+n]=False # 오른쪽 위 방향 대각선 제거
            x2[i+((N-1)-n)]=False # 오른쪽 아래 방향 대각선 제거

            # 자식 노드로 이동
            backtracking(n+1)

            # 백트래킹
            row[i]=True
            x1[i+n]=True
            x2[i+((N-1)-n)]=True
            arr[n] = 0

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

row = [True]*N # 가로
x1 = [True]*(2*N) # 제일 왼쪽이 인덱스인 우상향 대각선
x2 = [True]*(2*N) # 제일 오른쪽이 인덱스인 우하향 대각선

for i in range(N):
    if arr[i] != 0:
        row[arr[i]-1] = False  # 가로줄 제거
        x1[arr[i]-1 + i] = False  # 오른쪽 위 방향 대각선 제거
        x2[arr[i]-1 + ((N - 1) - i)] = False  # 오른쪽 아래 방향 대각선 제거

backtracking(0)
print(-1)

```

<br/>

### ❗row[] : 가로 줄

row는 간단하게 가로에 겹치는게 있으면 안되므로, 해당 row를 사용했으면 False로 바꿔주기만 하면 된다.



### ❗x2[] : 우하향 대각선

`x2`는 **오른쪽 아래**로 가는 대각선을 뜻하고, 총 **2*N** 개가 나올 수 있다.

각 대각선들은 **가장 오른쪽에 갔을때** index를 기준으로 삼았다.

그림은 0, 1 단계를 마치고 **2단계**의 for문에서 **i=3**일때 우하향 대각선이 겹치지 않는지를 보는 것이다.

![N - Queen-1](https://github.com/hoonably/hoonably.github.io/assets/77783081/258c1afb-5fa8-493c-9e1a-a87c6c12f16c)

그렇다면 n 단계의 for문의 i번째 row일때 생기는 **우하향** 대각선은 **맨 오른쪽**으로 가면

`i + (마지막 단계 - 지금 단계)` 가 된다.

그러므로 놓았을때는

```python
x2[i+((N-1)-n)] = False 로 바꿔주어 대각선이 사용되었음을 나타내면 된다.
```

들어갈 수 있는지 체크할때는 

```python
x2[i+((N-1)-n)] 가 True면 겹치지 않고, False면 겹쳐서 불가능 한것이다.
```



<br/>

### ❗x1[] : 우상향 대각선

x2를 이해했다면 x1은 자동으로 이해된다. 

차이점은 **x2**는 **가장 오른쪽**이 기준이었다면, **x1**은 **가장 왼쪽**이 기준이다.

그렇다면 n 단계의 for문의 i번째 row일때 생기는 **우상향** 대각선은 **맨 왼쪽**으로 가면

`i + (지금 단계)` 가 된다.

그러므로 놓았을때는

```python
x1[i+n] = False 로 바꿔주어 대각선이 사용되었음을 나타내면 된다.
```

들어갈 수 있는지 체크할때는 

```python
x1[i+n] 가 True면 겹치지 않고, False면 겹쳐서 불가능 한것이다.
```

<br/>



## 💡 제출 결과 

---

아래의 풀이가 느렸던 첫번째 방식이고, 위의 풀이가 더 빠른 풀이이다.

<img width="1045" alt="image" src="https://github.com/hoonably/hoonably.github.io/assets/77783081/216ec727-eb71-4e59-9c9c-67b13a333bcd">

<br/>



## 💡 마무리 

---

지난번의 N-Queen 문제보다 재미있었다. 미리 Queend의 값을 받는 점이 흥미로웠고,

하나의 답만 나오면 출력해주어서 오류가 있을 때 어디서 발생했는지 보기 편했다.

나중에 [🧩 N-Queen (Hard)](https://www.acmicpc.net/problem/30243){:target="_blank"} 를 풀어보겠다. (참고로 C++로 풀었다.)



<br/>
