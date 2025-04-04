# Notion에서 export한 HTML 파일을 Jekyll 블로그 포스트로 변환하는 스크립트

# 사용법
# 1. Notion에서 export한 HTML 파일과 이미지 폴더가 들어있는 zip 파일을 이 스크립트와 같은 폴더에 넣습니다.
# 2. 스크립트를 실행합니다.
# 3. 카테고리를 선택합니다.
# 4. 변환된 Markdown 파일이 _posts 폴더에 생성됩니다.
# 5. 해제됐던 폴더는 사라지고, zip 파일은 남아있습니다.
# 6. 확인 후 zip 파일을 직접 삭제합니다.

import os
import re
from datetime import datetime
from urllib.parse import unquote  # ✅ 꼭 필요
import shutil
import zipfile

current_time = ""  # 현재 시간 (YYYY-MM-DD HH:MM:SS)
current_date = ""  # 날짜 (YYYY-MM-DD)
old_filename = ""  # 기존 HTML 파일명 ()
new_filename = ""  # 마크다운 파일명과 폴더명 (YYYY-MM-DD-Data-Structure)

# 카테고리를 입력받는 함수
def get_category_from_user():

    # 현재 스크립트 기준 _site 경로
    script_dir = os.path.dirname(os.path.abspath(__file__))
    site_path = os.path.join(os.path.dirname(script_dir), "_site")

    # 제외할 폴더명
    excluded_dirs = {"about", "assets", "blog", "files", "images", "screenshots", "update_notion_script"}

    if not os.path.exists(site_path):
        print(f"⚠️  _site 경로가 존재하지 않음: {site_path}")
        return "uncategorized"

    # 카테고리 후보 필터링
    possible_categories = [
        d for d in os.listdir(site_path)
        if os.path.isdir(os.path.join(site_path, d)) and d.strip() != "" and d not in excluded_dirs
    ]

    possible_categories.sort()

    # 목록 출력
    print("사용 가능한 카테고리:")
    for idx, cat in enumerate(possible_categories, 1):
        print(f"{idx}. {cat}")
    print(f"{len(possible_categories) + 1}. 새 카테고리 입력")

    # 사용자 숫자 입력 받기
    selected = input("사용하실 카테고리 번호를 입력해주세요: ").strip()
    while not selected.isdigit() or not (1 <= int(selected) <= len(possible_categories) + 1):
        selected = input("잘못된 입력입니다. 다시 입력해주세요: ").strip()

    selected_num = int(selected)

    # 새 카테고리 입력 시
    if selected_num == len(possible_categories) + 1:
        while True:
            new_cat = input("새로운 카테고리 이름을 입력해주세요: ").strip()
            if new_cat in excluded_dirs:
                print("❌ 사용할 수 없는 카테고리명입니다. 다시 입력해주세요.")
            elif new_cat == "":
                print("❌ 빈 이름은 사용할 수 없습니다. 다시 입력해주세요.")
            else:
                return new_cat
    else:
        return possible_categories[selected_num - 1]

# html 파일 내에 있는 src, href 속성의 경로를 변경하는 함수
def rewrite_image_paths(html_content):

    old_encoded = old_filename.replace(" ", "%20")
    html_content = html_content.replace(
        f'src="{old_encoded}',
        f'src="/images/{new_filename}'
    )
    html_content = html_content.replace(
        f'href="{old_encoded}',
        f'href="/images/{new_filename}'
    )
    print(f"1️⃣ 이미지 경로 수정 완료: {old_encoded} → /images/{new_filename}")
    return html_content

