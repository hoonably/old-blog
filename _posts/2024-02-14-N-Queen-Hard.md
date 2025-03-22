---
layout: blog
title: "[백준] [C++] 🧩 N-Queen (Hard) 30243번"
subtitle: "Diamond 5 - Bitmasking, Backtracking"
date: 2024-02-14 19:00:00 +09:00
categories: PS
author: "hoonably"
# meta: "Springfield"
---



## 💡 문제 설명


[🧩 N-Queen (Hard)](https://www.acmicpc.net/problem/30243)

<img width="971" alt="image" src="https://github.com/hoonably/hoonably.github.io/assets/77783081/b33c0c07-e88f-4a73-b035-4d5b453fc58e">

기존의 N-Queen 문제와 같지만, N<=30으로 30단계까지 가야 해서 비트마스킹 없이는 절대로 시간제한 안에 문제를 풀 수 없다.

다른 N-Queen 문제와 같이 백트래킹을 사용하면된다.




## 💡 백트래킹 방식


백트래킹과 전반적인 풀이 방식은 [🧩 N-Queen (Easy) 풀이](https://hoonably.github.io/ps/N-Queen-Easy/) 와 동일하다. 안봤다면 꼭 보고 오자.


## 💡 음수 비트연산?



중간에 for문에서 처음 보는 내용이 있을 것이다.

bit에서 최하위 비트를 하나씩 뽑아서 a로 나타내 진행한다.

```c++
// 최하위 비트부터 없애면서 모든 비트가 없어질때까지 하나씩 재귀
for(ll a=0; bit!=0; bit ^= a){
    a = bit & (-bit);  // bit의 최하위 비트
```

예시

```c++
int bit = 0b0001100100;  // bit가 0001100100 이면
int a = bit & (-bit);    // 자신의 음수값과 AND 연산을 하면
cout << "bit : " << bitset<10>(bit) << endl;  // 2진수로 bit 출력
cout << "a   : " << bitset<10>(a) << endl;  // 2진수로 a 출력

// 결과
// bit : 0001100100
// a   : 0000000100
```




## 💡 C++ 풀이



```c++
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define MAX

int N;
int row;  // 가로 (놓을 수 있는곳이 1)
ll lx, rx;  // 왼대각선, 오른대각선 (놓을 수 없는곳이 1)
int Q[30];
int step[30];
int ans[30];

bool backtracking(int level){
    if(level>N){
        return true;
    }

    // bit : 현재 단계(세로줄)에서 놓을 수 있는 row는 1, 놓을 수 앖는 row는 0
    ll bit = row & ~((lx >> level) | (rx >> (N-level)));

    // 최하위 비트부터 없애면서 모든 비트가 없어질때까지 하나씩 재귀
    for(ll a=0; bit!=0; bit ^= a){

        a = bit & (-bit);  // bit의 최하위 비트

        // a자리에 놓았을 경우
        row ^= a;
        lx ^= a << level;
        rx ^= a << (N-level);

        // step을 활용해 구해야할 다음 단계로 바로 접근
        if(backtracking(level + step[level])) {
            ans[level] = a;
            return true;
        }

        // 백트래킹
        row ^= a;
        lx ^= a << level; 
        rx ^= a << (N-level);
    } 
    return false;
}

int main() {
    ios_base::sync_with_stdio(0); cin.tie(0);

    cin >> N;

    row = (1 << N) - 1;
    N--;

    for(int i = 0; i <= N; i++) {
        cin >> Q[i];
    }

    for(int i = 0; i <= N; i++){
        // 이미 놓여진 말 체크해주기
        if(Q[i]){
            // 1ull = 1을 그냥 쓰면 부호있는 32비트 상수이므로 64비트 연산시 이상한 값이 나올 수 있다.
            ans[i] = 1 << (Q[i]-1);
            row ^= 1ull << (Q[i] - 1);  // 놓을 수 있는 곳이 1
            lx |= 1ull << (Q[i] - 1 + i);  // 놓을 수 없는 곳이 1
            rx |= 1ull << (Q[i] - 1 + N - i);  // 놓을 수 없는 곳이 1
        }

        // 0이라면 다음에 구해야 할 곳이 몇 스텝 후인지 미리 계산
        else {
            int s = 1;
            while(i + s <= N && Q[i+s]) ++s;
            step[i] = s;
        }
    }

    // backtracking 시작지점 찾기
    int start = 0;
    while(start <= N && Q[start]) ++start;

    // 해가 없음
    if(!backtracking(start)){
        cout << -1; 
        return 0;
    }

    // 기록된 i번째 비트답을 이용해 답 출력
    for(int i = 0; i <= N; i++){
        int j = 0;
        while((1 << j) < ans[i]) j++;
        cout << j+1 << ' ';
    }
}
```




## 💡 제출 결과 



<img width="979" alt="image" src="https://github.com/hoonably/hoonably.github.io/assets/77783081/62bf4edb-b1b6-4cc4-a4f7-5ad3e5794d49">




## 💡 마무리 



맞은 사람이 10명도 안되는 문제다. (물론 푼 사람이 적어서겠지만...)

비트마스킹을 적용하기도 어렵지만, 최적화 진행을 안하면 시간초과가 발생할 수 있다.

혼자 풀었다가 다른 사람의 코드를 참고하면서 주석을 써보면서 깔끔하게 정리한 코드다.



rust로 236ms 만에 푼 사람이 있는데 rust는 읽을 수가 없어서 현재는 읽기를 포기했다.

