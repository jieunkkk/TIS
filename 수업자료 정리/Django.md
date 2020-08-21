# Django

### Project 생성

```
# django 설치
pip install django

# 프로젝트 생성
django-admin startproject <App_Name>
```

* 앱이름 설정 시 hyphen (-) 포함 불가

### App 생성

```
cd django_prac  # 안 쪽 파일로 들어가줘야됨

django-admin startapp home # home app 생성

python manage.py runserver  # app 실행
```

### App 등록

**django_prac/setting.py** (프로젝트명 -> django_prac)

```python
INSTALLED_APPS = [
    'home',  <- 앱 등록
    'django.contrib.admin',
    ...
]

...

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'  -> 언어랑 시간 설정
```

