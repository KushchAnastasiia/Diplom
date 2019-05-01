FROM python:3.6.8
MAINTAINER zadoyan_mk@localhost

COPY ./src /src

WORKDIR /src

RUN pip install --no-cache-dir -r requirements/dev.txt

COPY ./docker/dev/entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]