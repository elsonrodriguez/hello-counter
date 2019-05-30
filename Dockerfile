FROM python:2.7

ENV REDIS_HOST localhost
ENV REDIS_COUNTER_KEY hello_counter

RUN pip install flask==0.11.1

RUN pip install -r requirements.txt

ADD . /app

RUN chmod +x /app/main.py

CMD [ "python", "/app/main.py" ]
