FROM python:3.10

# Выбор папки, в которой будет вестись работа

WORKDIR code

# Установка зависимостей проекта
COPY requirements.txt .

RUN pip install -r requirements.txt

# Перенос проекта в образ
COPY . .

EXPOSE 8001

CMD uvicorn app.main:app --host 0.0.0.0 --port 8001