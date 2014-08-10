.. _db-world-creature-ai-summons:

=============================
"creature\_ai\_summons" table
=============================

The ``creature_ai_summons`` table holds information supporting summons
executed by creatures through AI scripts.

Table structure
---------------

+-----------------+--------------------+--------+-------+-----------+-------------------+
| Field           | Type               | Null   | Key   | Default   | Extra             |
+=================+====================+========+=======+===========+===================+
| id              | int(11) unsigned   | NO     | PRI   | NULL      | auto\_increment   |
+-----------------+--------------------+--------+-------+-----------+-------------------+
| position\_x     | float              | NO     |       | 0         |                   |
+-----------------+--------------------+--------+-------+-----------+-------------------+
| position\_y     | float              | NO     |       | 0         |                   |
+-----------------+--------------------+--------+-------+-----------+-------------------+
| position\_z     | float              | NO     |       | 0         |                   |
+-----------------+--------------------+--------+-------+-----------+-------------------+
| orientation     | float              | NO     |       | 0         |                   |
+-----------------+--------------------+--------+-------+-----------+-------------------+
| spawntimesecs   | int(11) unsigned   | NO     |       | 120       |                   |
+-----------------+--------------------+--------+-------+-----------+-------------------+
| comment         | varchar(255)       | NO     |       |           |                   |
+-----------------+--------------------+--------+-------+-----------+-------------------+

Fields
------

id
--

This references the third action parameter in the :doc:`creature-ai-scripts`
tables entry with a summon action assigned.

position\_x
-----------

The X position for the creature to be spawn.

position\_y
-----------

The Y position for the creature to be spawn.

position\_z
-----------

The Z position for the creature to be spawn.

orientation
-----------

The orientation for the creature to be spawn.

spawntimesecs
-------------

The despawn timer for the summoned creature.

comment
-------

Documents what kind of creature will be summoned. Currently it is common
to use the summoned creature's
:doc:`creature-template` ``entry`` value to describe
what is summoned.
