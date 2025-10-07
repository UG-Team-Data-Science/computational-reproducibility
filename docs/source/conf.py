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


revealjs_script_conf = {
    "hash": True,
    "width": 1280,
    "height": 720,
    "margin": 0.04,   # optional, space around the slides
    "minScale": 0.2,
    "maxScale": 2.0,
}

# revealjs_css_files = [
#     "revealjs/plugin/highlight/zenburn.css",
#     "https://cdn.jsdelivr.net/npm/reveal.js-plugins@latest/customcontrols/style.css",
# ]

# revealjs_script_plugins = [
#     {
#         "name": "RevealNotes",
#         "src": "revealjs/plugin/notes/notes.js",
#     },
#     {
#         "name": "RevealHighlight",
#         "src": "revealjs/plugin/highlight/highlight.js",
#     },
#     {
#         "name": "RevealMath",
#         "src": "revealjs/plugin/math/math.js",
#     },
#     {
#         "name": "RevealCustomControls",
#         "src": "https://cdn.jsdelivr.net/npm/reveal.js-plugins@latest/customcontrols/plugin.js",
#     },
# ]