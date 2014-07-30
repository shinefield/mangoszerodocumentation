====================
Documentation Format
====================

The **mangos-zero** documentation uses `reStructuredText`_ as its markup language and
`Sphinx`_ for building the output (HTML, PDF, ...).

reStructuredText
----------------

reStructuredText "is an easy-to-read, what-you-see-is-what-you-get plaintext
markup syntax and parser system".

You can learn more about its syntax by reading existing **mangos-zero** `documents`_
or by reading the `reStructuredText Primer`_ on the Sphinx website.

If you are familiar with Markdown, be careful as things are sometimes very
similar but different:

* Lists starts at the beginning of a line (no indentation is allowed);
* Inline code blocks use double-ticks (````like this````).

Sphinx
------

Sphinx is a build system that adds some nice tools to create documentation
from reStructuredText documents. As such, it adds new directives and
interpreted text roles to standard reST `markup`_.

Syntax Highlighting
~~~~~~~~~~~~~~~~~~~

All code examples uses C++ as the default highlighted language. You can change
it with the ``code-block`` directive:

.. code-block:: rst

    .. code-block:: text

        ############################################
        # MaNGOS realmd configuration file         #
        ############################################

        [RealmdConf]
        ConfVersion=2010062001

.. note::

    A list of supported languages is available on the `Pygments website`_.

.. _docs-configuration-blocks:

Configuration Blocks
~~~~~~~~~~~~~~~~~~~~

Whenever you show a configuration, you must use the ``code-block`` directive
to show the configuration ``Text only`` format.

.. code-block:: rst

    .. code-block:: text

        ############################################
        # MaNGOS realmd configuration file         #
        ############################################

        [RealmdConf]
        ConfVersion=2010062001


The previous reST snippet renders as follow:

.. code-block:: text

    ############################################
    # MaNGOS realmd configuration file         #
    ############################################

    [RealmdConf]
    ConfVersion=2010062001


The current list of supported formats are the following:

+-----------------+----------------+
| Markup format   | Displayed      |
+=================+================+
| cpp             | C++            |
+-----------------+----------------+
| sql             | SQL Statements |
+-----------------+----------------+
| text            | Text Only      |
+-----------------+----------------+

Adding Links
~~~~~~~~~~~~

To add links to other pages in the documents use the following syntax:

.. code-block:: rst

    :doc:`/path/to/page`

Using the path and filename of the page without the extension, for example:

.. code-block:: rst

    :doc:`/contributing/code/license`

The link text will be the main heading of the document linked to. You can
also specify alternative text for the link:

.. code-block:: rst

    :doc:`License </contributing/code/license>`

Testing Documentation
~~~~~~~~~~~~~~~~~~~~~

To test documentation before a commit:

* Install `Sphinx`_;

* Run the `Sphinx quick setup`_;

* Run ``make html`` and view the generated HTML in the ``build`` directory.

.. _reStructuredText:        http://docutils.sourceforge.net/rst.html
.. _Sphinx:                  http://sphinx-doc.org/
.. _documents:               http://bitbucket.org/mangoszero/documentation
.. _reStructuredText Primer: http://sphinx-doc.org/rest.html
.. _markup:                  http://sphinx-doc.org/markup/
.. _Pygments website:        http://pygments.org/languages/
.. _Sphinx quick setup:      http://sphinx-doc.org/tutorial.html#setting-up-the-documentation-sources
