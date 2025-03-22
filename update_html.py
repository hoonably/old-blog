import os
import re
from datetime import datetime

# Notion에서 저장한 이미지 폴더명을 변환해주는 스크립트
# 1. 다운받은 html 파일을 이름변경하지 않고 이 파일과 같은 위치로 옮깁니다.
# 2. 이 스크립트를 실행하여 Notion에서 받은 HTML 파일의 이미지 경로를 Jekyll 형식으로 변환합니다.
# 3. 이미지와 pdf 등이 있는 폴더를 이름변경하고 assets/images/ 폴더로 옮깁니다.
# 4. 기존 html 파일을 삭제합니다.


# 현재 날짜 및 시간 설정
current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S +09:00")

print("\n📂 바꿀 파일명을 입력해주세요. (Python env 181451cf7b7980809440e8edbb098bf2)")
old_name = input()

print("\n📂 새로운 파일명을 입력해주세요. (2025-01-01-제목)")
new_name = input()

print("\n📂 블로그 카테고리를 입력해주세요. \nPaper, Research, Setting, Study, Review, Algorithm, PS, Language, DB, Blog, Talking")
catregory = input()

# 새로운 Jekyll 이미지 폴더 경로
new_image_folder = "/images/" + new_name

# HTML 파일 읽기
with open(old_name+".html", "r", encoding="utf-8") as file:
    html_content = file.read()

# HTML 파일에서 <title>...</title> 찾기
title_match = re.search(r"<title>(.*?)</title>", html_content, re.IGNORECASE)
extracted_title = title_match.group(1) if title_match else "Zsh와 환경변수"

# YAML 프론트 매터 생성
yaml_front_matter = f"""---
layout: blog
title: "{extracted_title}"
subtitle: ""
date: {current_date}
categories: {catregory}
author: "hoonably"
---
"""

# YAML 프론트 매터를 HTML 파일 맨 앞에 추가
html_content = yaml_front_matter + html_content

# 이미지 경로를 Jekyll에 맞게 수정하는 정규식 패턴
updated_html = re.sub(
    rf'src="{old_name}/(.*?)"',
    rf'src="{new_image_folder}/\1"',
    html_content
)

# ✅ `white-space: pre-wrap;`을 제거
updated_html = re.sub(
    r'(white-space:\s*pre-wrap;)',  # 찾을 패턴
    '', # 삭제
    updated_html
)

# ✅ `a,` (콤마 포함) 제거하여
updated_html = re.sub(
    r'a,\s*\n',  # `a,`와 줄바꿈을 포함한 패턴 찾기
    '',  # 삭제
    updated_html
)

# ✅ <header> 태그 삭제
updated_html = re.sub(
    r'<header[\s\S]*?</header>',  # <header>와 </header> 사이의 모든 내용 삭제
    '',
    updated_html
)


# 업데이트된 HTML 저장 (_posts/ 폴더 내에 저장)
jekyll_html_file = f"_posts/{new_name}.html"  # Jekyll에서 사용할 HTML 파일 이름
with open(jekyll_html_file, "w", encoding="utf-8") as file:
    file.write(updated_html)

print(f"✅ 이미지 경로가 Jekyll 형식으로 변환되었고, 필요없는 부분이 수정되었습니다!")
