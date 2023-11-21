FROM python:3.9 AS compile-image
LABEL maintainer="Sylvain Boily <sylvain@wazo.io>"

RUN apt-get -qy update && apt-get -qy dist-upgrade

RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN mkdir /usr/src/api
COPY api /usr/src/api/
WORKDIR /usr/src/api/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python setup.py install

FROM python:3.9-slim-bullseye AS build-image
COPY --from=compile-image /opt/venv /opt/venv
COPY --from=compile-image /usr/src/api /usr/src/api

RUN set -x \
    && apt-get -qy update \
    && apt-get -qy dist-upgrade \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

EXPOSE 8999
ENV PATH="/opt/venv/bin:$PATH"
WORKDIR /usr/src/api/

ENTRYPOINT ["python3", "./main.py"]
