from alpine:latest

RUN apk add --no-cache python3-dev \
	&& pip3 install --upgrade pip

WORKDIR /app

COPY . /app

RUN  pip3 --no-cache-dir install -r requirements.txt

EXPOSE 5984 8000

CMD ["gunicorn", "--config", "gunicorn_conf.py", "web:app"]
