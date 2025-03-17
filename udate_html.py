import os
import re

# Notion에서 저장한 이미지 폴더명을 변환해주는 스크립트
# 0. html 파일과 이미지 폴더명을 "2025-03-17-제목" 형식으로 변경합니다.
# 1. 다운받은 html 파일을 _posts/ 폴더로 옮깁니다.
# 2. 이미지와 pdf 등이 있는 폴더를 assets/images/ 폴더로 옮깁니다.
# 3. 이 스크립트를 실행하여 Notion에서 받은 HTML 파일의 이미지 경로를 Jekyll 형식으로 변환합니다.

# Notion HTML 파일 위치
print("\n📂 Notion에서 받은 HTML 파일을 _posts에 넣었다면 파일 이름을 입력해주세요. (.html 제외)")
file_name = input()
notion_html_file = "_posts/" + file_name + ".html"  # Notion에서 받은 HTML 파일 이름

# 기존 Notion 이미지 폴더명 (다운로드한 폴더명)
print("\n📂 Notion에서 받은 이미지 폴더명을 입력해주세요.")
old_image_folder = input()

# 새로운 Jekyll 이미지 폴더 경로
new_image_folder = "/assets/img/" + file_name

# HTML 파일 읽기
with open(notion_html_file, "r", encoding="utf-8") as file:
    html_content = file.read()

# 이미지 경로를 Jekyll에 맞게 수정하는 정규식 패턴
updated_html = re.sub(
    rf'src="{old_image_folder}/(.*?)"',
    rf'src="{new_image_folder}/\1"',
    html_content
)

# ✅ `white-space: pre-wrap;`을 주석 처리
updated_html = re.sub(
    r'(white-space:\s*pre-wrap;)',  # 찾을 패턴
    '', # 삭제
    updated_html
)

# ✅ `a,` (콤마 포함) 제거하여 `a.visited`만 남기기
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


# 업데이트된 HTML 저장
jekyll_html_file = file_name + ".html"  # Jekyll에서 사용할 HTML 파일 이름
with open(jekyll_html_file, "w", encoding="utf-8") as file:
    file.write(updated_html)

print(f"✅ 이미지 경로가 Jekyll 형식으로 변환되었고, 필요없는 부분이 수정되었습니다! ➝ {jekyll_html_file} 파일을 끌어서 _posts/에 넣어주세요.")
