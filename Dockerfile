FROM python:3.12-bookworm AS base

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

ARG UV_VERSION=0.10.8

USER root

SHELL [ "/bin/bash", "-euxo", "pipefail", "-c" ]
# hadolint ignore=DL3009  # this is a dev image
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    useradd --uid 1000 --user-group --create-home bot

ADD https://astral.sh/uv/${UV_VERSION}/install.sh /home/bot/Downloads/install-uv.sh

VOLUME [ "/bot/.venv" ]

RUN mkdir -p /bot && \
    chown -R bot:bot /bot && \
    chown -R bot:bot /home/bot && \
    mkdir -p /bot/.venv && \
    chown -R bot:bot /bot/.venv

USER bot

WORKDIR /bot

ENV PATH="/home/bot/.local/bin:${PATH}"

SHELL [ "/bin/sh", "-eu" ]
RUN /home/bot/Downloads/install-uv.sh

ENTRYPOINT [ "/bin/bash", "-euxo", "pipefail" ]
CMD [ "docker-entrypoint.dev.sh" ]
