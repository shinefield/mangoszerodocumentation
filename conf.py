# -*- coding: utf-8 -*-

import sys
import os

from sphinx.highlighting import lexers
from pygments.lexers.web import PhpLexer

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.doctest', 'sphinx.ext.todo', 'sphinx.ext.coverage', 'sphinx.ext.pngmath', 'sphinx.ext.mathjax', 'sphinx.ext.ifconfig', 'sensio.sphinx.configurationblock']
source_suffix = '.rst'
master_doc = 'index'
project = u'mangos-zero'
copyright = u'2013-2014, Daniel S. Reichenbach'
version = '0.1'
release = '0.1.2'
exclude_patterns = ['_build']
pygments_style = 'sphinx'
html_theme = "sphinx_rtd_theme"
html_theme_path = ["_themes", ]
htmlhelp_basename = 'mangos-zero-doc'
man_pages = [
    ('index', 'mangos-zero', u'mangos-zero Documentation',
     [u'Daniel S. Reichenbach'], 1)
]
sys.path.append(os.path.abspath('_exts'))
lexers['php'] = PhpLexer(startinline=True)
lexers['php-annotations'] = PhpLexer(startinline=True)
primary_domain = 'php'
