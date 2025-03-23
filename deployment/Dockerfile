
FROM python:3.10-slim

WORKDIR /app

COPY backend/requirements.txt backend/
RUN pip install --no-cache-dir -r backend/requirements.txt

COPY backend/ .
COPY frontend/ .

CMD ["uvicorn", "backend.app:app", "--host", "0.0.0.0", "--port", "8000"]
