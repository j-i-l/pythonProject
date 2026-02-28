# 1. Use an official, lightweight Python runtime
FROM python:3.13-slim

# 1. Install git (needed if you still want VCS tools, but not strictly required with the fix below)
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# 2. Get uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# 3. Receive the version from GitHub Actions
ARG VERSION
ENV SETUPTOOLS_SCM_PRETEND_VERSION=$VERSION

# 4. Copy project files
COPY . /app

# 5. Install (uv will now use the ENV variable instead of looking for .git)
RUN uv pip install --system --no-cache --compile-bytecode .

# 6. Run
CMD ["python", "scripts/drafts/say_hello.py"]
