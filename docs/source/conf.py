# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Reproducible Research: a computational approach'
copyright = '2025, V. Soancatl Aguilar'
author = 'V. Soancatl Aguilar'
release = 'v0.1-draft'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_revealjs'
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']


revealjs_html_theme = "revealjs-simple"
# revealjs_style_theme = 'sky'
revealjs_static_path = ["_static"]
revealjs_css_files = [
    "custom.css",
]

# revealjs_css_files = [
#     "revealjs/plugin/highlight/zenburn.css",
#     "https://cdn.jsdelivr.net/npm/reveal.js-plugins@latest/customcontrols/style.css",
# ]