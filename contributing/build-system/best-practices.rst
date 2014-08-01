.. _contribute-build-system-best-practices:

==============
Best Practices
==============

**mangos-zero** relies on `CMake`_ to produce build definitions and project
files on various platforms, such as Linux, Windows or Mac OS X.

To ensure that our project can be built on most platforms we enforce a few
rules when crafting ``CMakeLists.txt`` files.

.. caution::

    These rules are preliminary and based on the experiences with our new
    unified CMake build definitions.

    Rules may change. Make sure to check back.

Introduction
------------

Since we removed any platform specific build files, and just kept CMake
build definitions, we have found a few rules which will greatly ease
maintaining our build system, and ensuring it works on all platforms.

As with all things, there is a certain order to CMake definitions that
ensures thins will run smooth.


Includes First
--------------

CMake modules required come first

Sub directories
---------------

Any sub directories should follow.

Provide Options
---------------

Build switches a user can select.

Define the source
-----------------

Source lists, includes, dependencies - based on build switches

Configure it
------------

Variables and files to be combined

Build it
--------

Add library, executable - link dependencies, based on build switches

Tune it
-------

Set up compile time flags - based on build switches

Install it
----------

Install built app/library, configured files, and others - based on build switches

.. _CMake: http://cmake.org/
