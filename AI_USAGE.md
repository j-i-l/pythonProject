# AI Usage Declaration

This file declares the usage of Artificial Intelligence (AI) and Large Language Models (LLMs) applications in the development of this project.

## 1. Tools Applied
* **[Tool Name, e.g., GitHub Copilot]** – Applied primarily for [e.g., inline code completion].
* **[Tool Name, e.g., OpenAI GPT-4]** – Applied primarily for [e.g., code alteration, text restructuring, error localization].


## 2. Generative Usage
*This section catalogs instances where AI was used to generate text, code, or data directly from prompts, without a pre-existing human draft.*

* **Code Boilerplate:** [e.g., "Generated the initial class structures and skeleton code for the data ingestion pipeline in `src/ingest.py`."]
* **Unit Tests:** [e.g., "Generated foundational unit tests for the utility functions in `tests/test_utils.py`."]
* **Documentation Drafting:** [e.g., "Generated the initial structure of the Sphinx `docs/` folder."]

## 3. Alterative Usage
*This section catalogs instances where human-authored content or code was submitted to an AI system to be restructured, reformatted, or translated.*

* **Code Alteration:** [e.g., "Applied AI to restructure the nested loops in the core mathematical model (`src/model.py`) into vectorized operations."]
* **Error Localization:** [e.g., "Input stack traces into the AI to locate the source of memory leaks during HPC cluster deployment."]
* **Text Alteration:** [e.g., "Applied AI to alter the phrasing, syntax, and grammar of the methodology documentation and README."]
* **Data Reformatting:** [e.g., "Applied AI to generate scripts that convert raw instrument outputs from `.txt` format into structured `.json` format."]

## 4. Strict Exclusions
*The application of AI tools was strictly excluded from the following areas of the project:*

* **Hypothesis & Experimental Design:** The core scientific questions, theoretical frameworks, and experimental methodologies were developed entirely by the human researchers.
* **Data Manipulation:** AI tools were not used to synthesize, alter, interpolate, or extrapolate raw experimental or observational data. 
* **Result Interpretation:** The analysis of pipeline outputs and the formulation of scientific conclusions were performed solely by human authors.

## 5. Human Oversight & Verification
*This section details the protocols applied to review AI-generated and AI-altered outputs prior to integration.*

* **Testing:** All AI-generated and AI-altered code underwent human review and was required to pass the automated test suite (`pytest`) prior to merging.
* **Literature Verification:** Algorithmic structures or scientific concepts output by the AI were cross-referenced with primary literature.
* **Responsibility:** The human contributors hold absolute and final responsibility for the accuracy, legality, and scientific validity of all code, data, and text within this repository.
