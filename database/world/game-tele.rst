.. _db-world-game-tele:

==================
"game\_tele" table
==================

The ``game_tele`` table holds lists of teleport locations identified by
unique names.

*Notice*: teleport locations are merely an addition to ease the life of
game masters and developers, allowing to quickly travel to a location
instead of having to lookup the coordinates.

Table structure
---------------

+---------------+-------------------------+--------+-------+-----------+-------------------+
| Field         | Type                    | Null   | Key   | Default   | Extra             |
+===============+=========================+========+=======+===========+===================+
| id            | mediumint(8) unsigned   | NO     | PRI   | NULL      | auto\_increment   |
+---------------+-------------------------+--------+-------+-----------+-------------------+
| position\_x   | float                   | NO     |       | 0         |                   |
+---------------+-------------------------+--------+-------+-----------+-------------------+
| position\_y   | float                   | NO     |       | 0         |                   |
+---------------+-------------------------+--------+-------+-----------+-------------------+
| position\_z   | float                   | NO     |       | 0         |                   |
+---------------+-------------------------+--------+-------+-----------+-------------------+
| orientation   | float                   | NO     |       | 0         |                   |
+---------------+-------------------------+--------+-------+-----------+-------------------+
| map           | smallint(5) unsigned    | NO     |       | 0         |                   |
+---------------+-------------------------+--------+-------+-----------+-------------------+
| name          | varchar(100)            | NO     |       |           |                   |
+---------------+-------------------------+--------+-------+-----------+-------------------+

Fields
------

id
--

A unique identifier for the teleport location.

position\_x
-----------

The X coordinate for the teleport location.

position\_y
-----------

The Y coordinate for the teleport location.

position\_z
-----------

The Z coordinate for the teleport location.

orientation
-----------

The orientation for the teleport location.

map
---

A map identifier. The value has to match with a map identifier defined
in `Map.dbc <../dbc/Map.dbc>`__.

name
----

A unique name for the teleport location.

*Notice*: using spaces and special characters for locations is
prohibited.
