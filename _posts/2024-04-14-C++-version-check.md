---
layout: page
title: "[C++] C++ 버전 체크 방법"
subtitle: "Gold - bitmasking"
date: 2024-04-14 20:50:00 +09:00
categories: Language
author: "hoonably"
# meta: "Springfield"
---

## 💡 버전이 궁금했던 이유



분명히 VSCode에서 C++17로 설정을 바꿔줬는데, 

C++17 부터 가능한 auto tuple, pair unpacking을 하면 오류가 발생해서 뭐지 하면서 확인해봤다.

```c++
auto [x, y] = q.front();
```

알고보니 GCC version이 낮아서 C++17 명령어를 입력해도 17로 실행이 안됐던 것이다.

그래도 이런 것 덕분에 버전체크하는 법도 알아냈다.


## 💡 버전 체크 (C++)



```c++
#include <iostream>
using namespace std;

int main() {
    if (__cplusplus == 201703L)
        cout << "C++17" << endl;
    else if (__cplusplus == 201402L)
        cout << "C++14" << endl;
    else if (__cplusplus == 201103L)
        cout << "C++11" << endl;
    else if (__cplusplus == 199711L)
        cout << "C++98" << endl;
    else
        cout << "pre-standard C++" << endl;
}
```

