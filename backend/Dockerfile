FROM python:3.11-slim

ENV POETRY_VERSION=1.8.2
WORKDIR /backend

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && ln -s /root/.local/bin/poetry /usr/local/bin/poetry \
    && poetry config virtualenvs.create false \
    && apt-get clean

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-interaction --no-ansi

COPY . .

CMD ["poetry", "run", "gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000"]
