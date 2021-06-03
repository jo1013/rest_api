FROM ubuntu:18.04

MAINTAINER Sawyer "tkdah0@gmail.com"


ARG DEBIAN_FRONTEND=noninteractiv


RUN apt update


RUN apt install software-properties-common -y
RUN add-apt-repository ppa:deadsnakes/ppa


RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get dist-upgrade -y
RUN apt-get install python3-pip -y



RUN apt install python 3.7 -y

RUN pip3 install pillow
RUN pip3 install requests
RUN pip3 install pandas

RUN pip3 install --upgrade pip
RUN pip3 install notebook
RUN pip3 install --ignore-installed jupyter
RUN pip3 install scikit-learn
RUN pip3 install matplotlib
RUN jupyter notebook --generate-config --allow-root
RUN echo "c.NotebookApp.password = u'sha1:6a3f528eec40:6e896b6e4828f525a6e20e5411cd1c8075d68619'" >> /root/.jupyter/jupyter_notebook_config.py

EXPOSE 8888

ENTRYPOINT jupyter notebook --allow-root --ip=0.0.0.0 --port=8888 --no-browser


