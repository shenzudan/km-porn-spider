FROM python:3-slim

WORKDIR ./docker_demo

ADD . .

RUN pip install -r requirements.txt

CMD ["python", "./src/main.py"]
