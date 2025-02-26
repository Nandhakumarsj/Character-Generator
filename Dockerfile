FROM python:3.10-slim-buster

# Set working directory
WORKDIR /app

# Install necessary packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    # Required for OpenCV or pillow (PIL) library
    libpq-dev \  
    # Useful for potential network operations or testing
    curl  

# Install Python libraries
RUN pip install --no-cache-dir google-generativeai flask python-dotenv

COPY . .

# Set environment variable for API Key (Best practice is to pass it at runtime, see instructions in the README below)
# ENV GOOGLE_API_KEY=YOUR_API_KEY  # Not recommended to hardcode in Dockerfile

# CMD ["/bin/bash"]
EXPOSE 5000
CMD ["python", "app.py"]
