.. _db-world-game-event-quest:

==========================
"game\_event\_quest" table
==========================

The ``game_event_quest`` table holds definitions for quests which should
only be available during an active game event.

Table structure
---------------

+---------+-------------------------+--------+-------+-----------+---------+
| Field   | Type                    | Null   | Key   | Default   | Extra   |
+=========+=========================+========+=======+===========+=========+
| quest   | mediumint(8) unsigned   | NO     | PRI   | 0         |         |
+---------+-------------------------+--------+-------+-----------+---------+
| event   | smallint(5) unsigned    | NO     | PRI   | 0         |         |
+---------+-------------------------+--------+-------+-----------+---------+

Fields
------

quest
-----

This references the :doc:`quest-template` tables entry
which should be restricted to the referenced game event.

event
-----

This references the :doc:`game-event` tables unique ID for
which the entry is valid.
