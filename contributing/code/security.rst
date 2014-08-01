.. _contribute-code-security:

===============
Security Issues
===============

This document explains how **mangos-zero** issues are handled by the core team.

Reporting a Security Issue
--------------------------

If you think that you have found a security issue in **mangos-zero**, don't
use the bug tracker and do not post it publicly. Instead, all security
issues must be sent to **theluda [at] getmangos.com**. Emails sent to
this address are forwarded to the core team members.

Resolving Process
-----------------

For each report, we first try to confirm the vulnerability. When it is
confirmed, the team works on a solution following these steps:

1. Send an acknowledgement to the reporter;
2. Work on a patch;
3. Write a security announcement for the official **mangos-zero** `blog`_
   about the vulnerability. This post should contain the following
   information:

   * a title that always include the "Security release" string;
   * a description of the vulnerability;
   * the affected versions;
   * the possible exploits;
   * how to patch/upgrade/workaround affected applications;
   * credits.
4. Send the patch and the announcement to the reporter for review;
5. Apply the patch to all maintained versions of **mangos-zero**;
6. Publish the post on the official **mangos-zero** `blog`_;
7. Update the security advisory list (see below).

.. note::

    Releases that include security issues should not be done on Saturday or
    Sunday, except if the vulnerability has been publicly posted.

.. note::

    While we are working on a patch, please do not reveal the issue publicly.

.. _Git repository:      http://bitbucket.org/mangoszero7server
.. _blog:                http://getmangos.com/blog
