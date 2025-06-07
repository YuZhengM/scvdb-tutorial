# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'SCVdb'
copyright = '2025, Zheng-Min Yu'
author = 'Zheng-Min Yu'

release = '1.0.0'
version = '1.0.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'SCVdb': ('https://bio.liclab.net/scvdb/', None),
    'GitHub': ('https://github.com/YuZhengM/scvdb-tutorial', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
