FROM python:3
ADD server.py /
ADD templates /
RUN pip install flask
RUN pip install gevent
EXPOSE 5000
CMD [ "python", "./server.py" ]