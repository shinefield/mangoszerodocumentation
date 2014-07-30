.. _db-world-game-graveyard-zone:

=============================
"game\_graveyard\_zone" table
=============================

The ``game_graveyard_zone`` table holds information on which graveyard a
dead character should appear, depending on where he dies and what
faction he belongs to.

Table structure
---------------

+---------------+-------------------------+--------+-------+-----------+---------+
| Field         | Type                    | Null   | Key   | Default   | Extra   |
+===============+=========================+========+=======+===========+=========+
| id            | mediumint(8) unsigned   | NO     | PRI   | 0         |         |
+---------------+-------------------------+--------+-------+-----------+---------+
| ghost\_zone   | mediumint(8) unsigned   | NO     | PRI   | 0         |         |
+---------------+-------------------------+--------+-------+-----------+---------+
| faction       | smallint(5) unsigned    | NO     |       | 0         |         |
+---------------+-------------------------+--------+-------+-----------+---------+

Fields
------

id
--

A graveyard identifier. The value has to match with a location
identifier defined in `WorldSafeLocs.dbc <../dbc/WorldSafeLocs.dbc>`__.

ghost\_zone
-----------

A zone identifier. The value has to match with a zone identifier defined
in `AreaTable.dbc <../dbc/AreaTable.dbc>`__.

faction
-------

The faction for which this graveyard should be used. This references a
faction entry from the `Faction.dbc <../dbc/Faction.dbc>`__ table.

+---------+-----------------+
| Value   | Faction         |
+=========+=================+
| 0       | Any faction     |
+---------+-----------------+
| 67      | Horde only      |
+---------+-----------------+
| 469     | Alliance only   |
+---------+-----------------+

