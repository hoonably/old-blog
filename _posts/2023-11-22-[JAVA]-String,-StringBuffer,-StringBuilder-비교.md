---
title: "[Java] String, StringBuffer, StringBuilder 비교" #대괄호를 쓰려면 ""로 감싸주면 된다.
date: 2023-11-22 13:10:00 +09:00
categories: [코딩언어, Java]
tags: [Java,String]



---

<br/>

https://adjh54.tistory.com/129

## 💡 String 이란? dddd

---

- java.lang에 있다.
- 한번 정해지면 변경불가능한 `불변(immutable) 클래스`다.
- String 객체가 생성되면 그 값은 변경되는게 아니라 새로운 객체로 추가 및 변경이 된다.

<br/>

## 💡 StringBuffer 란?

---

- java.lang에 있다.
- StringBuffer는 변경이 가능한 `가변(mutable) 클래스`다.
- 동기화 과정에서 성능 저하가 발생할 수 있다.

<br/>

## 💡 StringBuilder 란?

---

- java.lang에 있다.
- StringBuilder는 변경이 가능한 `가변(mutable) 클래스`이다.
- 멀티쓰레드 환경에서 불안정적이다.

<br/>



## 💡 문자열 더하기 적용

---

```java
String a = "나는 ";
String b = "말하는 ";
String c = "감자";

// String +
String s = a + b + c;
System.out.println(s); // 출력 : 나는 말하는 감자

// StringBuffer.append()
StringBuffer sb = new StringBuffer("Hello");
sb.append(a).append(b).append(c); // 기존의 StringBuffer 객체에 추가가 된다.
System.out.println(sb); // 출력 : 나는 말하는 감자

// StringBuilder.append()
StringBuilder sb2 = new StringBuilder();
sb2.append(a).append(b).append(c);
System.out.println(sb2); // 출력 : 나는 말하는 감자


//toString을 이용해 String값에 대입
String str = sb2.toString(); 
System.out.println(str);
```



## 💡 반복문 적용

---

반복문을 사용해 많은 데이터를 넣을 때 각 방법에서 큰 차이가 발생한다.







## 💡 특징 비교

---

|      |      |      |      |
| ---- | ---- | ---- | ---- |
|      |      |      |      |
|      |      |      |      |
|      |      |      |      |
|      |      |      |      |





