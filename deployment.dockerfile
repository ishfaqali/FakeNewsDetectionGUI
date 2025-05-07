# Base image
FROM pytorch/pytorch:2.0.1-cuda11.7-cudnn8-runtime

# Install dependencies
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Create app directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy model weights and code
COPY models/ ./models
COPY app.py .

# Expose API port
EXPOSE 8000

# Launch FastAPI
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]