# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('.'))

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

# -- Project information -----------------------------------------------------
import pyrez #from pyrez import __version__ as pyrez
epub_title = project = pyrez.__package_name__.capitalize()
epub_copyright = copyright = pyrez.__copyright__
epub_publisher = epub_author = author = pyrez.__author__

# The full version, including alpha/beta/rc tags
version = release = pyrez.__version__

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
  'sphinx.ext.autodoc',
  'sphinx.ext.autosectionlabel',
  'sphinx.ext.extlinks',
  'sphinx.ext.intersphinx',
  'sphinx.ext.napoleon',
  'sphinx.ext.todo',
  #'sphinx.ext.viewcode',
  'sphinxcontrib.asyncio',
]

if on_rtd:
  # The master toctree document.
  master_doc = 'index'

html_context = {
  'on_rtd' : on_rtd
}
if not on_rtd:
  import sphinx_rtd_theme
  html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_theme = ['sphinx_rtd_theme', 'default'][0]

intersphinx_mapping = {
  "python": ('https://docs.python.org/3', None),
  #"aiohttp": ('https://aiohttp.readthedocs.io/en/stable/', None),
  "requests": ('https://requests.readthedocs.io/en/stable/', None),
}
extlinks = {
  'issue': ('https://github.com/luissilva1044894/pyrez/issues/%s', 'GH-'),
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
  '_build',
  'Thumbs.db',
  '.DS_Store',
  'global.rst',
]

autodoc_member_order = ['groupwise', 'alphabetical', 'bysource'][0]

rst_epilog = """
.. include:: global.rst
"""
#rst_prolog = open('global.rst', 'r').read()

pygments_style = ['sphinx', 'friendly'][0]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme_options = {
  'prev_next_buttons_location': 'bottom',
  'style_external_links': True,
  'navigation_depth': 4,
}

source_suffix = {
  '.rst': 'restructuredtext',
  '.txt': 'restructuredtext',
  '.md': 'markdown',
}

# Output file base name for HTML help builder.
htmlhelp_basename = project + 'doc'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If true, links to the reST sources are added to the pages.
# If false, no module index is generated.
html_show_sourcelink = latex_use_modindex = html_use_modindex = not on_rtd

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_sphinx = html_show_copyright = on_rtd

needs_sphinx = ['1.8', '2.0'][0 if on_rtd else 1]

highlight_language = 'python'
