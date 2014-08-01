.. _contribute-code-patches:

==================
Submitting a Patch
==================

Patches are the best way to provide a bug fix or to propose enhancements to
**mangos-zero**.

Step 1: Setup your Environment
------------------------------

Install the Software Stack
~~~~~~~~~~~~~~~~~~~~~~~~~~

Before working on **mangos-zero**, setup a C++ friendly environment with the
following software:

* Git;
* GCC 4.7 or above;
* MySQL 5.5 or above;
* CMake 2.8 or above;
* zlib;
* bzip2;
* OpenSSL;
* ACE 6.0 or above;

Configure Git
~~~~~~~~~~~~~

Set up your user information with your real name and a working email address:

.. code-block:: bash

    $ git config --global user.name "Your Name"
    $ git config --global user.email you@example.com

.. tip::

    If you are new to Git, you are highly recommended to read the excellent and
    free `ProGit`_ book.

.. tip::

    If your IDE creates configuration files inside the project's directory,
    you can use global ``.gitignore`` file (for all projects) or
    ``.git/info/exclude`` file (per project) to ignore them.

.. tip::

    Windows users: when installing Git, the installer will ask what to do with
    line endings, and suggests replacing all LF with CRLF. This is the wrong
    setting if you wish to contribute to **mangos-zero**. Selecting the as-is
    method is your best choice, as Git will convert your line feeds to the ones
    in the repository. If you have already installed Git, you can check the value
    of this setting by typing:

    .. code-block:: bash

        $ git config core.autocrlf

    This will return either "false", "input" or "true"; "true" and "false" being
    the wrong values. Change it to "input" by typing:

    .. code-block:: bash

        $ git config --global core.autocrlf input

    Replace --global by --local if you want to set it only for the active
    repository

Get the mangos-zero Source Code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Get the **mangos-zero** source code:

* Create a `BitBucket`_ account and sign in;

* Fork the `mangos-zero repository`_ (click on the "Fork" button);

* After the "forking action" has completed, clone your fork locally
  (this will create a ``server`` directory):

.. code-block:: bash

      $ git clone git@bitbucket.org:YOURUSERNAME/server.git

* Add the upstream repository as a remote:

.. code-block:: bash

      $ cd server
      $ git remote add upstream git@bitbucket.org:mangoszero/server.git

Step 2: Work on your Patch
--------------------------

The License
~~~~~~~~~~~

Before you start, you must know that all the patches you are going to submit
must be released under the *GPL version 2 license*, unless explicitly specified
in your commits.

Create a Topic Branch
~~~~~~~~~~~~~~~~~~~~~

Each time you want to work on a patch for a bug or on an enhancement, create a
topic branch:

.. code-block:: bash

    $ git checkout -b BRANCH_NAME develop

.. tip::

    Use a descriptive name for your branch (``issue_XXX`` where ``XXX`` is the
    GitHub issue number is a good convention for bug fixes).

The above checkout commands automatically switch the code to the newly created
branch (check the branch you are working on with ``git branch``).

Work on your Patch
~~~~~~~~~~~~~~~~~~

Work on the code as much as you want and commit as much as you want; but keep
in mind the following:

* Read about the **mangos-zero** :doc:`conventions <conventions>` and follow the
  coding :doc:`standards <standards>` (use ``git diff --check`` to check for
  trailing spaces -- also read the tip below);

* Do atomic and logically separate commits (use the power of ``git rebase`` to
  have a clean and logical history);

* Squash irrelevant commits that are just about fixing coding standards or
  fixing typos in your own code;

* Never fix coding standards in some existing code as it makes the code review
  more difficult (submit CS fixes as a separate patch);

* Write good commit messages (see the tip below).

.. tip::

    A good commit message is composed of a summary (the first line),
    optionally followed by a blank line and a more detailed description. The
    summary should start with the Component you are working on in square
    brackets (``[Core]``, ``[Documentation]``, ...). Use a
    verb (``fixed ...``, ``added ...``, ...) to start the summary and **don't
    add a period at the end**.

Prepare your Patch for Submission
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When your patch is not about a bug fix (when you add a new feature or change
an existing one for instance), it must also include the following:

* An explanation of the changes in the relevant ``CHANGELOG`` file(s) (the
  ``[BC BREAK]`` or the ``[DEPRECATION]`` prefix must be used when relevant);

* An explanation on how to upgrade an existing application in the relevant
  ``UPGRADE`` file(s) if the changes break backward compatibility or if you
  deprecate something that will ultimately break backward compatibility.

Step 3: Submit your Patch
-------------------------

Whenever you feel that your patch is ready for submission, follow the
following steps.

Rebase your Patch
~~~~~~~~~~~~~~~~~

Before submitting your patch, update your branch (needed if it takes you a
while to finish your changes):

.. code-block:: bash

    $ git checkout develop
    $ git fetch upstream
    $ git merge upstream/develop
    $ git checkout BRANCH_NAME
    $ git rebase develop

