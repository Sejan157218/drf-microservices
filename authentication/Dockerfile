# pull official base image
FROM python:3.11.4-slim-buster

# set work directory
WORKDIR /usr/src/app/authentication

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/authentication
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app/authentication

CMD ["gunicorn", "--bind", ":8001", "--workers", "3", "authentication.wsgi:application"]
