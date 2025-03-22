# REST API Docker 설정 및 사용 가이드

## Docker 실행

Docker 컨테이너를 실행하여 로컬 디렉토리와 컨테이너 내부를 연결합니다.

```bash
# 기본 실행 명령어
docker run -d -it --rm -p 8333:8333 -p 8000:8000 -v ~/workspace:/home --name rest_api -e LC_ALL=C.UTF-8 jo1013/rest_api:0.1

# 일반 형식
docker run -d -it --rm -p [로컬포트]:[컨테이너포트] -v [로컬경로]:[컨테이너경로] --name [컨테이너이름] -e [환경설정] [이미지명]:[태그]
```

> **참고**: 
> - 컨테이너 내 `/home` 디렉토리에 로컬 폴더 내용이 연결됩니다.
> - 다수의 컨테이너를 실행할 경우, 포트 충돌을 피하기 위해 Jupyter Notebook은 8333 포트를 사용합니다.
> - FastAPI는 기본적으로 8000 포트를 사용합니다.

## Docker 컨테이너 접속

```bash
# 컨테이너 접속
docker exec -it rest_api bash

# 일반 형식
docker exec -it [CONTAINER_ID 또는 CONTAINER_NAME] bash
```

## Jupyter Notebook 실행

```bash
# Jupyter Notebook 실행
jupyter notebook --allow-root --ip=0.0.0.0 --port=8333 --no-browser

# 일반 형식
jupyter notebook --allow-root --ip=0.0.0.0 --port=[포트번호] --no-browser
```

## API 서버 실행

### app.py로 서버 실행
```bash
uvicorn app:app --reload --host=0.0.0.0 --port=8000
```

### main.py로 서버 실행
```bash
uvicorn main:app --reload --host=0.0.0.0 --port=8000

# 일반 형식
uvicorn [파일명]:[app변수명] --reload --host=0.0.0.0 --port=[포트번호]
```

## API 사용 안내

### 데이터 출처
데이터 출처: 도로교통공단 TAAS(교통사고분석시스템) - http://taas.koroad.or.kr/api/

### API 엔드포인트 설명

#### 사고 유형
- `child`: 어린이사고
- `bicycle`: 자전거사고
- `dawn`: 야간사고
- `old`: 노인사고
- `pedestrian`: 보행자사고

#### 연도 범위
- 지원 연도: 2012~2019

#### 반환 데이터 필드
- `code`: 법정동코드
- `cases`: 사고건수
- `cases_ratio`: 사고건수 구성비
- `die`: 사망자수
- `dieratio`: 사망자수 구성비
- `fatality`: 치사율
- `lnjured`: 부상자수
- `lnjuredratio`: 부상자수 구성비

### API 문서 및 사용 예시

API 문서는 브라우저에서 `http://localhost:8000/docs`로 접속하여 확인할 수 있습니다.

#### 사용 예시
- `localhost:8000/child`: 모든 연도의 어린이사고 데이터 (딕셔너리 형태)
- `localhost:8000/child/2013`: 2013년 어린이사고 데이터 (딕셔너리 형태)
- `localhost:8000/child/2013/code`: 2013년 어린이사고 법정동코드 목록 (리스트 형태)
