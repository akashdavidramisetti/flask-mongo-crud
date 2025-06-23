# Use official Python image
FROM python:3.11

# Set working directory inside container
WORKDIR /app

# Copy dependency list and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy everything else
COPY . .

# Run the app
CMD ["python", "main.py"]
