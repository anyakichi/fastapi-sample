FROM anyakichi/poetry-builder:3.9

ENV \
  DEFAULT_SCRIPT="poe start" \
  GIT_REPO=https://github.com/anyakichi/fastapi-sample.git
