.. _db-world-world-template:

=======================
"world\_template" table
=======================

The ``world_template`` table holds informations for connection world
continents to scripts from the script library.

Table structure
---------------

+--------------+------------------------+--------+-------+-----------+---------+
| Field        | Type                   | Null   | Key   | Default   | Extra   |
+==============+========================+========+=======+===========+=========+
| map          | smallint(5) unsigned   | NO     | PRI   | NULL      |         |
+--------------+------------------------+--------+-------+-----------+---------+
| ScriptName   | varchar(128)           | NO     |       |           |         |
+--------------+------------------------+--------+-------+-----------+---------+

Fields
------

map
---

A world continent identifier. The value has to match with a continent
identifier defined in :doc:`../../file-formats/dbc/worldmapcontinent`,
and references the ``mapID`` field in that file.

ScriptName
----------

To assign a script from the script library to the world continent, set
this string to the script's exported name.
