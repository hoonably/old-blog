---
layout: blog
title: "Ablation Study 란?"
subtitle: ""
date: 2025-03-05 17:20:00 +09:00
categories: Research
author: "hoonably"
# meta: "Springfield"
---


[SVDQuant Project](https://hanlab.mit.edu/projects/svdquant)

논문을 읽다가 도대체 Ablation Study가 뭐지? 했다.

한국어로 직역하면 절제 연구인데 해석해도 이게 뭔지 싶어서 궁금해서 찾아봤다.



> 모델에서 특정 요소를 제거하거나 변경하면서 해당 요소가 성능에 미치는 영향을 분석하는 실험



##  💡 Ablation Study의 목적

1. 각 구성 요소의 중요도 평가
   - 모델에서 특정 요소(예: 특정 레이어, 손실 함수, 데이터 처리 기법 등)를 제거하거나 수정했을 때 성능이 얼마나 떨어지는지 본다.
   - 예를 들어 "SVDQuant에서 SVD를 안 쓰면 성능이 어떻게 되지?" 같은 실험.
2. 최적의 모델 구성 찾기
   - 여러 요소를 실험적으로 비교하면서 불필요한 부분을 제거해 **더 가볍고 빠른 모델**을 만들 수도 있음.
3. 이론적 정당성 검증
   - "우리가 제안한 방법이 정말 효과가 있는지?"를 증명하는 과정.





## 💡 예제: SVDQuant 논문에서 Ablation Study

<img width="936" alt="Image" src="https://github.com/user-attachments/assets/f36e5dd1-951f-44e7-a2a0-37ab7ec0aa11" />



SVDQuant 논문에서는 **Figure 10**에서 다양한 실험을 함:

- **SVD만 적용** → 성능이 낮아짐 ❌
- **기본적인 4-bit 양자화** → 품질이 많이 떨어짐 ❌
- **Smoothed Quantization 추가** → 조금 나아지지만 여전히 부족함 ❌
- **LoRC 방식 적용** → 효과가 적음 ❌
- **SVDQuant 방식 적용** → 가장 좋은 결과 ✅

즉, **각 요소를 하나씩 제거하면서 실험**을 진행해서 "SVDQuant가 왜 효과적인가?"를 증명함.





## 💡 쉽게 비유하면?

Ablation Study는 마치 **요리에서 특정 재료를 빼보면서 맛이 어떻게 변하는지 실험하는 과정**과 비슷함

- 카레를 만들면서 **"양파를 빼면?"**, **"후추를 빼면?"**, **"소금을 줄이면?"** 하는 식으로 실험
- 최종적으로 "이 재료가 핵심이구나!"를 찾아내는 과정

그래서 논문에서 **Ablation Study**라고 하면 "**이 기능이 없었으면 어땠을까?**"를 실험한 부분이라고 생각하면 됨.