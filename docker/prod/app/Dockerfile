FROM python:3.7-slim
MAINTAINER zadoyan_mk@localhost

COPY ./src /src

WORKDIR /src

RUN pip install --no-cache-dir -r requirements/prod.txt

COPY ./docker/prod/app/entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]