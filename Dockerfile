# 1. Use an official, lightweight Python runtime
FROM python:3.13-slim

# NEW: Install git so the build backend can determine the package version
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# 2. Copy the pre-compiled uv binary from the official image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# 3. Set the working directory inside the container
WORKDIR /app

# 4. Copy the project files into the container
COPY . /app

# 5. Install the package and dependencies using uv
RUN uv pip install --system --no-cache --compile-bytecode .

# 6. Create a non-root user for security
RUN useradd -m appuser && chown -R appuser /app
USER appuser

# 7. Run the script when the container launches
CMD ["python", "scripts/drafts/hello.py"]
