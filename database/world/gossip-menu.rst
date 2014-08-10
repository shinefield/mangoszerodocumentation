.. _db-world-gossip-menu:

====================
"gossip\_menu" table
====================

The ``gossip_menu`` table holds information on gossip menus assigned to
either a creature or an game object.

Table structure
---------------

+-----------------+-------------------------+--------+-------+-----------+---------+
| Field           | Type                    | Null   | Key   | Default   | Extra   |
+=================+=========================+========+=======+===========+=========+
| entry           | smallint(6) unsigned    | NO     | PRI   | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| text\_id        | mediumint(8) unsigned   | NO     | PRI   | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| script\_id      | mediumint(8) unsigned   | NO     | PRI   | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| condition\_id   | mediumint(8) unsigned   | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+

Fields
------

entry
-----

The unique identifier for the gossip menu entry. This may be referenced
by either the :doc:`creature-template` table's
``gossip_menu_id`` field, or by
:doc:`gameobject-template` tables ``data3`` field
for all game objects which are quest givers.

text\_id
--------

This references the :doc:`npc-text` tables unique ID for which
the entry is valid.

script\_id
----------

This references the :doc:`dbscripts-on-gossip`
tables unique ID for which the entry is valid.

condition\_id
-------------

This references the :doc:`conditions` tables unique ID for
which the entry is valid.
