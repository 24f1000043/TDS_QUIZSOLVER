# Use the official Playwright Python image
# This includes Python and the Chromium browser pre-installed!
FROM mcr.microsoft.com/playwright/python:v1.40.0-jammy

# Set the working directory
WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port (Render typically uses 10000, but we'll use an env var)
EXPOSE 10000

# Run the application using Gunicorn for production stability
# OR just run python app.py if you want to keep it simple for this project
CMD ["python", "app.py"]