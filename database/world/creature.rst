.. _db-world-creature:

================
"creature" table
================

The ``creature`` table holds spawns of ``creature_template`` entries.

Table structure
---------------

+-------------------+-------------------------+--------+-------+-----------+-------------------+
| Field             | Type                    | Null   | Key   | Default   | Extra             |
+===================+=========================+========+=======+===========+===================+
| guid              | int(10) unsigned        | NO     | PRI   | NULL      | auto\_increment   |
+-------------------+-------------------------+--------+-------+-----------+-------------------+
| id                | mediumint(8) unsigned   | NO     | MUL   | 0         |                   |
+-------------------+-------------------------+--------+-------+-----------+-------------------+
| map               | smallint(5) unsigned    | NO     | MUL   | 0         |                   |
+-------------------+-------------------------+--------+-------+-----------+-------------------+
| modelid           | mediumint(8) unsigned   | NO     |       | 0         |                   |
+-------------------+-------------------------+--------+-------+-----------+-------------------+
| equipment\_id     | mediumint(9)            | NO     |       | 0         |                   |
+-------------------+-------------------------+--------+-------+-----------+-------------------+
| position\_x       | float                   | NO     |       | 0         |                   |
+-------------------+-------------------------+--------+-------+-----------+-------------------+
| position\_y       | float                   | NO     |       | 0         |                   |
+-------------------+-------------------------+--------+-------+-----------+-------------------+
| position\_z       | float                   | NO     |       | 0         |                   |
+-------------------+-------------------------+--------+-------+-----------+-------------------+
| orientation       | float                   | NO     |       | 0         |                   |
+-------------------+-------------------------+--------+-------+-----------+-------------------+
| spawntimesecs     | int(10) unsigned        | NO     |       | 120       |                   |
+-------------------+-------------------------+--------+-------+-----------+-------------------+
| spawndist         | float                   | NO     |       | 5         |                   |
+-------------------+-------------------------+--------+-------+-----------+-------------------+
| currentwaypoint   | mediumint(8) unsigned   | NO     |       | 0         |                   |
+-------------------+-------------------------+--------+-------+-----------+-------------------+
| curhealth         | int(10) unsigned        | NO     |       | 1         |                   |
+-------------------+-------------------------+--------+-------+-----------+-------------------+
| curmana           | int(10) unsigned        | NO     |       | 0         |                   |
+-------------------+-------------------------+--------+-------+-----------+-------------------+
| DeathState        | tinyint(3) unsigned     | NO     |       | 0         |                   |
+-------------------+-------------------------+--------+-------+-----------+-------------------+
| MovementType      | tinyint(3) unsigned     | NO     |       | 0         |                   |
+-------------------+-------------------------+--------+-------+-----------+-------------------+

Fields
------

guid
----

The unique identifier of the creature spawn.

id
--

This references the `creature\_template <creature_template>`__ tables
unique ID for which the entry is valid.

map
---

A map identifier. The value has to match with a map identifier defined
in :doc:`../../file-formats/dbc/map`.

modelid
-------

A display model identifier. This references the
`creature\_model\_info <creature_model_info>`__ tables unique ID for
which this entry is valid.

equipment\_id
-------------

This references the
`creature\_equip\_template <creature_equip_template>`__ tables unique ID
for which the entry is valid.

position\_x
-----------

The X position for the creatures initial position.

position\_y
-----------

The Y position for the creatures initial position.

position\_z
-----------

The Z position for the creatures initial position.

orientation
-----------

The orientation for the creatures initial position.

spawntimesecs
-------------

The respawn time for the creature, defined in seconds till respawn.

spawndist
---------

The maximum distance that the creature should spawn from its spawn
point. If the creature is set to random movement, this defines a radius
in which the creature may move.

currentwaypoint
---------------

The current waypoint, on which the creature resides. If waypoints are
defined, this references the `creature\_movement <creature_movement>`__
tables ``point`` field for which the entry is valid.

curhealth
---------

The current health that the creature has.

curmana
-------

The current mana that the creature has.

DeathState
----------

Defines if the creature spawn is alive or dead.

+---------+---------+
| Value   | State   |
+=========+=========+
| 0       | Alive   |
+---------+---------+
| 1       | Dead    |
+---------+---------+

.. note::

    Dead creatures can not have gossip dialogues, unless you
    explicitly set the dynamic flag for corpses on the
    `creature\_template <creature_template>`__.

MovementType
------------

The movement type defines what a creature spawn will behave like after
spawning.

+---------+-----------------------------------------------+
| Value   | Behaviour                                     |
+=========+===============================================+
| 0       | Idle on spawn point                           |
+---------+-----------------------------------------------+
| 1       | Random movement within ``spawndist`` radius   |
+---------+-----------------------------------------------+
| 2       | Waypoint movement                             |
+---------+-----------------------------------------------+

