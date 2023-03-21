# Configuration file for the Sphinx documentation builder.
import os
pwd = os.path.dirname(os.path.abspath(__file__))

# -- Project information

project = 'scSELpy'
copyright = 'Mark Dedden'
author = 'Mark Dedden'

release = '0.1'
with open(pwd+"/../../scselpy/version.txt") as f:
	version = str(f.read())

# -- General configuration

extensions = [
#    'myst_parser',
    'myst_nb',
    'sphinx_gallery.load_style',
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
