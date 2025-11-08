FROM python:3.10.19-slim

WORKDIR /app

RUN pip install --upgrade pip

COPY ./main.py ./settings.toml ./config.py ./pyproject.toml ./poetry.lock /app/
COPY ./services/ /app/services/
COPY ./tts_model/ /app/tts_model/

RUN pip install poetry
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --without dev

RUN mkdir /app/logs && touch tts.log
RUN chmod -R 777 /app/logs

EXPOSE 7700

CMD [ "python", "main.py" ]
