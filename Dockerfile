# Use the official Python 3.12.4-slim image as the base image
FROM python:3.12.4-slim

# Install necessary dependencies and tools
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    wget \
    ca-certificates \
    unzip \
    chromium \
    chromium-driver \
    libnss3 \
    libgconf-2-4 \
    libasound2 \
    libx11-xcb1 \
    libxtst6 \
    libxss1 \
    libxrandr2 \
    libgl1-mesa-glx \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install curl
RUN apt-get update && apt-get install -y curl

# Set environment variables for Chrome and ChromeDriver
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver

# Set the working directory to /app
WORKDIR /usr/app

# Copy the project files into the Docker image
COPY . /usr/app

# Copy the wait-for-it.sh script and set execute permissions
COPY wait-for-it.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/wait-for-it.sh

# Set the Python path to include the /app directory
ENV PYTHONPATH=/usr/app

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Create logs directory
RUN mkdir -p /usr/app/logs

# Command to run the tests or application

ENTRYPOINT ["/usr/local/bin/wait-for-it.sh", "selenium-hub:4444", "--"]
CMD ["pytest", "-v", "-s", "--browser", "chrome"]

