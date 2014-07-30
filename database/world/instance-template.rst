.. _db-world-instance-template:

==========================
"instance\_template" table
==========================

The ``instance_template`` table holds definitions for the basic
parameters of any instance.

Each time a new group opens an instance, an instance is opened using
these.

Table structure
---------------

+--------------------+------------------------+--------+-------+-----------+---------+
| Field              | Type                   | Null   | Key   | Default   | Extra   |
+====================+========================+========+=======+===========+=========+
| map                | smallint(5) unsigned   | NO     | PRI   | NULL      |         |
+--------------------+------------------------+--------+-------+-----------+---------+
| parent             | smallint(5) unsigned   | NO     |       | 0         |         |
+--------------------+------------------------+--------+-------+-----------+---------+
| levelMin           | tinyint(3) unsigned    | NO     |       | 0         |         |
+--------------------+------------------------+--------+-------+-----------+---------+
| levelMax           | tinyint(3) unsigned    | NO     |       | 0         |         |
+--------------------+------------------------+--------+-------+-----------+---------+
| maxPlayers         | tinyint(3) unsigned    | NO     |       | 0         |         |
+--------------------+------------------------+--------+-------+-----------+---------+
| reset\_delay       | int(10) unsigned       | NO     |       | 0         |         |
+--------------------+------------------------+--------+-------+-----------+---------+
| ghostEntranceMap   | smallint(5) unsigned   | NO     |       | NULL      |         |
+--------------------+------------------------+--------+-------+-----------+---------+
| ghostEntranceX     | float                  | NO     |       | NULL      |         |
+--------------------+------------------------+--------+-------+-----------+---------+
| ghostEntranceY     | float                  | NO     |       | NULL      |         |
+--------------------+------------------------+--------+-------+-----------+---------+
| ScriptName         | varchar(128)           | NO     |       |           |         |
+--------------------+------------------------+--------+-------+-----------+---------+

Fields
------

map
---

A map identifier. The value has to match with a map identifier defined
in `Map.dbc <../dbc/Map.dbc>`__.

parent
------

If the instance is part of another instance, this holds its parent map.
The value has to match with a map identifier defined in
`Map.dbc <../dbc/Map.dbc>`__.

levelMin
--------

The lowest allowed level required to enter the instance.

levelMax
--------

The highest allowed level able to search for groups using meeting stones
for the instance.

maxPlayers
----------

The maximum amount of players allowed to enter as group or raid.

reset\_delay
------------

The number of days between each global reset for the instance map. If
zero, the value is taken from DBC files.

The resulting value is multiplied by the Rate.InstanceResetTime
configuration.

ghostEntranceMap
----------------

The continent on which ghosts will be spawned. This references the
``mapID`` column in the
`WorldMapContinent.dbc <../dbc/WorldMapContinent.dbc>`__ table.

ghostEntranceX
--------------

**TODO**

ghostEntranceY
--------------

**TODO**

ScriptName
----------

To assign a script from the script library to the instance\_template,
set this string to the script's exported name.
