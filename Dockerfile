# Base image: Official Python 3.13 slim (Debian-based)
FROM python:3.13-slim

# Prevent interactive prompts and Python output buffering
ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONUNBUFFERED=1

# Install curl to download uv
RUN apt-get update && apt-get install -y curl \
    && rm -rf /var/lib/apt/lists/*

# Install uv directly from Astral
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app

# Copy dependency files first to leverage Docker layer caching
COPY pyproject.toml requirements.txt ./

# Install dependencies using uv into the system environment
RUN uv pip install --system -r requirements.txt

# Copy configuration and execution scripts
COPY config/ config/
COPY scripts/ scripts/

# Execute the payload
CMD ["python", "scripts/drafts/hello.py"]
