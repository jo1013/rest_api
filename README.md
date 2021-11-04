

# rest_api


실행할 때 현재 디렉토리와 도커 컨테이너 디럭토리 연결 /home에 현재 폴더 내용을 갖고 있음.

$ docker run -d -it --rm -p 8333:8333 -v ~/workspace:/home --name rest_api jo1013/rest_api:0.09 .


$ jupyter notebook --allow-root --ip=0.0.0.0 --port=8333 --no-browser