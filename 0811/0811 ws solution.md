# 0810_WS_solution

### 1. img tag

```
<img src="c:\Users\Windows 10\Desktop\TIL\ssafy\image\my_photo.png" alt= ssafy>
```

### 2. 파일 경로

* html 경로 aclass\html\h.html

```
(a) 절대 경로
(b) 상대 경로
<img src="..\ssafy\my_photo.png" alt="ssafy">
```

* `.` : 현재 경로를 기준으로 이동
* `..` : 상위 경로 기준으로 이동

### 3. Hyper Link

```
<a href="http://www.ssafy.com">
  <img src="..\ssafy\my_photo.png" alt="ssafy">
</a>
```

### 4. 선택자

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        #ssafy > p:nth-child(2) {
            color: red;
        }
    </style>
</head>
<body>
    <div id="ssafy">
        <h2>어떻게 선택 될까?</h2>
        <p>첫번째 단락</p>
        <p>두번째 단락</p>
        <p>세번째 단락</p>
        <p>네번째 단락</p>
    </div>
</body>
</html>
```

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        #ssafy > p:nth-of-type(2) {
            color: blue;
        }
    </style>
</head>
<body>
    <div id="ssafy">
        <h2>어떻게 선택 될까?</h2>
        <p>첫번째 단락</p>
        <p>두번째 단락</p>
        <p>세번째 단락</p>
        <p>네번째 단락</p>
    </div>
</body>
</html>
```

