FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir pandas numpy mysql-connector-python prometheus_client

CMD ["python", "simulation.py"]