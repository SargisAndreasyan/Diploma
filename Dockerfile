FROM python:3.8.12-slim
WORKDIR /app
COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install python-xlib

COPY . .
COPY classes .
CMD [ "python3",  "./main.py"]