

# rest_api


실행할 때 현재 디렉토리와 도커 컨테이너 디럭토리 연결 /home에 현재 폴더 내용을 갖고 있음.

$ docker run -it --rm -p 8888:8888 -v `pwd`:/home jo1013/rest_api:0.05 .
