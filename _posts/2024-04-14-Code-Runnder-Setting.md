---
layout: page
title: "[VSCode] Code Runner을 위한 setting.json 설정"
subtitle: ""
date: 2024-04-14 21:30:00 +09:00
categories: Setting
author: "hoonably"
# meta: "Springfield"
---


## 💡 setting.json ?



vscode에서 setting.json 이란 파일이 있다.

검색창에 >setting을 치면, 작업 영역 설정 열기를 하면 열 수 있다.

이 작업 영역에서 setting을 어떻게 할 지에 대해서 설정한다.

<img width="965" alt="image" src="https://github.com/hoonably/hoonably.github.io/assets/77783081/f9833bf8-5397-45b9-b5fc-c57d021a61a4">


## 💡 Code Runner 띄어쓰기



기본적으로 Code Runner에서, 파일명에 띄어쓰기 등과 같은 것이 있으면 

터미널로 옮겨적을때 띄어쓰기로 인식해서 정상적으로 컴파일되지 않는다. 

그래서 파일명을 항상 _ 와 같은 것을 사용했는데, 불편함이 있었다.

이는 " " 를 사용하여 파일명을 감싸주면, 파일에 띄어쓰기나 .이 있어도 정상적으로 컴파일된다.

```json
// 파일명 띄어쓰기 안됨
"cpp": "cd $dir && g++ -std=c++17 $fileName -o $fileNameWithoutExt && ./$fileNameWithoutExt"

// 파일명 띄어쓰기 가능
"cpp": "cd $dir && g++ -std=c++17 \"$fileName\" -o \"$fileNameWithoutExt\" && ./\"$fileNameWithoutExt\""
```


## 💡 setting.json



```json
{
    "code-runner.executorMap": {
        "javascript": "node",
        "java": "cd $dir && javac \"$fileName\" && java \"./tempCodeRunnerFile\"",
        "c": "cd $dir && gcc \"$fileName\" -o \"tempCodeRunnerFile\" && ./\"tempCodeRunnerFile\"",
        "cpp": "cd $dir && clang++ -std=c++17 \"$fileName\" -o \"tempCodeRunnerFile\" && ./\"tempCodeRunnerFile\"",
            // 경로에 들어가고,  g++로 c++17버전으로 컴파일해 실행 파일 생성,     열기

        // "python3" 명령어를 "python"으로 바꿔준 경우 사용 가능 (원래는 python3)
        // 터미널에서 vi ~/.zshrc 로 들어간 후
        // alias python="python3"
        // 라는 한 줄을 추가하면 앞으로 python을 입력하면 python3 효과가 나온다.
        "python": "python",
        "ruby": "ruby",
        "spim": "spim -file \"$fileName\""
    },

    "code-runner.preserveFocus": false,  // 파일 실행해도 실행 텍스트 포커스 유지하는 옵션
    "code-runner.saveFileBeforeRun": true,  // 실행버튼 누르면 자동으로 저장하고 실행하는 옵션
    "code-runner.runInTerminal": true,  // 터미널에서 실행하는 옵션 (이걸 켜야 입력 가능)

    "cmake.configureOnOpen": true,
    "code-runner.ignoreSelection": true,
    "files.associations": {
        "*.scm": "racket",
    },

    
    // 윈도우용 (윈도우에서도 같은 폴더를 USB나 Cloud로 공유해서 쓴다면 해놓자.)
    // "C_Cpp.default.compilerPath": "C:\\MinGW\\bin\\g++.exe",
}
```

