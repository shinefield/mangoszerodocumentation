.. _db-world-spell-target-position:

===============================
"spell\_target\_position" table
===============================

The ``spell_target_position`` table holds coordinate information on
where a character should be teleported to when a spell with effect
SPELL\_EFFECT\_TELEPORT\_UNITS is cast.

Table structure
---------------

+-----------------------+-------------------------+--------+-------+-----------+---------+
| Field                 | Type                    | Null   | Key   | Default   | Extra   |
+=======================+=========================+========+=======+===========+=========+
| id                    | mediumint(8) unsigned   | NO     | PRI   | 0         |         |
+-----------------------+-------------------------+--------+-------+-----------+---------+
| target\_map           | smallint(5) unsigned    | NO     |       | 0         |         |
+-----------------------+-------------------------+--------+-------+-----------+---------+
| target\_position\_x   | float                   | NO     |       | 0         |         |
+-----------------------+-------------------------+--------+-------+-----------+---------+
| target\_position\_y   | float                   | NO     |       | 0         |         |
+-----------------------+-------------------------+--------+-------+-----------+---------+
| target\_position\_z   | float                   | NO     |       | 0         |         |
+-----------------------+-------------------------+--------+-------+-----------+---------+
| target\_orientation   | float                   | NO     |       | 0         |         |
+-----------------------+-------------------------+--------+-------+-----------+---------+

Fields
------

id
--

The spell identifier. The value has to match with a spell identifier
defined in `Spell.dbc <../dbc/Spell.dbc>`__.

target\_map
-----------

The target map's identifier. The value has to match with a map
identifier defined in `Map.dbc <../dbc/Map.dbc>`__.

target\_position\_x
-------------------

The X position on the target map.

target\_position\_y
-------------------

The Y position on the target map.

target\_position\_z
-------------------

The Z position on the target map.

target\_orientation
-------------------

The orientation for the character on the target map. This is measured in
radians, ``0`` is north on the mini-map and ``pi`` is south on the
mini-map etc.
