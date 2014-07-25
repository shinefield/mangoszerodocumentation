# -*- coding: utf-8 -*-

import sys
import os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "_exts")))

# -- General configuration ------------------------------------------------
# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.doctest', 'sphinx.ext.todo', 'sphinx.ext.coverage', 'sphinx.ext.pngmath', 'sphinx.ext.mathjax', 'sphinx.ext.ifconfig']

# The suffix of source filenames.
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'mangos-zero'
copyright = u'2013-2014, Daniel S. Reichenbach'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.2'
# The full version, including alpha/beta/rc tags.
release = '0.2.0'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "mangos_rtd_theme"

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ["_themes", ]

# Output file base name for HTML help builder.
htmlhelp_basename = 'mangos-zero-doc'

# -- Options for manual page output ---------------------------------------
man_pages = [
    ('index', 'mangos-zero', u'mangos-zero Documentation',
     [u'Daniel S. Reichenbach'], 1)
]