When doing the ``rebase`` command, you might have to fix merge conflicts.
``git status`` will show you the *unmerged* files. Resolve all the conflicts,
then continue the rebase:

.. code-block:: bash

    $ git add ... # add resolved files
    $ git rebase --continue

Push your branch remotely:

.. code-block:: bash

    $ git push --force origin BRANCH_NAME

Make a Pull Request
~~~~~~~~~~~~~~~~~~~

You can now make a pull request on the ``mangoszero/server`` BitBucket repository.

To ease the core team work, always include the modified components in your
pull request message, like in:

.. code-block:: text

    [Core] Fixed something
    [BuildSystem] Supported something

The pull request description must include the following checklist at the top
to ensure that contributions may be reviewed without needless feedback
loops and that your contributions can be included into **mangos-zero** as
quickly as possible:

.. code-block:: text

    | Q             | A
    | ------------- | ---
    | Bug fix?      | [yes|no]
    | New feature?  | [yes|no]
    | BC breaks?    | [yes|no]
    | Deprecations? | [yes|no]
    | Tests pass?   | [yes|no]
    | Fixed tickets | [comma separated list of tickets fixed by the PR]
    | License       | GPL version 2
    | Doc PR        | [The reference to the documentation PR if any]

An example submission could now look as follows:

.. code-block:: text

    | Q             | A
    | ------------- | ---
    | Bug fix?      | no
    | New feature?  | no
    | BC breaks?    | no
    | Deprecations? | no
    | Fixed tickets | #12, #43
    | License       | GPL version 2
    | Doc PR        | mangoszero/documentation#123

The whole table must be included (do **not** remove lines that you think are
not relevant). For simple typos, minor changes in the PHPDocs, or changes in
translation files, use the shorter version of the check-list:

.. code-block:: text

    | Q             | A
    | ------------- | ---
    | Fixed tickets | [comma separated list of tickets fixed by the PR]
    | License       | GPL version 2

Some answers to the questions trigger some more requirements:

 * If you answer yes to "Bug fix?", check if the bug is already listed in the
   issues and reference it/them in "Fixed tickets";

 * If you answer yes to "New feature?", you must submit a pull request to the
   documentation and reference it under the "Doc PR" section;

 * If you answer yes to "BC breaks?", the patch must contain updates to the
   relevant ``CHANGELOG`` and ``UPGRADE`` files;

 * If you answer yes to "Deprecations?", the patch must contain updates to the
   relevant ``CHANGELOG`` and ``UPGRADE`` files;

If some of the previous requirements are not met, create a todo-list and add
relevant items:

.. code-block:: text

    - [ ] Submit changes to the documentation
    - [ ] Document the BC breaks

If the code is not finished yet because you don't have time to finish it or
because you want early feedback on your work, add an item to todo-list:

.. code-block:: text

    - [ ] Finish the feature
    - [ ] Gather feedback for my changes

As long as you have items in the todo-list, please prefix the pull request
title with "[WIP]".

In the pull request description, give as much details as possible about your
changes (don't hesitate to give code examples to illustrate your points). If
your pull request is about adding a new feature or modifying an existing one,
explain the rationale for the changes. The pull request description helps the
code review.

In addition to this "code" pull request, you must also send a pull request to
the `documentation repository`_ to update the documentation when appropriate.

Rework your Patch
~~~~~~~~~~~~~~~~~

Based on the feedback on the pull request, you might need to rework your
patch. Before re-submitting the patch, rebase with ``upstream/develop``, don't
merge; and force the push to the origin:

.. code-block:: bash

    $ git rebase -f upstream/develop
    $ git push --force origin BRANCH_NAME

.. note::

    When doing a ``push --force``, always specify the branch name explicitly
    to avoid messing other branches in the repo (``--force`` tells Git that
    you really want to mess with things so do it carefully).

Often, **mangos-zero** team members will ask you to "squash" your commits. This
means you will convert many commits to one commit. To do this, use the rebase
command:

.. code-block:: bash

    $ git rebase -i upstream/develop
    $ git push --force origin BRANCH_NAME

After you type this command, an editor will popup showing a list of commits:

.. code-block:: text

    pick 1a31be6 first commit
    pick 7fc64b4 second commit
    pick 7d33018 third commit

To squash all commits into the first one, remove the word ``pick`` before the
second and the last commits, and replace it by the word ``squash`` or just
``s``. When you save, Git will start rebasing, and if successful, will ask
you to edit the commit message, which by default is a listing of the commit
messages of all the commits. When you are finished, execute the push command.

.. _ProGit:                                http://git-scm.com/book
.. _BitBucket:                             http://bitbucket.org/account/signup/
.. _`mangos-zero repository`:              http://bitbucket.org/mangoszero/server
.. _`documentation repository`:            http://bitbucket.org/mangoszero/documentation
