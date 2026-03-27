FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir pandas numpy flask mysql-connector-python prometheus_client

EXPOSE 8000

CMD ["python", "main.py"]