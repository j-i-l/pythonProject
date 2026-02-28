# 1. Use an official, lightweight Python runtime
FROM python:3.13-slim

# 2. Install git so the build backend can determine the package version
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# 3. Copy the pre-compiled uv binary from the official image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# 4. Set the working directory inside the container
WORKDIR /app

# 5. Copy the project files into the container (respecting .dockerignore)
COPY . /app

# 6. Install the package and dependencies using uv
RUN uv pip install --system --no-cache --compile-bytecode .

# 7. Create a non-root user for security
RUN useradd -m appuser && chown -R appuser /app
USER appuser

# 8. Run the script when the container launches
CMD ["python", "scripts/drafts/hello.py"]
