FROM python:3.9-slim-buster

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
