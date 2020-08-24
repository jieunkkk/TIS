# CSS Layout

### Float

* Float된 이미지 좌, 우측 주변으로 텍스트가 주위를 감싸는 레이아웃을 위해 도입
* none : 기본값  
* left :요소를 왼쪽으로 띄움 `float: left;`
* right : 요소를 오른쪽으로 띄움 `float: right;`
* clear : 선행 floating 요소가 그 아래로 내려가야 하는지를 지정할 때 사용되는 속성
* 과거 열 레이아웃을 만드는 데 사용 -> 텍스트 블록 내에서 float 이미지를 위한 역할로 돌아감

### Flexbox

: 요소 간 공간 배분과 정렬 기능을 제공하기 위한 1차원 레이아웃 모델(단방향 레이아웃)

* 요소
  * Flex Container (부모 요소)
  * Flex Item (자식 요소)
* 축
  * main axis (메인축)
  * cross axis (교차축)

**flexbox의 시작**

=> 부모 요소에 `display: flex;` 혹은 `inline-flex`를 작성

**용어**

* justify : main 축 (default : 좌 -> 우)
* align : cross 축
* content : 여러 줄을 설정
* items : 한 줄을 설정
* self : 개별 요소 설정

**flex에 적용하는 속성**

* 배치 방향 설정
  * flex-direction : 쌓이는 방향을 설정
    * row(기본 값) : 좌 -> 우
    * row-reverse : 우 -> 좌
    * column : 위 -> 아래
    * column-reverse : 아래 -> 위
* 메인축 방향 정렬
  * justify-content : 메인 방향축 요소들을 어떻게 배치할 지 설정
    * flex-start(기본 값) : 좌측 상단 부터 차례로 배치
    * flex-end : 끝나는 점부터 배치 (아이템의 순서는 그대로, 정렬만 우측)
    * center : 메인축 정중앙
    * space-between : 좌우 정렬 (양 끝 아이템은 양 끝에 배치하고 균등하게 아이템을 위치)
    * space-around : 아이템 좌우에 동일한 공간을 부여 ( nㅁ2nㅁ2nㅁn )
    * space-evenly : 균등 정렬
* 교차축 방향 정렬
  * align-items : cross 축 요소를 어떻게 배치할 지 설정
    * 기본값 - strech : 공간을 아이템으로 가득 채움
    * flex-start / flex-end / center
    * baseline : item 내부의 text 밑을 기준선으로 맞춤
  * align-content
    * flex-start / flex-end / center / strech / space-between / space-around
  * align-self : cross 축 각 개별 아이템을 어떻게 배치할 지 설정
    * 설정 값은 위와 동일(기본값 : auto)
* order : 정렬
  * 기본 값 : 0 (모든 아이템)
  * 작은 숫자일 수록 앞에 배치
* 기타
  * flex-grow : 메인 축에서 남는 공간을 각 항목에게 분배하는 방법
    * 각 아이템에 값을 줘서 그 공간 만큼 함
    * 비율을 설정하는 것이 아님
    * 음수는 불가능

----------------------

# Bootstrap

* 오픈 소스 프론트엔드 라이브러리
* 웹 페이지에서 쓰는 많은 요소를 거의 내장
* 디자인 할 시간 줄여주고, 여러 웹 브라우저를 지원하기 위한 크로스 브라우징 고민 필요 없음
* 웹 브라우저 크기에 따라 자동 정렬되는 '그리드 시스템'
* 반응형 웹 디자인 (Responsive Web)

**color**

primary, success, warning, danger...

**spacing**

* 브라우저 html의 루트 글꼴 크기는 16px
* m - margin / p - padding
* t - top / b - bottom / l - left / r - right / x - left, right / y - top, bottom
* 0 - 0rem => 0px / 1 - 0.25rem => 4px / 2 - 0.5rem => 8px / 3 - 1rem => 16px / 4 - 1.5rem => 24px / 5 - 3rem => 48px
  * mt-1 : 0.25rem => 4px

**Responsive Web Design**

- 다양한 화면 크기를 가진 디바이스들이 등장함에 따라 등장

### Bootstrap Grid System

* flexbox를 기반으로 container, row, column으로 컨텐츠를 배치하고 정렬

* 1) **12개의 column** (12가 약수의 개수가 많아서 경우의 수를 많이 고려할 수 있음)

  2) **5개의 grid breakpoints**

* container > row > column
* breakpoints
  * sm(576px) , md(768px), lg(992px), xl(1200px)