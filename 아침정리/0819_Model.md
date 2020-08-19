# Model

* DB에 데이터를 저장하고 가져오는 것
* SQL
* ORM (쉽게 말해 통역기)
  * 쿼리를 python에서 object로 사용할 수 있게 해줌

### 모델 정의

* `models.py` 에 모델 클래스를 정의를 해서 사용할 수 있음

  * **class 테이블명(models.Model):**

    ​	title = model.CharField(max_length=100):

    * 자주 사용하는 필드명
    * CharField / DataTimeField / TextField / IntegerField / BooleanField / ...
    * Django 공식 문서 Model field 라고 구글링하면 찾을 수 있음

### DB 생성

* 클래스를 다 정의를 하면 **반드시 해야만 하는 일!!**
  * makemigrations
    * python manage.py makemigrations [app 이름]
    * DB에 적용하기 위한 설계도 제작
    * app 이름을 뒤에 적으면 해당 app에 있는 models.py의 내용만 설계도를 만듦(생략가능)
  * migrate
    * python manage.py migrate [app 이름]
    * 만들어진 설계도를 가지고 DB에 테이블을 생성.
    * app 이름을 적으면 해당 app에 있는 migration 파일을 DB에 적용 시킴
  * showmigrations
  * sqlmigrate

### DB 사용

* DB api

  ```
  모델클래스이름.objects.QuerySetAPI
  
  Article.objects.all()
  * objects : s를 내비두고 놀지 말자. 항상 같이 델꼬 다니자!
  ```

* 자세한 사용 방법은 model crud 참고