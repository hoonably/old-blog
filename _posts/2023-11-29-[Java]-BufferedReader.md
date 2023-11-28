---
title: "[Java] BufferedReader" #대괄호를 쓰려면 ""로 감싸주면 된다.
date: 2023-11-29 23:00:00 +09:00
categories: [코딩언어, Java]
tags: [Java, Baekjoon]



---

<br/>

https://dev-myblog.tistory.com/entry/JAVA-String-StringBuilder-StringBuffer-BufferedWriter-%EC%B0%A8%EC%9D%B4

## 💡 BufferedReader란?

---





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

//toString()이나 valueOf()을 이용해 둘 다 String값에 대입이 가능하다.
String str1 = sb1.toString();
String str2 = sb2.toString();
```



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



## 💡 특징 비교

---





## 💡 결론

---

- String은 문자열을 변경하거나 추가할 때 사용하면 반복이 많아지고 데이터가 커질수록 속도 차이가 많이 나서 쓰지 않는게 좋다.
- 귀찮더라도 문자열을 더하는 경우가 많으면 `StringBuilder`을 사용하는 습관을 들이자.
- 백준에서 문제를 풀었는데 시간초과가 발생한다면 String을 사용했는지부터 보고 고치자.