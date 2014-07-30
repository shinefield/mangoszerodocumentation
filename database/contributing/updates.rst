.. _db-contributing-content-updates:

===============
Content Updates
===============

A *content update* is defined as a set of SQL queries which insert an
atomic unit of game content which just works.

Introduction
------------

Any content update starts with a healthy dose of
`research <Research>`__. Once your research is complete, you should
create a `new
issue <http://bitbucket.org/mangoszero/content/issues/new>`__ on the
issue tracker.

Documenting the update
----------------------

For contributing to our project, it is considered mandatory to create a
`new issue <http://bitbucket.org/mangoszero/content/issues/new>`__ for
each update.

Currently we support five issue components:

-  Creatures
-  Games objects
-  Items
-  Quests
-  Events

Selecting the component and the release version for which the issue
should be valid should be considered carefully. Here is a few examples:

1. You want to add the quest `Rite of
   Vision <http://www.wowhead.com/quest=772>`__ to the database, thus
   you would create an issue named "Quest: Rite of Vision" - the prefix
   should be identical to the component for easier sorting.
2. Now you document the quest template, involved creatures, movements,
   scripts, etc. in your issue.
3. Once you're finished with documentation, add a comment to your issue,
   with a request for review. One or more developers will be reviewing
   your issue, and - if possible - add further documentation, or provide
   some hints for improvements or praise, well, the later one of course
   if you did an awesome job.
4. Once your ticket has been reviewed and documentation is considered
   final by one or more developers, you should fork the database
   repository and submit a pull request.

When crafting your issue, feel free to attach images, add links to
relevant sites, or even to `YouTube <http://youtube.com/>`__ videos for
the content in question. Anything that provides proof for the content
being correct is welcome.

Building an update
------------------

Submitting an update
--------------------
