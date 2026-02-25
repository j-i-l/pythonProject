# Unit Testing

Unit testing is a powerful tool that helps to achieve and maintain a solid code quality.
For it to be effective, unit tests should be tied to the development cycle and run automatically, so that during the development, one can directly check the outcome of the unit tests without having to take care of initiating them.

A suitable approach for such automated setup is to use CI/CD pipelines.
This project templates has a unit testing pipeline set up and here are all you need to know bout it:

**File location**: `.github/workflows/unitTests.yml`


This GitHub Actions workflow is for running Python unit tests and reporting test coverage directly on Pull Requests.

With `uv` and the `py-cov-action`, this workflow is highly optimized for speed and automated feedback.

Here is the breakdown of exactly what this workflow does, section by section.

### 1. The Triggers (`on`)

This section dictates **when** the workflow runs.

* **Push:** It triggers on direct pushes to the `main` branch.
* **Pull Request:** It triggers when PRs targeting `main` are opened, updated (`synchronize`), reopened, edited, or marked as "ready for review".

### 2. Job 1: `unit-tests`

This job handles the actual execution of your testing suite.

* **The Guardrail (`if`):** Even though the workflow *triggers* on pushes to `main`, this specific job is explicitly restricted to **Pull Requests only**, and it strictly **ignores Draft Pull Requests**. If someone opens a draft, it won't waste runner minutes.
* **Setup & Checkout:** It checks out your code on an `ubuntu-24.04` machine and explicitly pulls in any Git submodules if you have them.
* **Environment Setup (The Modern Way):** Instead of using standard `setup-python` and `pip`, it uses `astral-sh/setup-uv@v7` to install `uv` with automatic caching. Then, it runs `uv sync --group test` to instantly create the environment and fetch dependencies based on your `pyproject.toml`.
* **Execution:** It runs `pytest` via `uv run`.
* `-s`: Disables output capturing (shows print statements).
* `-vvv`: Maximum verbosity.
* `--cov`: Measures code coverage.
* It sets an environment variable to name the coverage file `.coverage.unittests`.


* **Artifact Storage:** Regardless of whether the tests pass or fail (`if: always()`), it takes the generated `.coverage.unittests` file and uploads it to GitHub's temporary storage so the next job can access it.

### 3. Job 2: `coverage`

This job takes the results from the first job, analyzes them, and posts a comment on the Pull Request.

* **Dependencies (`needs`):** It waits for `unit-tests` to finish. It will run whether the tests passed or failed, ensuring you still get a coverage report even if a test breaks.
* **Permissions:** It grants the GitHub Actions bot permission to write comments on PRs and read repository contents.
* **Download & Combine:** It downloads the coverage artifact uploaded in the previous step. The `merge-multiple: true` flag is a great touch—if you ever expand this workflow to run tests on multiple operating systems or Python versions, this will combine all their coverage files together.
* **The Commenter:** It uses `python-coverage-comment-action` to parse the `.coverage` file and automatically post (or update) a highly visual comment on the active Pull Request showing exactly which lines of code were covered or missed.
* **Fallback Storage:** It saves the raw text of the comment as an artifact. This is often used in advanced setups where PRs from forks don't have permission to comment directly, allowing a separate workflow to post it later.

---

**This setup is**:

1. **Cost-efficient:** It entirely skips Draft PRs.
2. **Fast:** It relies on `uv` for dependency resolution, which shaves significant time off the setup phase compared to standard `pip`.
3. **Decoupled:** By separating the test running from the coverage reporting, you keep the logs clean and make it easier to add more testing jobs (like integration tests or UI tests) later without rewriting the coverage logic.
