FROM python:3.8-slim-buster

WORKDIR /app

RUN pip install --upgrade pip

COPY ./main.py ./settings.toml ./config.py ./pyproject.toml ./poetry.lock /app/
COPY ./services/ /app/services/
COPY ./tts_model/ /app/tts_model/

RUN pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-dev

RUN mkdir /app/logs && touch tts.log
RUN chmod -R 777 /app/logs

EXPOSE 7700

CMD [ "python", "main.py" ]
