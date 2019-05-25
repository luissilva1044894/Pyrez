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
from pyrez import __version__ as pyrez
project = pyrez.__package_name__
copyright = pyrez.__copyright__
author = pyrez.__author__

# The full version, including alpha/beta/rc tags
version = pyrez.__version__
release = pyrez.__version__

# -- Options for Epub output ----------------------------------------------
# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

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
autodoc_member_order = 'bysource'

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
  '.DS_Store'
]

autodoc_member_order = 'bysource'

rst_epilog = rst_prolog = """
.. |coro| replace:: This function is a |corourl|_.
.. |corourl| replace:: *coroutine*
.. _corourl: https://docs.python.org/3/library/asyncio-task.html#coroutine
.. |dailyexcep| replace:: pyrez.exceptions.DailyLimit: |dailydesc|
.. |dailydesc| replace:: Raised when the daily request limit is reached.
"""

pygments_style = 'sphinx'#'friendly'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
#if not on_rtd:  # only import and set the theme if we're building docs locally
#  import sphinx_rtd_theme
#  html_theme = 'sphinx_rtd_theme'
#  html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

source_suffix = {
  '.rst': 'restructuredtext',
  '.txt': 'restructuredtext',
  '.md': 'markdown',
}
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = True


needs_sphinx = '2.0'
