FROM python:3.9-slim-buster

# Install build dependencies for pip
# RUN apk update && apk upgrade
# RUN apk add --no-cache gcc \
#                        python3-dev \
#                        gpgme-dev \
#                        libc-dev \
#                        musl-dev \
#                        libffi-dev \
#                        openssl-dev \
#                        cargo \
#     && rm -rf /var/cache/apk/*

# Poetry is used so that all dependencies can be audited & locked
# Install poetry & dependencies
RUN pip install --upgrade pip && pip install -U poetry
WORKDIR /tmp/poetry
COPY pyproject.toml /tmp/poetry
COPY poetry.lock /tmp/poetry
RUN poetry export -f requirements.txt --output requirements.txt
RUN pip install -r requirements.txt
RUN rm /tmp/poetry/*

WORKDIR /code

COPY . /code

CMD python3.9 app.py
