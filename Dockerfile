FROM python:2.7

ENV REDIS_HOST localhost
ENV REDIS_COUNTER_KEY hello_counter

ADD . /app

WORKDIR /app

RUN pip install flask==0.11.1
RUN pip install -r requirements.txt

RUN chmod +x /app/main.py

CMD [ "python", "/app/main.py" ]
