# Django로 Blog만들기 개인 프로젝트

## 📅 프로젝트 기간
- 2025년 2월 5일 ~ 2월 11일

## 📝 프로젝트 설명
### 제주도 맛집 리뷰 블로그입니다.
- 제주도의 숨은 맛집부터 현지인들이 사랑하는 오래된 식당까지, 발로 뛰며 직접 체험한 진솔한 리뷰를 들려드립니다.
  신선한 제주 식재료로 만든 토속 음식부터 트렌디한 카페까지, 제주의 다채로운 미식 문화를 소개합니다.
  맛있는 음식과 함께 제주의 아름다운 풍경과 이야기를 담아, 여러분의 제주 여행이 더욱 특별해지도록 안내해드리겠습니다.

## 🎯 주요 기능
### 1. 로그인/ 회원가입 기능
   - Django-allauth를 사용하여 Google, Kakao Social 로그인과 User Name, Email로 로그인 할 수 있도록 함

1️⃣ Google 로그인
![login (1)](https://github.com/user-attachments/assets/149c460d-fe01-42dc-8f02-728043811dcd)


2️⃣ Kakao 로그인
![kakao login](https://github.com/user-attachments/assets/13ad8eda-ca13-4a89-b1a5-b84d2302d81a)


### 2. 블로그 관련 기능

#### 1️ 메인화면
<img width="1280" alt="메인 화면" src="https://github.com/user-attachments/assets/7dece6d9-1f0a-4ad8-88a9-a4882703c7d4" />

#### 2️ 포스트 목록 화면
![post_list](https://github.com/user-attachments/assets/a349e8f7-a812-479a-9568-fb61c3492a2a)

#### 3️ 포스트 상세 화면
![post_detail](https://github.com/user-attachments/assets/6b17b4ab-85e4-4d6c-91a4-46e191f1a1ec)

#### 4️ 포스트 생성 화면
![create_post](https://github.com/user-attachments/assets/9186d7f4-f7f6-4abf-a4b7-ec54fe48e6b9)

#### 5️ 포스트 수정 화면
![Update_post](https://github.com/user-attachments/assets/feb790df-63d5-49e4-8e71-38f832c0c5b2)

#### 6️ 포스트 삭제 화면
![delete_post](https://github.com/user-attachments/assets/0d5860e4-0ecb-4806-ad78-136b2832b90c)

#### 7️ 카테고리 조회 화면
![category](https://github.com/user-attachments/assets/b8ee8bd9-9b36-4416-bb43-69ca52a23014)

#### 8️ 포스트 검색 화면
![post_search](https://github.com/user-attachments/assets/3e079dde-88e8-45bf-9aa5-8ea8bb593802)

#### 9️ 댓글 작성 화면
![comment](https://github.com/user-attachments/assets/d1486cd8-4cdb-45e0-8109-fbc73cf94645)

#### 10 댓글 수정 화면
![Update_comment](https://github.com/user-attachments/assets/55396c29-850c-4199-876a-e5db67d03d2f)

#### 11 댓글 삭제 화면
![delete_comment](https://github.com/user-attachments/assets/2743a39b-1db9-4d99-82dd-4bab2b89b958)


#### ➕ 추가 기능
   - 게시글 조회수 확인 가능
   - 카테고리 분류 가능 / 카테고리 설정하지 않았을 시 자동으로 미분류로 설정
   - 포스트 작성자 프로필 구현
   - head image 없을 시 랜덤 이미지 추가
   - 포스트 작성자 프로필 없을 시 랜덤 이미지 추가
   - 페이지네이션

## 🛠️ Stacks

### Environment
![PyCharm](https://img.shields.io/badge/pycharm-000000?style=for-the-badge&logo=pycharm&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white)
![Github](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white)             

### Config
![pip](https://img.shields.io/badge/pip-CB3837?style=for-the-badge&logo=pip&logoColor=white)        

### Development
![HTML](https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Django](https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)

## 📃 API 명세서

### 블로그 관련 API

| 메서드 | URL패턴 | 기능 |
|--------|-----|-------------|
| GET | / | 메인 페이지 |
| GET | /blog/ | 포스트 목록 조회 |
| GET | /blog/<int:pk>/ | 포스트 상세 조회 |
| POST | /blog/create_post/ | 포스트 작성 |
| POST | /blog/update_post/<int:pk>/ | 포스트 수정 |
| POST | /blog/delete_post/<int:pk>/ | 포스트 삭제 |
| GET | /blog/search/<str:q>/ | 포스트 검색 |
| GET | /blog/category/<str:slug>/ | 카테고리 별 포스트 조회 |
| POST | /blog/<int:pk>/new_comment/ | 댓글 작성 |
| POST | /blog/update_commnet/<int:pk>/ | 댓글 수정 |
| POST | /blog/delete_comment/<int:pk>/ | 댓글 삭제 |


### 계정 관련 API
| 메서드 | URL패턴 | 기능 |
|--------|-----|-------------|
| POST | /accounts/signup/ | 회원가입 |
| POST | /accounts/login/ | 로그인 |
| POST | /accounts/google/login/callback/ | 구글 로그인 |
| POST | /accounts/kakao/login/callback/ | 카카오 로그인 |
| POST | /accounts/logout/ | 로그아웃 |

## 📁 프로젝트 파일 구조

## ERD
![ERD](https://github.com/user-attachments/assets/89b08bd4-8fb4-4923-b74c-40054e44fae0)





