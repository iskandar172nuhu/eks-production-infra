FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY test_app.py .
COPY templates ./templates
COPY static ./static

RUN useradd -m appuser
USER appuser

EXPOSE 5001

CMD ["python", "app.py"]