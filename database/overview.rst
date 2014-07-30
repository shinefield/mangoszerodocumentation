********
Overview
********

This documentation is part of an effort to recreate the original `World of Warcraft`_
content from scratch while making sure each bit of content is valid for
version 1.12.x; compatibility with the **mangos-zero** `server`_, and our
`scripts`_ is ensured.


Development process
-------------------

In order to develop a `database`_ which everyone can enjoy, we have defined a few
processes and rules for contributing to our project. If you intend to submit pull
requests and/or patches, please familiarize yourself with these rules prior to
submitting your contributions.

* :ref:`db-contributing-content-research`
* :ref:`db-contributing-content-updates`
* :ref:`db-contributing-style-guide`

Database structure
------------------

This includes the structure for the character, realm list, world and
script library databases.

* :ref:`db-realm-index`: the authentication and realm list server, where you
  configure users, available world servers, and also can ban abusive users,
  and IP addresses.
* :ref:`db-world-index`: the world server's content source. This is where
  creatures, objects, quests, items, etc. are defined.
* :ref:`db-character-index`: the place where a player's data for all characters
  are stored.
* :ref:`db-script-index`: the storage space the the script library. Holds texts,
  dialogues and waypoints for any scripted action.

.. _World of Warcraft:  http://blizzard.com/games/wow/

.. _mangos-zero:        http://bitbucket.org/mangoszero
.. _server:             http://bitbucket.org/mangoszero/server
.. _scripts:            http://bitbucket.org/mangoszero/scripts
.. _database:           http://bitbucket.org/mangoszero/content
