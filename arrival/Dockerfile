FROM python:3.7-slim AS app

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get clean

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY app app
COPY docker-entrypoint.sh .

ENV PYTHONPATH "${PYTHONPATH}:/"
WORKDIR /

EXPOSE 8080
ENTRYPOINT [ "/docker-entrypoint.sh" ]
