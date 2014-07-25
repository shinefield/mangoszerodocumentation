mangos-zero
===========
This is official documentation repository for **mangos-zero**, a GPL licensed
server for [World of Warcraft][wow] version *1.12.x* (also known as
[vanilla WoW][wow-vanilla]).

The rendered version of this documentation is hosted by [Read The Docs][rtd],
and available on [docs.getmangos.com][mz-docs-live].

Documentation is based on [reStructuredText][sphinx-rest] and enhanced with
[Sphinx-specific markup][sphinx-markup], and processed by [Sphinx][sphinx] to
render various target formats such as HTML or PDF.

## Usage

To build the HTML version of the **mangos-zero** documentation, execute

    make html

in your clone of the documentation repository. Generated documentation will
be stored in `_build/html`.

A build requires only a few seconds to finish.

To clean up the build directory execute

    make clean

## Requirements

Aside from a decent text editor supporting text markup such as [Sublime Text][st],
you will need a local installation of [Sphinx][sphinx].

## Contributing

The **mangos-zero** documentation is hosted on [BitBucket][mz-docs]. Fork it,
and check out our [issue tracker][mz-docs-issues], where we keep track of
the documentation project.

Of course you can just browse the source files, and just edit as you like, too.

## License

**mangos-zero** [documentation][mz-docs] is copyright of the respective
authors and is available under the terms of the Creative Commons
[Attribution-NonCommercial-ShareAlike 3.0][cc-ancsa] license, except where
explicitly stated otherwise.

See [License.md](License.md) for further details, and the meaning of the
license.


[wow]: http://worldofwarcraft.com/
[wow-vanilla]: http://blizzard.com/games/wow/

[mz-docs]: http://bitbucket.org/mangoszero/documentation
[mz-docs-issues]: http://bitbucket.org/mangoszero/documentation/issues
[mz-docs-live]: http://docs.getmangos.com/

[rtd]: http://readthedocs.org/

[sphinx]: http://sphinx-doc.org/
[sphinx-rest]: http://sphinx-doc.org/rest.html#rst-primer
[sphinx-markup]: http://sphinx-doc.org/markup/index.html#sphinxmarkup

[st]: http://sublimetext.com/

[cc]: http://creativecommons.org/ "Creative Commons"
[cc-ancsa]: http://creativecommons.org/licenses/by-nc-sa/3.0/ "Creative Commons Attribution-NonCommercial-ShareAlike 3.0"
