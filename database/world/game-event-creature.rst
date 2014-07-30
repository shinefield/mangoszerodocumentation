.. _db-world-game-event-creature:

=============================
"game\_event\_creature" table
=============================

The ``game_event_creature`` table holds lists of ``creature`` entries to
be spawned during game events.

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

This references the `creature <creature>`__ tables unique ID for which
the entry is valid.

event
-----

This references the `game\_event <game_event>`__ tables unique ID for
which the entry is valid.
