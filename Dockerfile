FROM python:2.7

ENV REDIS_HOST localhost
ENV REDIS_COUNTER_KEY hello_counter

RUN pip install flask==0.11.1
RUN pip install redis==2.10.5

ADD . /app

RUN chmod +x /app/hello-counter.py

CMD [ "python", "/app/hello-counter.py" ]
