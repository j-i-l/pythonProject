import tomllib
import datetime
from pathlib import Path
from importlib.metadata import version as get_version

# -- Project information (Dynamically loaded from pyproject.toml) ------------

# Locate and parse the pyproject.toml file
# Assuming conf.py is in 'docs/' and pyproject.toml is in the root directory
pyproject_path = Path(__file__).parent.parent / "pyproject.toml"

with open(pyproject_path, "rb") as f:
    toml_data = tomllib.load(f)

# Extract metadata blocks
project_meta = toml_data.get("project", {})
urls_meta = project_meta.get("urls", {})

# Extract project attributes
project = project_meta.get("name", "Alternative Name")
description = project_meta.get("description", "")

# Extract and format authors
authors_list = project_meta.get("authors", [])
author = ", ".join([a.get("name") for a in authors_list if "name" in a])

# Auto-generate the copyright with the current year
current_year = datetime.date.today().year
copyright = f"{current_year}, {author}"

# Extract URLs
homepage_url = urls_meta.get("Homepage", "")
issues_url = urls_meta.get("Issues", "")
# try to get the owner
try:
    github_owner = homepage_url.split("github.com/")[1].split("/")[0]
except (IndexError, AttributeError):
    github_owner = "TODO"  # Set a fallback

master_doc = 'index'

# Dynamically fetch the version built by hatch-vcs
try:
    release = ".".join(get_version(project).split('.')[:2])
except Exception:
    release = "unknown"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx_design',
    'sphinx_togglebutton',
    "sphinx_copybutton",
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    "autoapi.extension",
    "sphinx_tippy",
]

# Napoleon autodoc settings
napoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
# Type hints only in description( not in signatures) for readability
autodoc_typehints = "description"
# also include everything in the scripts/ folder (ignoring drafts)
autoapi_dirs = ["../src/", "../scripts/"]

# -- Intersphinx configuration -----------------------------------------------
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# TODO: change this to your icon or logo (path inside the _static folder)
html_logo = "_static/images/logo.png"
# TODO: change this to your icon or logo
html_favicon = "_static/images/logo.png"

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
# NOTE: This is for custom styling and can be removed
html_css_files = ['custom-pst.css']

html_context = {
    "github_user": github_owner,  # Keep as is if it's your GitHub org/username
    "github_repo": project,       # Dynamically matches the project name
    "github_version": "main",
    "doc_path": "docs/",
    "default_mode": "light",
}

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_title = project
html_theme_options = {
    "use_edit_page_button": True,
    "navbar_start": ["navbar-logo"],
    "navbar_center": ["navbar-nav"],
    "navbar_end": ["theme-switcher", "navbar-icon-links"],
    "navbar_persistent": ["search-button"],
    "secondary_sidebar_items": ["page-toc", "edit-this-page", "sourcelink"],
    "footer_start": ["copyright", "sphinx-version"],
    # Optional integration of the URLs parsed from pyproject.toml
    "icon_links": [
        {
            "name": "GitHub",
            "url": homepage_url,
            "icon": "fa-brands fa-github",
        },
        {
            "name": "Issue Tracker",
            "url": issues_url,
            "icon": "fa-solid fa-bug",
        }
    ] if homepage_url or issues_url else [],
}

myst_enable_extensions = [
    "dollarmath",
    "attrs_block",
    "amsmath",
    "deflist",
    "colon_fence",
    # "html_admonition",
    # "html_image",
    # "smartquotes",
    # "replacements",
    # "linkify",
    # "substitution",
]

# -- AutoApi Extension config -------------------------------------------------
autoapi_dirs = ["../src/", ]
autoapi_member_order = "groupwise"
autoapi_python_class_content = "both"  # use both class and __init__( docstring
autoapi_options = [
    "members",
    "undoc-members",
    "special-members",
    "show-inheritance",
    "show-module-summary",
    # "imported-members",
    # "private-members",
]
autoapi_ignore = []
