FROM anyakichi/poetry-builder:3.9-full

ENV \
  DEFAULT_SCRIPT="poe start" \
  GIT_REPO=https://github.com/anyakichi/fastapi-sample.git

COPY pyproject.toml poetry.lock /build/
COPY fastapi_sample /build/fastapi_sample/
RUN chown -R builder:builder /build

WORKDIR /build

USER builder
RUN poetry install --no-dev

USER root

EXPOSE 8000
