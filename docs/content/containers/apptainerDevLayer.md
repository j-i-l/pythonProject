# Apptainer Development Layer

This setup decouples the **toolchain** from the **project workspace**.

* **The Container (`dev.sif`):** An immutable image containing system libraries and the `uv` manager.
* **The Host Workspace:** Your project directory containing `pyproject.toml` and the `.venv`.
* **Python Versioning:** The container provides a base Python version, but `uv sync` manages the specific version requested in your `pyproject.toml`. If your project requires Python 3.12, `uv` will download that version into the host-side `.venv` regardless of the container's internal 3.13 default.

---

### The Definition File (`containers/dev.def`)

```bash
Bootstrap: docker
From: python:3.13-slim

%post
    # Install system-level tools inside the image
    apt-get update && \
    apt-get install -y --no-install-recommends curl ca-certificates git
    rm -rf /var/lib/apt/lists/*

    # Install the uv package manager inside the image
    curl -LsSf https://astral.sh/uv/install.sh | env UV_INSTALL_DIR="/usr/local/bin" sh

%environment
    # Forces the container to prioritize the .venv in the current host directory
    export VIRTUAL_ENV="$PWD/.venv"
    export PATH="$VIRTUAL_ENV/bin:$PATH"
    
    # Ensures uv manages the Python version within the host-side .venv
    export UV_PROJECT_ENVIRONMENT="$VIRTUAL_ENV"

%runscript
    # 1. Sync Mode: Triggered by calling the image with no arguments
    if [ $# -eq 0 ]; then
        if [ -f "pyproject.toml" ]; then
            uv sync --group dev
            echo ">>> Success: Host .venv synchronized via container."
        else
            echo ">>> Error: No pyproject.toml found in $PWD."
            exit 1
        fi
        exit 0
    fi

    # 2. Execution Mode: Passes host commands into the container's context
    exec "$@"

```

---

### Mechanics: How the Layer Functions

This setup uses Apptainer’s ability to map the host filesystem into the container's namespace.

1. **File Mapping:** Apptainer automatically "bind-mounts" your current directory. Both the host and the container see the same project files.
2. **The "Hollow" Venv:** When you run the sync command, `uv` (running inside the container) writes the libraries and the requested Python interpreter to the `.venv` on your host.
3. **Path Precedence:** The `%environment` block prepends `$PWD/.venv/bin` to the container's `PATH`. When the container executes `python`, it finds the version in your host's `.venv` first.
4. **Interpreter Execution:** The binaries inside the `.venv` execute using the container's kernel namespace and system-level C libraries.

---

### Usage Workflow

If your terminal is inside your project root, the commands look like this:

1. **Build the Layer:**
```bash
apptainer build dev.sif containers/dev.def

```


2. **Synchronize the Host:**
Run the image with no arguments to create/update the `.venv`.
```bash
./dev.sif

```


3. **Execute through the Layer:**
Run your code or tests while staying in your host terminal.
```bash
./dev.sif python main.py
./dev.sif pytest

```

Since the `.venv` is physically located on your host, your IDE can point to it for local syntax highlighting and type checking, while the `dev.sif` handles the actual execution.

