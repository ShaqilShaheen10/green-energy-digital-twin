FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip + increase timeout
RUN pip install --upgrade pip

# Copy requirements
COPY requirements.txt .

# Install with higher timeout (VERY IMPORTANT)
RUN pip install --no-cache-dir --default-timeout=200 -r requirements.txt

# Copy rest of code
COPY . .

CMD ["python", "simulation/simulation.py"]