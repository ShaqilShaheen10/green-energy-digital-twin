FROM python:3.10-slim

WORKDIR /app

# Upgrade pip + avoid timeout issues
RUN pip install --upgrade pip

# Install packages with timeout + no cache
RUN pip install --no-cache-dir --default-timeout=200 \
    numpy \
    pandas \
    mysql-connector-python \
    prometheus_client

COPY . .

CMD ["python", "simulation/simulation.py"]