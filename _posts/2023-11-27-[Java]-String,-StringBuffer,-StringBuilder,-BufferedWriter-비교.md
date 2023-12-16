---
title: "[Java] String, StringBuffer, StringBuilder, BufferedWriter 비교" #대괄호를 쓰려면 ""로 감싸주면 된다.
date: 2023-11-27 23:00:00 +09:00

categories: [Language, Java]

# Algorithm : 시간복잡도, 자료구조, 정렬, 탐색, 탐욕알고리즘, 정수론, 그래프, 트리, 조합, 다이나믹프로그래밍
# Language : Java, Python, C++
# Blog : Markdown, Just_blog
# Baekjoon : Bronze, Silver, Gold, Platinum, Diamond, Ruby

tags: [Java, Baekjoon]

# Algorithm, Baekjoon, Python, Java, DB, Blog

---

<br/>

## 💡 String 이란?

---

- java.lang에 있다.
- 한번 정해지면 변경불가능한 `불변(immutable) 클래스`다.
- String 객체가 생성되면 그 값은 변경되는게 아니라 새로운 객체로 추가 및 변경이 된다.

<br/>

## 💡 StringBuffer 란?

---

- java.lang에 있다.
- StringBuffer는 변경이 가능한 `가변(mutable) 클래스`다.
- 멀티 쓰레드 환경에서 동시에 같은 문자열 인스턴스에 접근할 때 **중복 점유를 막을 수 있는 장치**가 되어 있다.
- 위의 장치 때문에 **동기화 과정에서 성능 저하**가 발생할 수 있다.

<br/>

## 💡 StringBuilder 란?

---

- java.lang에 있다.
- StringBuilder는 변경이 가능한 `가변(mutable) 클래스`이다.
- 멀티쓰레드 환경에서 불안정적이지만 일반적 환경에서는 StringBuffer처럼 동기화로 인한 성능저하가 일어나지 않기 때문에 `가장 빠르다.`

<br/>

## 💡 BufferedWriter 란?

---

- java.io에 있다.
- 선언이 필요하다.
- throws Exception 예외처리가 필요하다.
- 버퍼를 잡아 놓았기 때문에 반드시 사용한 후에, flush()/ close()를 해주어야 한다. 

<br/>



## 💡 문자열 더하기

---

```java
String a = "나는 ";
String b = "말하는 ";
String c = "감자";

// String +
String str = a + b + c;
System.out.println(str);	 // 출력 : 나는 말하는 감자

// StringBuffer.append()
StringBuffer sb = new StringBuffer();
sb.append(a).append(b).append(c);
System.out.println(sb); 	// 출력 : 나는 말하는 감자

// StringBuilder.append()
StringBuilder sb2 = new StringBuilder();
sb2.append(a).append(b).append(c);
System.out.println(sb2); 	// 출력 : 나는 말하는 감자

//BufferedWriter
BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
bw.write(a);
bw.write(b);
bw.write(c);
bw.flush();   // 출력 : 나는 말하는 감자
bw.close();
```

```java
//toString()이나 valueOf()을 이용해 둘 다 String값에 대입이 가능하다.
String str1 = sb1.toString();
String str2 = sb2.toString();
```

<br/>

## 💡 반복문 적용

---

