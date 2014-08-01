.. _db-world-game-event:

===================
"game\_event" table
===================

The ``game_event`` table holds definitions for in-game events, both
holiday related and normal events.

.. note::

    game events are not necessarily events related to events
    introduced by patches (e.g. The Ahn'Qiraj opening). Game events include
    things such as the Stockades riots, or the Pyrewood Village event for
    the Worgen curse.

Table structure
---------------

+---------------+-------------------------+--------+-------+-----------------------+---------+
| Field         | Type                    | Null   | Key   | Default               | Extra   |
+===============+=========================+========+=======+=======================+=========+
| entry         | mediumint(8) unsigned   | NO     | PRI   | NULL                  |         |
+---------------+-------------------------+--------+-------+-----------------------+---------+
| start\_time   | timestamp               | NO     |       | 0000-00-00 00:00:00   |         |
+---------------+-------------------------+--------+-------+-----------------------+---------+
| end\_time     | timestamp               | NO     |       | 0000-00-00 00:00:00   |         |
+---------------+-------------------------+--------+-------+-----------------------+---------+
| occurence     | bigint(20) unsigned     | NO     |       | 86400                 |         |
+---------------+-------------------------+--------+-------+-----------------------+---------+
| length        | bigint(20) unsigned     | NO     |       | 43200                 |         |
+---------------+-------------------------+--------+-------+-----------------------+---------+
| holiday       | mediumint(8) unsigned   | NO     |       | 0                     |         |
+---------------+-------------------------+--------+-------+-----------------------+---------+
| description   | varchar(255)            | YES    |       | NULL                  |         |
+---------------+-------------------------+--------+-------+-----------------------+---------+

Fields
------

entry
-----

The unique identifier for the game event.

start\_time
-----------

A timestamp for the start date and time of the event. Try to keep start
time related to the official World of Warcraft release on November 23rd
2004.

end\_time
---------

A timestamp for the end date and time of the event. Try to keep start
time related to the official World of Warcraft release on November 23rd
2004.

occurence
---------

Defines the time span between occurrences of the game event. The time
span is measured in minutes.

-  1440 minutes for a day,
-  2880 minutes for two days,
-  etc.

length
------

Defines the length of an event. The time is measured in minutes, and
**needs** to be lower than the value set for ``occurence``.

.. note::

    if ``length`` is > ``occurence``, an event would never stop.

holiday
-------

If an event is related to an official in-game world event such as Winter
Veil, etc. this contains the unique identifier as known by the game
client.

description
-----------

Describe the game event. If possible specify name, location, and
schedule in the comment.
