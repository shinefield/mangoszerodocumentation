.. _contribute-build-system-overview:

========
Overview
========

**mangos-zero** does not provide any platform specific build files, such as GNU
Makefiles or Visual Studio project files.

.. image:: /_static/cmake100.png
   :alt:   CMake
   :align: right

Instead we chose to use `CMake`_, the Cross Platform Make toolkit, which basically
allows us to define dependencies, libraries, servers and command line tools in
simple text files which **CMake** then can turn into any build system you have
available at your hands.

.. note::

    We currently use CMake version *2.8.x*. The current build system has not yet
    been tested with `CMake 3`_.

.. _CMake:    http://cmake.org/
.. _CMake 3:  http://www.cmake.org/cmake/help/v3.0/release/3.0.0.html
