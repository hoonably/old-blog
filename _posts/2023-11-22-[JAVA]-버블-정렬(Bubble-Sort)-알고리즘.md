---
title: "[JAVA] 버블 정렬(Bubble Sort) 알고리즘" #대괄호를 쓰려면 ""로 감싸주면 된다.
date: 2023-11-22 00:50:00 +09:00
categories: [알고리즘, 정렬]
tags: [java, algorithm]


---

<br/>

## 버블정렬 함수

<br/>

먼저 알고리즘을 알고있지만 복붙이나 복습을 위해 찾아온 사람들을 위해 코드를 먼저 보여주겠다.

처음 보는거라면 꼭 아래로 내려가 이해해보도록 하자.

<br/>

### 함수 사용 방법

```java
bubblesort(arr);
```

### 함수

```java
public static void bubblesort(int[] arr) {
  int temp = 0;
  for(int i=0;i<arr.length;i++) {
    for(int j=0; j < arr.length - i - 1 ; j++) {
      if(arr[j]>arr[j+1]) { //내림차순일때는 부호 반대로
				temp = arr[j];
				arr[j] = arr[j+1];
				arr[j+1] = temp;
      }
    }
  }
}
```

<br/>

## 알고리즘 이해

가장 큰 수부터 차례대로 맨 뒤로 이동시켜 고정한다고 생각하면 쉽다.

<br/>

### 각 단계에서 일어나는 일

다음 원소와 비교했을때,  지금의 원소가 더 크다면 순서를 바꾼다.

| 현재 원소와 다음 원소 비교 |  3   |  2   |  5   |  4   |  1   |
| :------------------------: | :--: | :--: | :--: | :--: | :--: |
|      arr[j]>arr[j+1]       | `2`  | `3`  |  5   |  4   |  1   |
| arr[j]<=arr[j+1] (변경 X)  |  2   | `3`  | `5`  |  4   |  1   |
|      arr[j]>arr[j+1]       |  2   |  3   | `4`  | `5`  |  1   |
|      arr[j]>arr[j+1]       |  2   |  3   |  4   | `1`  | `5`  |

한 단계마다 가장 큰 수가 제일 뒤로 가게 된다. 

<br/>

### 모든 단계에서 일어나는 일

각 단계에서 정해진 가장 큰 수를 고정하고 그 앞부분에서 단계를 또 시작한다.

| 정렬 전 |  5   |  2   |  3   |  4   |  1   |
| :-----: | :--: | :--: | :--: | :--: | :--: |
|  1단계  |  2   |  3   |  4   |  1   | `5`  |
|  2단계  |  2   |  3   |  1   | `4`  | `5`  |
|  3단계  |  2   |  1   | `3`  | `4`  | `5`  |
|  4단계  |  1   | `2`  | `3`  | `4`  | `5`  |

<br/>

## 코드 이해

먼저, 배열의 두 원소를 바꾸는 함수부터 만들어보자.

다음 함수는 int타입 배열의 i번째 값과 j번째 값을 바꾸는 함수이다.

```java
public static void swap (int[] arr, int i, int j) {
  int temp = arr[i]; // temp에 i번째 값 저장
  arr[i]=arr[j];		 // i번째에 j번째 값 저장
  arr[j]=temp;			 // j번째 값에 저장했던 원래의 i번째 값 넣기
}
```

<br/>

미리 만들었던 swap 함수를 사용하여 bubblesort 함수를 만들어보자.

```java
public static void bubblesort(int[] arr) {
  for(int i=0;i<arr.length;i++) {				// 단계를 i번 반복
    for(int j=0; j < arr.length - i - 1 ; j++) { // 고정된 것을 제외하고 반복
      if(arr[j]>arr[j+1]) { //현재 원소가 다음 원소보다 크면
        swap(arr,j,j+1); //다음 원소와 바꾼다.
      }
    }
  }
}
```

<br/>

하지만 우리는 똑똑하니까 한번에 해보자.

두 함수를 합치면 다음과 같다.

```java
public static void bubblesort(int[] arr) {
  for(int i=0;i<arr.length;i++) { 				
    for(int j=0; j < arr.length - i - 1 ; j++) {	
      if(arr[j]>arr[j+1]) { //오름차순일 경우 부호를 반대로 해주면 된다.
				int temp = arr[j];
				arr[j] = arr[j+1];
				arr[j+1] = temp;
      }
    }
  }
}
```

<br/>

## 코드 테스트 - 백준 2750번: 수 정렬하기

<img width="1231" alt="image" src="https://github.com/hhhoon/hhhoon.github.io/assets/77783081/cdf42206-856a-4da0-af6e-cd916ec7aba2">

```java
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] arr = new int[n];
		for(int i=0;i<n;i++) {
			arr[i] = sc.nextInt();
		}
		sc.close();
		
		bubblesort(arr);
		
		for(int i=0;i<n;i++) {
			System.out.println(arr[i]);
		}
		
	}
	
	public static void bubblesort(int[] arr) {
		  for(int i=0;i<arr.length;i++) {
		    for(int j=0; j < arr.length - i - 1 ; j++) {
		      if(arr[j]>arr[j+1]) {
						int temp = arr[j];
						arr[j] = arr[j+1];
						arr[j+1] = temp;
		      }
		    }
		  }
		}
}
```

#### Output

```java
1
2
3
4
5
```

<br/>

## 시간복잡도

시간 복잡도에 대한 설명은 다음에 포스팅 하도록 하겠다.

<img width="1107" alt="image" src="https://github.com/hhhoon/hhhoon.github.io/assets/77783081/76be57bb-c35a-4225-a1df-58db08724fd1">

이미 정렬이 되어있는지에 상관 없이 무조건 for문을 2번 돌면서 비교를 하기 때문에

버블 정렬의 시간 복잡도는 best, worst, average case 모두 **O(n^2)** 이다.

<br/>

## 정리

### 장점

- 구현이 아주 간단하다.
- 알고리즘을 이해하기 쉽다.

### 단점

- 하나의 원소를 옮기는데 여러번 교환해야 하는 일이 발생한다.
- 이미 옳은 위치에 정렬되어있는 상태의 요소도 교환되는 일이 많다.
- 정렬 알고리즘 중에서 가장 느리고 효율성이 떨어진다.

<br/>

> 버블정렬 알고리즘은 처음 알고리즘을 공부하기엔 좋지만 너무 비효율적이기 때문에 쓸 일이 없다.

