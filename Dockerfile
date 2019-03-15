FROM python:3
ADD server.py /
ADD templates /
RUN pip install flask
EXPOSE 5000
CMD [ "python", "./server.py" ]