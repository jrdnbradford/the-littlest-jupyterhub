# Use build args to select Ubuntu and Python versions
ARG UBUNTU_VERSION=22.04
FROM ubuntu:${UBUNTU_VERSION}

# Avoid interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Use build arg for Python version
ARG PYTHON_VERSION=3.10

# Install system dependencies
RUN apt-get update && apt-get install --yes \
    python${PYTHON_VERSION} \
    python${PYTHON_VERSION}-venv \
    python3-pip \
    bzip2 \
    git \
    && rm -rf /var/lib/apt/lists/*

# Create and activate virtual environment
RUN python${PYTHON_VERSION} -m venv /srv/venv
ENV PATH="/srv/venv/bin:$PATH"

# Set working directory
WORKDIR /app

# Copy requirements first for better layer caching
COPY ../dev-requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r dev-requirements.txt

# Copy the rest of the application
COPY ../ .

# Install the package in editable mode
RUN pip install -e .

# Default command runs pytest
CMD ["pytest", "tests"]