[백준 2751번 수 정렬하기 2](https://www.acmicpc.net/problem/2751){:target="_blank"}

<img width="1065" alt="image" src="https://github.com/hhhoon/hhhoon.github.io/assets/77783081/12ad07e6-4b44-4b0b-b287-b6e19a8521a0">

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		ArrayList<Integer> list = new ArrayList<Integer>();
		
		int N =	Integer.parseInt(br.readLine());
		for(int i=0; i<N; i++) {
			list.add(Integer.parseInt(br.readLine()));
		}
		
		//오름차순 정렬
		Collections.sort(list);
		
		//StringBuilder 사용
		StringBuilder sb = new StringBuilder();
		
		//향상된 for문 사용 (list)
		for(int value : list) {
			sb.append(value).append('\n');
		}
		
		//StringBuilder 출력
		System.out.println(sb);	
		
	}

}
```

<img width="1041" alt="image" src="https://github.com/hhhoon/hhhoon.github.io/assets/77783081/e8275870-0fc1-42ed-901b-bc6873ac72d8">

- 아래 3개의 시간초과 모두  StringBuilder를 사용하지 않고 String을 사용해 더해서 생긴 결과다. 
- 위에서 두번째 결과는 위 코드에서 BufferedReader를 쓰지 않고 Scanner을 썼던 결과다.
- 맨 위의 결과가 위의 코드의 결과이다. BufferedReader + StringBuilder을 사용해 빠른 결과를 도출했다.
- Scanner와 BufferedReader 의 비교는 추후에 글로 작성할 예정이다.

<br/>

## 💡 특징 비교

---

|                |              String               |    StringBuffer    |   StringBuilder    |   BuffereWriter   |
| :------------: | :-------------------------------: | :----------------: | :----------------: | :---------------: |
|     클래스     |               불변                |        가변        |        가변        |       가변        |
|  문자열 변경   |           str += "추가"           | sb.append("추가"); | sb.append("추가"); | bw.write("추가"); |
|      속도      |       `매우 매우 매우 느림`       |        빠름        |    `가장 빠름`     |       보통        |
| 추천 사용 방법 | 문자열의 변경이나 추가가 없는경우 |  멀티쓰레드 환경   |  단일쓰레드 환경   |                   |

<br/>

## 💡 상세 속도 비교

---

![image](https://github.com/hhhoon/hhhoon.github.io/assets/77783081/be1b9069-c651-4654-8c29-fd726b112ff5)

출처 : javapapers.com

- y축은 걸리는 시간으로 기울기가 가장 낮은 StringBuilder가 가장 빠르다.
- 다음은 0을 반복적으로 더해서 직접 걸리는 시간을 구해보는 코드다.

```java
package Test;

import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;

public class Time {

	public static void main(String[] args) throws IOException {

		long now;
		
		// String 
		now = System.currentTimeMillis();
		String test = "";
		for (int i = 0; i < 300000; i++) {
			test += "0";
		}
		System.out.println(test);
		System.out.println("String 연산시간 : " + (System.currentTimeMillis()-now));
		
		// StringBuffer
		now = System.currentTimeMillis();
		StringBuffer buffer = new StringBuffer();
		for (int i = 0; i < 300000; i++) {
			buffer.append("0");
		}
		System.out.println(buffer);
		System.out.println("StringBuilder 연산시간 : " + (System.currentTimeMillis()-now));
		
		// StringBuilder
		now = System.currentTimeMillis();
		StringBuilder builder = new StringBuilder();
		for (int i = 0; i < 300000; i++) {
			builder.append("0");
		}
		System.out.println(builder);
		System.out.println("StringBuffer 연산시간 : " + (System.currentTimeMillis()-now)); 
		
		// BufferedWriter
		now = System.currentTimeMillis();
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		for (int i = 0; i < 300000; i++) {
			bw.write("0");
		}
		bw.newLine();
		bw.flush();
		System.out.println("BufferedWriter 연산시간 : " + (System.currentTimeMillis()-now));
		
	}

}
```

```
//출력 결과
000000000...(300000개)
String 연산시간 : 6267~6500 (너무 느려서 3번만 돌려봄)

000000000...(300000개)
StringBuilder 연산시간 : 25~49 (10회 돌려본 결과)

000000000...(300000개)
StringBuilder 연산시간 : 16~28 (10회 돌려본 결과)

000000000...(300000개)
BufferedWriter 연산시간 : 24~38 (10회 돌려본 결과)
```

<br/>

## 💡 결론

---

- String은 문자열을 변경하거나 추가할 때 사용하면 반복이 많아지고 데이터가 커질수록 속도 차이가 많이 나서 쓰지 않는게 좋다.
- 귀찮더라도 문자열을 더하는 경우가 많으면 `StringBuilder`을 사용하는 습관을 들이자.
- 백준에서 문제를 풀었는데 시간초과가 발생한다면 String을 사용했는지부터 보고 고치자.