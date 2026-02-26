# 1. Use an official, lightweight Python runtime
FROM python:3.13-slim

# 2. Copy the pre-compiled uv binary from the official image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# 3. Set the working directory inside the container
WORKDIR /app

# 4. Copy the project files into the container
COPY . /app

# 5. Install the package and dependencies using uv
# --system: Installs into the container's global Python (standard Docker practice)
# --no-cache: Prevents uv from caching downloaded wheels, keeping the image small
# --compile-bytecode: Pre-compiles .pyc files for slightly faster startup times
RUN uv pip install --system --no-cache --compile-bytecode .

# 6. Create a non-root user for security (Best Practice)
RUN useradd -m appuser && chown -R appuser /app
USER appuser

# 7. Run the script when the container launches
CMD ["python", "scripts/drafts/hello.py"]
