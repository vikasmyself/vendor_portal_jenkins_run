# Use the official Python 3.11 image as the base image
FROM python:3.11-alpine

# Install necessary dependencies and tools
RUN apk update && apk add --no-cache \
    wget \
    ca-certificates \
    unzip \
    chromium \
    chromium-chromedriver \
    nss \
    libstdc++ \
    libx11 \
    libxcomposite \
    libxdamage \
    libxrandr \
    libxtst \
    libxkbcommon \
    gdk-pixbuf \
    ttf-freefont \
    && rm -rf /var/cache/apk/*

# Set environment variables for Chrome and ChromeDriver
ENV CHROME_BIN=/usr/bin/chromium-browser
ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver

# Set the working directory to /app
WORKDIR /app

# Copy the project files into the Docker image
COPY . /app

ENV PYTHONPATH=/app

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Expose the port on which the app will run (if needed)
# EXPOSE 80

# Command to run the tests or application (adjust as needed)
CMD ["pytest", "-v", "-s", "--browser", "chrome"]
