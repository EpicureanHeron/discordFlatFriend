FROM python:3.9

RUN apt-get update
ADD . .
RUN pip install -r requirements.txt
#COPY requirements.txt requirements.txt
#RUN pip3 install -r requirements.txt

ENTRYPOINT ["python", "flatfriendboy.py"]

