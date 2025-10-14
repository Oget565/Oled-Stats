FROM python:3.12-slim

# Install i2c-tools for hardware access
RUN apt-get update && apt-get install -y \
    i2c-tools \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "app.py"]