# 마크다운 파일 수정 및 생성하는 함수
def write_markdown_file(filepath, html_content):
    global new_filename  # 전역변수 변경해야하므로

    # <div class="page-body"> 이전 내용 제거
    marker = '<div class="page-body">'
    marker_index = html_content.find(marker)
    if marker_index != -1:
        html_content = html_content[marker_index:]

    # 마지막 줄 </article> 이후 제거
    end_marker = '</article>'
    end_index = html_content.find(end_marker)
    if end_index != -1:
        html_content = html_content[:end_index]
    
    # 파일명에서 title 추출
    base_name = os.path.basename(filepath)
    filename_no_ext = os.path.splitext(base_name)[0]
    split_parts = filename_no_ext.strip().split()
    title = ' '.join(split_parts[:-1]) if len(split_parts) > 1 else filename_no_ext
    print(f"⭐️⭐️⭐️⭐️⭐️ {title}.html 변환작업을 시작합니다.")

    # .md 파일명과 이미지 등이 들어있는 폴더명 사용자가 지정
    new_filename = input("파일명을 영어로 입력해주세요 (공백은 '-'으로 자동 변경됩니다): ").strip()
    while not new_filename:
        new_filename = input("❌ 비워둘 수 없습니다. 다시 입력해주세요: ").strip()
    new_filename = new_filename.replace(" ", "-")
    new_filename = current_date + "-" + new_filename

    # category 선택
    category = get_category_from_user()

    # YAML 프론트 매터 생성
    yaml_front_matter = f"""---
layout: blog
title: "{title}"
subtitle: ""
date: {current_time} +09:00
categories: {category}
author: "hoonably"
---
"""
    
    # 이미지 경로 수정
    html_content = rewrite_image_paths(html_content)

    # ✅ .md 수정본 생성 후 저장
    final_content = yaml_front_matter + html_content
    script_dir = os.path.dirname(os.path.abspath(__file__))
    posts_dir = os.path.join(os.path.dirname(script_dir), "_posts")
    os.makedirs(posts_dir, exist_ok=True)
    new_filepath = os.path.join(posts_dir, f"{new_filename}.md")
    with open(new_filepath, 'w', encoding='utf-8') as file:
        file.write(final_content)
    print(f"2️⃣ 마크다운 파일 생성 완료: {new_filepath}")

# 이미지가 들어있는 폴더를 "images/" 안으로 복사하는 함수
def copy_folder(html_path):
    """
    html_path: 원본 HTML 경로
    new_filename: 예시 - '2025-04-04-MLOps.md'
    """

    # 원본 이미지 폴더: html 파일 옆에 있는 동일 이름 폴더
    html_dir = os.path.dirname(html_path)
    html_filename = os.path.splitext(os.path.basename(html_path))[0]
    original_image_folder = os.path.join(html_dir, html_filename)

    if not os.path.exists(original_image_folder):
        print(f"❌ 이미지 폴더가 존재하지 않습니다.: {original_image_folder}")
        return

    # 타겟 경로: images/{new_filename_without_ext}/
    script_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(script_dir)
    folder_name = os.path.splitext(new_filename)[0]  # .md 제거
    target_folder = os.path.join(root_dir, "images", folder_name)
    os.makedirs(target_folder, exist_ok=True)

    # 이미지 복사
    for item in os.listdir(original_image_folder):
        src_path = os.path.join(original_image_folder, item)
        dst_path = os.path.join(target_folder, item)
        if os.path.isfile(src_path):
            shutil.copy2(src_path, dst_path)

    print(f"3️⃣ 이미지 복사 완료 → {target_folder}")

def process_html_file(filepath):
    # 파일 읽기
    with open(filepath, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # 마크다운 파일 생성
    write_markdown_file(filepath, html_content)

    # 이미지 들어있는 폴더 옮기기
    copy_folder(html_file)

    # ✅ 변환 완료 메시지
    print(f"✅ 모든 작업 완료 → {new_filename}")

if __name__ == "__main__":
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    current_date = current_time.split()[0]

    script_dir = os.path.dirname(os.path.abspath(__file__))

    for filename in os.listdir(script_dir):
        if filename.endswith(".zip"):
            zip_path = os.path.join(script_dir, filename)
            extract_dir = os.path.join(script_dir, os.path.splitext(filename)[0])

            # 압축 해제
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(extract_dir)

            # .html 파일 찾기
            html_file = None
            for root, _, files in os.walk(extract_dir):
                for f in files:
                    if f.endswith(".html"):
                        html_file = os.path.join(root, f)
                        old_filename = os.path.splitext(f)[0]
                        break

            if html_file:
                process_html_file(html_file)

            # 해제된 폴더 삭제
            shutil.rmtree(extract_dir)

            # zip 파일 삭제
            os.remove(zip_path)

