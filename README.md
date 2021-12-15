

# REST_API


* ### 실행할 때 현재 디렉터리와 도커 컨테이너 디렉터리 연결 
* ### 컨테이너 내 /home에 현재 폴더 내용을 갖고 있음.


----
----


* ### 다르게 설정 할 수 있다. 컨테이너를 여러개 돌리는 경우가 있어 8333으로 설정했다. 
### fast_api는 8000으로 설정
```
$ docker run -d -it --rm -p 8333:8333 -p 8000:8000 -v ~/workspace:/home --name rest_api -e LC_ALL=C.UTF-8 jo1013/rest_api:0.1
$ docker run -d -it --rm -p [로컬포트]:[컨테이너포트] -v [local 경로]:[컨테이너경로] -e [환경설정] [image]:[tag]
```

### docker 터미널 실행

```
$ docker exec -it rest_api bash
$ docker exec -it [CONTAINER ID or CONTAINER NAME] bash
```




### 쥬피터 실행
```

$ jupyter notebook --allow-root --ip=0.0.0.0 --port=8333 --no-browser
$ jupyter notebook --allow-root --ip=0.0.0.0 --port=[포트] --no-browser

```


### app있는 폴더에서 서버 실행
```

~~ $ uvicorn app:app --reload --host=0.0.0.0 --port=8000 ~~
~~ $ uvicorn app:app --reload --host=0.0.0.0 --port=[포트] ~~

```


### main있는 폴더에서 서버 실행
```
$ uvicorn main:app --reload --host=0.0.0.0 --port=8000
$ uvicorn [py파일]]:[api_name] --reload --host=0.0.0.0 --port=8000
```

CSV 자료 :
http://taas.koroad.or.kr/api/

```


API 명세 

child = '어린이사고'                              
    bicycle = '자전거사고'
    dawn = '야간사고'
    old = '노인사고'
    pedestrian = '보행자사고'                                            
 
 
year  2012~2019


   code = '법정동코드'
    cases = '사고건수'
    cases_ratio = '사고건수 구성비'
    die = '사망자수'
    dieratio = '사망자수 구성비'
    fatality = '치사율'
    lnjured = '부상자수'
    lnjuredratio = '부상자수 구성비'

```
# http://localhost:8000/docs    으로 문서로 확인할 수있음.

* #### ex url  :   localhost:8000/child              =>  딕셔너리 형태
* #### ex url  :   localhost:8000/child/2013   =>  딕셔너리 형태
* #### ex url  :   localhost:8000/child/2013/code   =>  리스트 형태
* 

