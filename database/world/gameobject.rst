.. _db-world-gameobject:

==================
"gameobject" table
==================

The ``gameobject`` table holds spawns of ``gameobject_template``
entries.

Table structure
---------------

+-----------------+-------------------------+--------+-------+-----------+-------------------+
| Field           | Type                    | Null   | Key   | Default   | Extra             |
+=================+=========================+========+=======+===========+===================+
| guid            | int(10) unsigned        | NO     | PRI   | NULL      | auto\_increment   |
+-----------------+-------------------------+--------+-------+-----------+-------------------+
| id              | mediumint(8) unsigned   | NO     | MUL   | 0         |                   |
+-----------------+-------------------------+--------+-------+-----------+-------------------+
| map             | smallint(5) unsigned    | NO     | MUL   | 0         |                   |
+-----------------+-------------------------+--------+-------+-----------+-------------------+
| position\_x     | float                   | NO     |       | 0         |                   |
+-----------------+-------------------------+--------+-------+-----------+-------------------+
| position\_y     | float                   | NO     |       | 0         |                   |
+-----------------+-------------------------+--------+-------+-----------+-------------------+
| position\_z     | float                   | NO     |       | 0         |                   |
+-----------------+-------------------------+--------+-------+-----------+-------------------+
| orientation     | float                   | NO     |       | 0         |                   |
+-----------------+-------------------------+--------+-------+-----------+-------------------+
| rotation0       | float                   | NO     |       | 0         |                   |
+-----------------+-------------------------+--------+-------+-----------+-------------------+
| rotation1       | float                   | NO     |       | 0         |                   |
+-----------------+-------------------------+--------+-------+-----------+-------------------+
| rotation2       | float                   | NO     |       | 0         |                   |
+-----------------+-------------------------+--------+-------+-----------+-------------------+
| rotation3       | float                   | NO     |       | 0         |                   |
+-----------------+-------------------------+--------+-------+-----------+-------------------+
| spawntimesecs   | int(11)                 | NO     |       | 0         |                   |
+-----------------+-------------------------+--------+-------+-----------+-------------------+
| animprogress    | tinyint(3) unsigned     | NO     |       | 0         |                   |
+-----------------+-------------------------+--------+-------+-----------+-------------------+
| state           | tinyint(3) unsigned     | NO     |       | 0         |                   |
+-----------------+-------------------------+--------+-------+-----------+-------------------+

Fields
------

guid
----

The unique identifier of the game object spawn.

id
--

This references the :doc:`gameobject-template`
tables unique ID for which the entry is valid.

map
---

A map identifier. The value has to match with a map identifier defined
in :doc:`../../file-formats/dbc/map`.

position\_x
-----------

The X position for the game objects initial position.

position\_y
-----------

The Y position for the game objects initial position.

position\_z
-----------

The Z position for the game objects initial position.

orientation
-----------

The orientation for the game objects initial position.

rotation0
---------

**TODO**

rotation1
---------

**TODO**

rotation2
---------

**TODO**

rotation3
---------

**TODO**

spawntimesecs
-------------

The respawn time for the game object, defined in seconds till respawn.

.. note::

    Using a negative spawn time will lead to the object being
    despawned until spawned by a script. It will then *despawn* after the
    time specified here.

animprogress
------------

**TODO**

.. note::

    Set to ``100`` for game objects of type chest.

state
-----

This field is only used for game objects which are doors, or chests, and
will signal their initial state.

-  if set to ``0``, the door/chest is opened,
-  if set to ``1``, the door/chest is closed.

