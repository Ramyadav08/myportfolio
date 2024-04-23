# First stage: Build Stage
FROM python:3.10 AS builder

# Set the working directory in the container
WORKDIR /app

# Copy only the requirements file to optimize caching
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Second stage: Runtime Stage
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies from the builder stage
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages

# Copy the rest of the application code
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]