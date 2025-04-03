# Notion에서 export한 HTML 파일을 Jekyll 블로그 포스트로 변환하는 스크립트

# 사용법
# 1. 다운받은 html 파일을 이름변경하지 않고 이 파일과 같은 위치로 옮깁니다.
# 2. 이 파일을 실행합니다.
# 3. 카테고리를 입력합니다.
# 4. 변환된 파일은 _posts 폴더에 저장됩니다.

import os
import re
from datetime import datetime
from urllib.parse import unquote  # ✅ 꼭 필요
import shutil
import zipfile

def get_category_from_user():

    # 현재 스크립트 기준 _site 경로
    script_dir = os.path.dirname(os.path.abspath(__file__))
    site_path = os.path.join(os.path.dirname(script_dir), "_site")

    # 제외할 폴더명
    excluded_dirs = {"about", "assets", "blog", "files", "images", "screenshots", "update_html"}

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

def rewrite_image_paths(html_content, title, date_prefix):
    folder_name = f"{date_prefix}-{title.strip()}"

    def replace_src(match):
        original_src = unquote(match.group(1))  # ✅ URL 디코딩
        filename = os.path.basename(original_src)
        return f'src="/images/{folder_name}/{filename}"'

    def replace_href(match):
        original_href = unquote(match.group(1))  # ✅ URL 디코딩
        filename = os.path.basename(original_href)
        return f'href="/images/{folder_name}/{filename}"'

    html_content = re.sub(r'src=["\']([^"\']+)["\']', replace_src, html_content)
    html_content = re.sub(r'href=["\']([^"\']+)["\']', replace_href, html_content)

    return html_content

def copy_images_to_post_folder(html_path, title, date_prefix):
    html_dir = os.path.dirname(html_path)
    html_filename = os.path.splitext(os.path.basename(html_path))[0]
    original_folder = os.path.join(html_dir, html_filename)

    if not os.path.exists(original_folder):
        print(f"⚠️ 이미지 폴더가 존재하지 않음: {original_folder}")
        return

    folder_name = f"{date_prefix}-{title.strip()}"

    script_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(script_dir)
    target_image_dir = os.path.join(root_dir, "images", folder_name)
    os.makedirs(target_image_dir, exist_ok=True)

    for filename in os.listdir(original_folder):
        source_file = os.path.join(original_folder, filename)
        target_file = os.path.join(target_image_dir, filename)
        if os.path.isfile(source_file):
            shutil.copy2(source_file, target_file)

def process_html_file(filepath, current_date):
    # 파일 읽기
    with open(filepath, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # <div class="page-body"> 이전 내용 제거
    marker = '<div class="page-body">'
    marker_index = html_content.find(marker)
    if marker_index != -1:
        html_content = html_content[marker_index:]
    else:
        print(f"❌ {filepath} 에서 <div class=\"page-body\"> 태그를 찾을 수 없습니다. 건너뜁니다.")
        return

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
    print(f"\n\n\n ⭐️⭐️⭐️⭐️⭐️ {title} 작업을 시작합니다.")
    category = get_category_from_user()

    # YAML 프론트 매터 생성
    yaml_front_matter = f"""---
layout: blog
title: "{title}"
subtitle: ""
date: {current_date} +09:00
categories: {category}
author: "hoonably"
---
"""

    # 최종 콘텐츠 생성
    final_content = yaml_front_matter + html_content

    # 저장 경로 설정
    script_dir = os.path.dirname(os.path.abspath(__file__))
    posts_dir = os.path.join(os.path.dirname(script_dir), "_posts")
    os.makedirs(posts_dir, exist_ok=True)

    date_prefix = current_date.split()[0]
    safe_title = title.replace(" ", "-")
    folder_name = f"{date_prefix}-{title}"

    html_content = rewrite_image_paths(html_content, title, date_prefix)
    copy_images_to_post_folder(filepath, title, date_prefix)

    new_filename = f"{folder_name}.md"
    new_filepath = os.path.join(posts_dir, new_filename)

    # Markdown 파일 저장
    with open(new_filepath, 'w', encoding='utf-8') as file:
        file.write(final_content)

    # 원본 HTML도 잘라서 다시 저장
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(html_content)

    # ✅ 변환 완료 메시지
    print(f"✅✅✅✅✅ 변환 완료: {new_filename}")

if __name__ == "__main__":
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
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
                        break

            if html_file:
                process_html_file(html_file, current_date)

            # zip 및 해제된 폴더 삭제
            shutil.rmtree(extract_dir)
            os.remove(zip_path)


