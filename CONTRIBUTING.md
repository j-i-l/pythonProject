# Contributing to `[Project Name]`

> [!NOTE]
> Global Search & Replace: Update `[Project Name]` to your actual repository name. You will also need to update the GitHub URLs (currently `https://github.com/your-org/your-repo/...`) to point to your actual repository.

This outlines how to propose a change to `[Project Name]`.

## The "Pull request" process

In general, all edits to the `[Project Name]` package go through the process of a [Pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request).

### Fixing typos

If you spot typos or other language-related errors in the documentation, you may directly use the GitHub web interface to edit the source file. Simply click on the edit :pen: button, and GitHub will guide you through the process of forking the repository and creating a pull request.

### Beyond typos

If you would like to contribute bigger changes, please always refer to the [issue board](https://www.google.com/search?q=https://github.com/your-org/your-repo/issues) first!

> [!NOTE]
> Ensure the issue board links point to your repository. If you have specific contribution guidelines or a code-of-conduct document, link them in this section.

> [!NOTE]
> With the exception of simple typos, never open a pull request without an existing issue that it relates to!
> If you want to link a pull request to an issue, simply copy the link to the issue into the description of the pull request. If you are unsure how to do that, have a look at the official [GitHub documentation for pull requests](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue) for further details.

#### If you want to help...

...but have nothing specific in mind, simply head over to the [issue board](https://www.google.com/search?q=https://github.com/your-org/your-repo/issues) where you will find open issues labelled with `help wanted`. Feel free to comment on them if it is not clear to you what exactly the issue is about. Issues with the label `good first issue` might be good starting points if you are new to `[Project Name]`.

#### If you have a specific contribution...

...that you would like to add, first check the [issue board](https://www.google.com/search?q=https://github.com/your-org/your-repo/issues) (also see the closed issues) to see if you can find existing discussions related to the contribution you plan to make.

If yes, leave a comment on the related issue. If no, create a new issue describing the feature you want to implement.

Once the foreseen edits are documented in an issue, create a pull request and add your changes to the related branch.
The title of your pull request should briefly describe the change.
The body of your pull request should contain `Closes #issue-number`, where `#issue-number` is the identifier of the related issue.

## Development

We use [`uv`](https://www.google.com/search?q=%5Bhttps://docs.astral.sh/uv/%5D(https://docs.astral.sh/uv/)) for our development environment and dependency management.
`uv` is an extremely fast Python package and project manager that will automatically handle virtual environments and even download the correct Python version (we require `~=3.13.0`) if you don't already have it installed.

We suggest the following workflow for development:

* **Fork and Clone**: Fork the package on GitHub and clone it onto your computer using `git clone`.
* **Navigate**: Move into the project directory (`cd [Project Name]`).
* **Install `uv`**: If you haven't already, [install uv](https://docs.astral.sh/uv/getting-started/installation/) on your system.
* **Sync the Environment**: Run the following command to automatically create a virtual environment (`.venv`) and install the package in editable mode along with all dependencies:
```bash
uv sync

```
*This command reads our `pyproject.toml` and automatically installs the default dependencies as well as our `dev`, `test`, and `docs` dependency groups (which include tools like `pytest`, `ruff`, `black`, and `sphinx`).*
* **Run Commands**: You can execute tools directly within the isolated environment using `uv run`. For example:
```bash
uv run pytest      # Runs the test suite
uv run ruff check  # Runs the linter

```
*(Alternatively, you can manually activate the environment using `source .venv/bin/activate` on macOS/Linux or `.venv\Scripts\activate` on Windows).*
* **Branch and Edit**: Create a new branch for your pull request using `git checkout -b explicative-branch-name`.
* **Commit**: Edit the code in the `src/[mypkgs]/` directory, write tests, and commit your changes.

> [!NOTE]
> Global Search & Replace: Ensure `[Project Name]` matches your cloned repository folder name, and update `src/[mypkgs]/` to reflect the actual package directory defined in your `tool.hatch.build.targets.wheel` configuration.

### Managing Dependencies

If you need to add a new dependency while developing a feature:

* **Standard dependencies**: `uv add <package>`
* **Development dependencies**: `uv add --group dev <package>` (or `--group test` / `--group docs`)

Always commit the updated `pyproject.toml` and `uv.lock` files so other contributors can reproduce your exact environment.

> [!NOTE]
> Since this project uses Git tags for versioning via `hatch-vcs` (as defined in `pyproject.toml`), you do not need to manually bump versions in your source code files during standard feature development.
> The CI/CD release process will handle version numbering based on GitHub tags.

---

Does this align well with how you want your contributors interacting with `uv`? I can also adapt the testing section to explicitly use `uv run pytest` if you want to keep the toolchain instructions entirely unified!## Testing

The `[Project Name]` package uses a comprehensive, multi-layered testing infrastructure designed to ensure code quality while being efficient during development. Understanding when and how different tests run is essential for effective contribution.

### Automatic Testing During Development

When you create a pull request to any branch (except `main` and release branches), the package automatically runs **testing via GitHub Actions**:

* **Default environment**: Tests run against baseline Python version (i.e., Python 3.13) on Ubuntu.

> [!NOTE]
> Update the "Default environment" bullet to reflect your actual baseline Python version.
