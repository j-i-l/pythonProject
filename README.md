# Python Project Template
<div align="center">

<img src="./docs/_static/images/logo.png" alt="Templte Logo" width="350">

<p>
  <a href="https://github.com/j-i-l/pythonProject"><img src="https://img.shields.io/github/stars/j-i-l/pythonProject?style=social" alt="Stars"></a>
     <a href="https://github.com/j-i-l/pythonProject/generate"><img src="https://img.shields.io/badge/Template-Use_this_template-2ea44f?style=social&logo=github" alt="Use Template"></a>
   <br>
  <img src="https://github.com/j-i-l/pythonProject/raw/python-coverage-comment-action-data/badge.svg" alt="Coverage">

  <a href="https://choosealicense.com/licenses/mit/">
    <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
  </a>
</p>
  <br>
  <br>
<pre>
   <small>A versatile template for python projects</small>
</pre>
</div>

> [!NOTE]
> A brief summary of the project's objective and what the codebase accomplishes.
> If the project has an extended doucmentation (in the `docs/` folder) provide a prominent link to the extended documentation.

<!-- README-header -->

## Installation

> [!NOTE]
> Provide the minimal, quick-start commands to set up the environment and install dependencies (e.g., `pip install .`).
> Link to the extended documentation for advanced configuration, troubleshooting, or podman guides.

> [!TIP]
> Installation for a package:

1. Setup or activeate your virtual environment using python 3.13:
   ```
   uv venv --python 3.13
   ```
2. Install the package directly from GitHub:
   ```
   uv pip install git+https://github.com/<owner>/<repo-name>.git
   ```
> [!TIP]
> Setup for an analysis/training/... **or** for package development:

1. Clone the repository:
   ```
   # use SSH if you prefere auth via ssh-key
   git clone https://github.com/<owner>/<repo-name>.git
   ```
2. Create a dedicated python environment and install all dependencies:
   ```
   uv sync
   ```

## Usage

> [!NOTE]
> Provide a single, copy-pasteable example of how to run a script locally to get the user started immediately.
> Reference the extended documentation for the complete API reference, parameter definitions, and edge cases.

## Data

> [!NOTE]
> Document where any related data resides, how it is accessed and by whom it is owned.
> Link to extended documentation for detailed data schemas, metadata, and full preprocessing pipelines.

## Methodology

> [!NOTE]
> List the core algorithms, mathematical models, or computational workflows utilized (e.g., "Uses a Convolutional Neural Network and Runge-Kutta integration").
> Further explanations should reside in the extended documentation.

## AI Usage

> [!NOTE]
> State if the project used any Artificial Intelligence (AI) applications and Large Language Models (LLMs).
> Mention if AI tools were used to generate content (Generative Usage) and or to alter existing content (Alterative Usage).

For detailed explanations on AI usage see the [`AI_USAGE.md`](./AI_USAGE.md) file.

## Citation

> [!NOTE]
> Provide a ready-to-copy BibTeX block for citing this software or the accompanying paper.

If you want to cite this project use the citation information provided in [`CITATION.cff`](./CITATION.cff).

## License

> [!NOTE]
> State the legal framework (e.g., MIT, GPL) governing the code.

The full license can be found in the [`LICENSE`](./LICENSE) file.

## Contributors

> [!NOTE]
> A brief acknowledgment of the main authors, labs, or funding agencies.
> Include a link to the [`CONTRIBUTING.md`](./CONTRIBUTING.md) file.

## Contact Information

> [!NOTE]
> Provide contact information (e.g. email) or clarify the method of contact (e.g. open an Issue) for inquiries.
