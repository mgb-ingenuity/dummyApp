FROM python:3.9

# Install poetry: https://python-poetry.org/docs/#installation
RUN curl -sSL https://install.python-poetry.org | python3 -


WORKDIR /code

COPY ./pyproject.toml .


RUN poetry install