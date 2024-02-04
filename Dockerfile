FROM python:3.8

ARG SECRET_KEY
ARG DB_NAME
ARG DB_USER
ARG DB_PASSWORD
ARG DB_HOST
ARG DB_PORT

ENV SECRET_KEY ${SECRET_KEY}
ENV DB_NAME ${DB_NAME}
ENV DB_USER ${DB_USER}
ENV DB_PASSWORD ${DB_PASSWORD}
ENV DB_HOST ${DB_HOST}
ENV DB_PORT ${DB_PORT}

WORKDIR /app

COPY requirements.txt requirements.txt

RUN python -m venv venv && \
    . venv/bin/activate && \
    python -m pip install --upgrade pip \
    pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
CMD ["sh", "-c", "python -m venv venv && . venv/bin/activate && python manage.py migrate && gunicorn --bind 0.0.0.0:8000 cirrhocheck.wsgi"]