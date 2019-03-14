#!/usr/bin/env python

import os
import redis
import logging
from flask import Flask, render_template, make_response

version = ""

app = Flask(__name__)

@app.route("/check")
def check():
  response = make_response("OK!")
  response.headers['hello-counter-version'] = version
  return response

@app.route("/")
def hello():
    try:
      redis_host = os.getenv('REDIS_HOST', 'localhost')
      redis_counter_key = os.getenv('REDIS_COUNTER_KEY', 'hello_counter')

      redis_server = redis.Redis(host=redis_host, socket_timeout=0.05)
      redis_server.incr('hello_counter', 1)
      visitor_number = redis_server.get('hello_counter')

      counter_message = render_template('counter_message_template', visitor_number=visitor_number)
    except:
      app.logger.error("Couldn't do something with Redis!")
      counter_message = ''

    message = "Hello World!"

    response = make_response(render_template('index.html', version=version, message=message, counter_message=counter_message))
    response.headers['hello-counter-version'] = version

    return response 
    
if __name__ == "__main__":
    listen_port = int(os.getenv('PORT', '80'))
    app.run(host='0.0.0.0', port=listen_port)
