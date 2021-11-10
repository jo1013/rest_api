

# REST_API


## 실행할 때 현재 디렉토리와 도커 컨테이너 디럭토리 연결 
## /home에 현재 폴더 내용을 갖고 있음.



## 개인마다 다르게 설정 할 수 있다. 컨테이너를 여러개 돌리는 경우가 있어 8333으로 설정했다. 
### fast_api는 8000으로 설정
```
$ docker run -d -it --rm -p 8333:8333 -p 8000:8000 -v ~/workspace:/home --name rest_api -e LC_ALL=C.UTF-8 jo1013/rest_api:0.1
$ docker run -it --rm -p [로컬포트]:[컨테이너포트] -v [local 경로]:[컨테이너경로] [image]:[tag]
```

### docker 터미널 실행

```
$ docker exec -it rest_api bash
$ docker exec -it [CONTAINER ID or CONTAINER NAME] bash
```




### 쥬피터 실행
```

$ jupyter notebook --allow-root --ip=0.0.0.0 --port=8333 --no-browser

```


```
$ uvicorn app:app --reload --host=0.0.0.0 --port=8000

```



```
$ uvicorn main:app --reload --host=0.0.0.0 --port=8000
$ uvicorn [py파일]]:[api_name] --reload --host=0.0.0.0 --port=8000
```