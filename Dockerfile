FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -U pip \
    && pip install --no-cache-dir -e .

EXPOSE 8000

CMD ["uvicorn", "gpdah.api:app", "--host", "0.0.0.0", "--port", "8000"]
