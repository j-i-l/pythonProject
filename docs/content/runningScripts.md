# Local Execution & Configuration

To maximize flexibility and testability, this project does not hardcode configuration paths. Instead, it relies on environment variables injected at runtime, falling back to command-line interface (CLI) arguments.

## 1. The `.env` File

For local development, we use a `.env` file to store paths and secrets. This file should be placed in the root of the repository and must **never be committed to version control**.

### Template (`.env.example`)

We provide an `.env.example` file in the repository. Copy this file to `.env` and adjust the values as needed:

```ini
# ====================================================================
# Environment Configuration Template
# ====================================================================

# The absolute or relative path to your JSON configuration file.
# REQUIRED if not passed via the --config-file CLI flag.
CONFIG_PATH=./config/settings.json

# The directory where generated files and results will be saved.
# REQUIRED if not passed via the --output-dir CLI flag.
OUTPUT_DIR=./results

```

## 2. Running Scripts Locally

This project manages dependencies via `pyproject.toml` and relies on environment variable injection before script execution. There are two ways to run the code locally.

### Setup (First Time Only)

Ensure your virtual environment is created and your dependencies are synced using `uv`:

```bash
uv sync

```

---

### Option A: Using `uv run` (Recommended)

`uv run` is the fastest method because it automatically detects your virtual environment and **natively loads `.env` files** from the project root.

```bash
uv run python scripts/drafts/hello.py

```

### Option B: Using standard Virtual Environment Activation

If you prefer to work within an activated virtual environment, you will need to manually inject the `.env` file using the `dotenv` CLI (which is installed via our `pyproject.toml` dependencies).

**1. Activate the environment:**

```bash
# On Linux/macOS
source .venv/bin/activate

# On Windows
.venv\Scripts\activate

```

**2. Run the script via dotenv:**

```bash
dotenv run -- python scripts/drafts/hello.py

```

```{note}
Both execution methods ensure that `hello.py` thinks the environment variables were natively provided by the operating system. This makes your local development environment behave exactly like a production Docker container.

```

---

## 3. Using CLI Overrides

The application is built with `argparse` handling the fallback logic. If you need to quickly run the script with a different configuration or output directory, you can override the injected `.env` variables by passing explicit arguments to the script:

**Using `uv`:**

```bash
uv run python scripts/drafts/hello.py \
    --config-file ./config/experiment_2.json \
    --output-dir ./results/experiment_2

```

**Using activated environment:**

```bash
dotenv run -- python scripts/drafts/hello.py \
    --config-file ./config/experiment_2.json \
    --output-dir ./results/experiment_2

```

If neither the environment variables nor the CLI arguments are provided, the script will intentionally fail and raise a clean error to prevent accidental runs with missing configurations.

