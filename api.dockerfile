FROM python:3.9 as DEPS

# every subsequent command is relative to this path in the container:
WORKDIR /code

# install deps
COPY ./requirements.txt .
RUN python -m pip install -r requirements.txt

# copy entire app
COPY . .

CMD uvicorn dummyapp.app:app --host 0.0.0.0 --port $PORT