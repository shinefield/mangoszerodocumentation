.. _db-world-game-event-gameobject:

===============================
"game\_event\_gameobject" table
===============================

The ``game_event_gameobject`` table holds lists of ``gameobject``
entries to be spawned during game events.

Table structure
---------------

+---------+--------------------+--------+-------+-----------+---------+
| Field   | Type               | Null   | Key   | Default   | Extra   |
+=========+====================+========+=======+===========+=========+
| guid    | int(10) unsigned   | NO     | PRI   | NULL      |         |
+---------+--------------------+--------+-------+-----------+---------+
| event   | smallint(6)        | NO     |       | 0         |         |
+---------+--------------------+--------+-------+-----------+---------+

Fields
------

guid
----

This references the `gameobject <gameobject>`__ tables unique ID for
which the entry is valid.

event
-----

This references the `game\_event <game_event>`__ tables unique ID for
which the entry is valid.
