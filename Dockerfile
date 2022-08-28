FROM ubuntu:20.04

# make sure we don't get prompted for input during apt install
ARG DEBIAN_FRONTEND=noninteractive

# don't cache pip packages, reduces the docker image size
ARG PIP_NO_CACHE_DIR=1

# see https://stackoverflow.com/questions/59812009/what-is-the-use-of-pythonunbuffered-in-docker-file
ENV PYTHONUNBUFFERED=1

RUN apt update -y && \
    apt upgrade -y && \
    apt install -y bash \
        build-essential \
        git \
        curl \
        ca-certificates \
        libjpeg-dev \
        libpng-dev \
        python3.9 \
        python3-pip && \
    rm -rf /var/lib/apt/lists

WORKDIR /app

# copying only poetry files before running poetry install makes sure docker
# reruns the build ONLY if poetry.lock/pyproject.toml change (otherwise,
# docker would need to rebuild this layer on ANY file change, which is annoying)
COPY poetry.lock pyproject.toml ./
RUN python3.9 -m pip install pip poetry && python3.9 -m poetry install

COPY . .

EXPOSE 8000

ENV UVICORN_HOST=0.0.0.0 \
    UVICORN_PORT=8000
CMD [ "/bin/bash", "-c", "python3.9 -m poetry run uvicorn app:app" ]
