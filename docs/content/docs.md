# Working with the Documentation

This project uses [Sphinx](https://www.sphinx-doc.org/) to generate its documentation, powered by the **MyST Parser** (to write in Markdown instead of reStructuredText) and the **PyData Sphinx Theme**. We use `uv` to manage the isolated environment and dependencies.

## How to Build the Pages Locally

You don't need to install Sphinx globally. `uv` will handle downloading the dependencies and executing the build in an isolated environment.

**To build the HTML documentation once:**

```bash
# This reads the source files in docs/ and outputs the website to docs/_build/html
uv run sphinx-build -b html docs/ docs/_build/html

```

**To clean the build and start fresh** (useful if navigation or AutoAPI gets stuck):

```bash
rm -rf docs/_build docs/autoapi
uv run sphinx-build -b html docs/ docs/_build/html

```

**Live Preview (Recommended for writing):**
If you want the browser to automatically reload every time you save a `.md` or `.py` file, use the autobuild command:

```bash
uv run sphinx-autobuild docs/ docs/_build/html

```

## How to Add New Content

Because we use the MyST parser, you can write all your static pages in standard Markdown (`.md`).

1. **Create a new Markdown file** inside the `docs/` directory (e.g., `docs/tutorial.md`).
2. **Link it in the Table of Contents:** Open `docs/index.rst` (or `index.md`) and add the filename (without the `.md` extension) to the `toctree` directive so it shows up in the sidebar. If you want Sphinx to auto-number the sections, just add the `:numbered:` flag:

```rst
.. toctree::
   :maxdepth: 2
   :numbered:
   :caption: Contents:

   tutorial
   scripts

```

**Using Sphinx Features in Markdown:**
MyST allows you to use Sphinx directives inside Markdown using "fenced" code blocks. For example, to create a dropdown menu (powered by `sphinx_design`):

```markdown
```{dropdown} Click here for more info!
This is hidden content.
```

```

## How Docstrings are Parsed and Added

You do **not** need to manually document the Python modules in `src/mypkgs/`.

We use **`sphinx-autoapi`**, which statically parses our Python code and automatically generates the "API Reference" section of the website.

### Writing Docstrings

We strictly follow the **NumPy Docstring Standard**. AutoAPI (via Napoleon) parses these sections automatically.

```python
def calculate_area(length: float, width: float) -> float:
    """
    Calculate the area of a rectangle.

    Parameters
    ----------
    length : float
        The length of the rectangle.
    width : float
        The width of the rectangle.

    Returns
    -------
    float
        The calculated area.
    """
    return length * width

```

### Cross-Referencing

You can hyperlink to other functions, classes, or external libraries (like NumPy or Python built-ins) directly in your docstrings or `.md` files using Intersphinx roles:

* **Functions:**
  ```
  :func:`mypkgs.utils.get_config`
  ```
* **Classes:**
  ```
  :class:`numpy.ndarray`
  ```
* **Objects/Attributes:**
  ```
  :obj:`~numpy.matmul`
  ```
  *(Use the tilde`~` to hide the module prefix in the rendered text!)*

When you hover over links to our own code (or ReadTheDocs-hosted libraries like Rasterio), **`sphinx-tippy`** will display a live preview tooltip.


## Deployment to GitHub Pages

**File location:** `.github/workflows/deployDocs.yml`

This is the GitHub Actions workflow file.
It uses `uv` to set up the environment, builds the Sphinx docs, and uses GitHub's official Pages actions to deploy the static HTML.
