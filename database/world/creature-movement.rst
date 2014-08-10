.. _db-world-creature-movement:

==========================
"creature\_movement" table
==========================

The ``creature_movement`` table holds informations on paths for spawned
``creature`` entries and allows to define behaviour along the movement
path.

.. note::

    Movement definitions here will overwrite any movement defined
    for the creature template.

Table structure
---------------

+---------------+-------------------------+--------+-------+-----------+---------+
| Field         | Type                    | Null   | Key   | Default   | Extra   |
+===============+=========================+========+=======+===========+=========+
| id            | int(10) unsigned        | NO     | PRI   | NULL      |         |
+---------------+-------------------------+--------+-------+-----------+---------+
| point         | mediumint(8) unsigned   | NO     | PRI   | 0         |         |
+---------------+-------------------------+--------+-------+-----------+---------+
| position\_x   | float                   | NO     |       | 0         |         |
+---------------+-------------------------+--------+-------+-----------+---------+
| position\_y   | float                   | NO     |       | 0         |         |
+---------------+-------------------------+--------+-------+-----------+---------+
| position\_z   | float                   | NO     |       | 0         |         |
+---------------+-------------------------+--------+-------+-----------+---------+
| waittime      | int(10) unsigned        | NO     |       | 0         |         |
+---------------+-------------------------+--------+-------+-----------+---------+
| script\_id    | mediumint(8) unsigned   | NO     |       | 0         |         |
+---------------+-------------------------+--------+-------+-----------+---------+
| textid1       | int(11)                 | NO     |       | 0         |         |
+---------------+-------------------------+--------+-------+-----------+---------+
| textid2       | int(11)                 | NO     |       | 0         |         |
+---------------+-------------------------+--------+-------+-----------+---------+
| textid3       | int(11)                 | NO     |       | 0         |         |
+---------------+-------------------------+--------+-------+-----------+---------+
| textid4       | int(11)                 | NO     |       | 0         |         |
+---------------+-------------------------+--------+-------+-----------+---------+
| textid5       | int(11)                 | NO     |       | 0         |         |
+---------------+-------------------------+--------+-------+-----------+---------+
| emote         | mediumint(8) unsigned   | NO     |       | 0         |         |
+---------------+-------------------------+--------+-------+-----------+---------+
| spell         | mediumint(8) unsigned   | NO     |       | 0         |         |
+---------------+-------------------------+--------+-------+-----------+---------+
| wpguid        | int(11)                 | NO     |       | 0         |         |
+---------------+-------------------------+--------+-------+-----------+---------+
| orientation   | float                   | NO     |       | 0         |         |
+---------------+-------------------------+--------+-------+-----------+---------+
| model1        | mediumint(9)            | NO     |       | 0         |         |
+---------------+-------------------------+--------+-------+-----------+---------+
| model2        | mediumint(9)            | NO     |       | 0         |         |
+---------------+-------------------------+--------+-------+-----------+---------+

Fields
------

id
--

This references the :doc:`creature` tables unique ID for which the entry is valid.

point
-----

An index count for all movement points attached to a creature spawn.
Starts with ``1`` and increments by one.

position\_x
-----------

The X position for the creature's movement point.

position\_y
-----------

The Y position for the creature's movement point.

position\_z
-----------

The Z position for the creature's movement point.

waittime
--------

If the creature should wait at the movement point, set this to the time
in milliseconds. Otherwise set to zero for the creature to immediately
proceed to the next movement point.

script\_id
----------

If a script should be executed, this references the
:doc:`dbscripts-on-creature-movement` tables unique ID for which the entry
is valid. If not, set the value to zero.

textid1
-------

If a text should be emoted, this references the
:doc:`db-script-string` tables unique ID for which the
entry is valid. If not, set the value to zero.

textid2
-------

If a text should be emoted, this references the
:doc:`db-script-string` tables unique ID for which the
entry is valid. If not, set the value to zero.

textid3
-------

If a text should be emoted, this references the
:doc:`db-script-string` tables unique ID for which the
entry is valid. If not, set the value to zero.

textid4
-------

If a text should be emoted, this references the
:doc:`db-script-string` tables unique ID for which the
entry is valid. If not, set the value to zero.

textid5
-------

If a text should be emoted, this references the
:doc:`db-script-string` tables unique ID for which the
entry is valid. If not, set the value to zero.

emote
-----

An emote identifier. The value has to match with an emote identifier
defined in :doc:`../../file-formats/dbc/emotes`.

spell
-----

The spell identifier. The value has to match with a spell identifier
defined in :doc:`../../file-formats/dbc/spell`. This refers to a spell
which should be cast on this waypoint.

wpguid
------

A unique identifier for this waypoint.

orientation
-----------

The orientation for the creature's movement point. Measured in radians,
where ``0`` is north on the mini-map and ``pi`` is south on the
mini-map.

model1
------

A display model identifier activated on the waypoint. This references
the :doc:`creature-model-info` tables unique ID for which this entry is
valid.

model2
------

An alternative display model identifier activated on the waypoint. This
references the :doc:`creature-model-info` tables unique ID for which this
entry is valid.
