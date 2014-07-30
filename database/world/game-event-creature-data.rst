.. _db-world-game-event-creature-data:

===================================
"game\_event\_creature\_data" table
===================================

The ``game_event_creature_data`` table holds modifiers for ``creature``
entries spawned during a ``game_event``.

Table structure
---------------

+-----------------+-------------------------+--------+-------+-----------+---------+
| Field           | Type                    | Null   | Key   | Default   | Extra   |
+=================+=========================+========+=======+===========+=========+
| guid            | int(10) unsigned        | NO     | PRI   | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| entry\_id       | mediumint(8) unsigned   | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| modelid         | mediumint(8) unsigned   | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| equipment\_id   | mediumint(8) unsigned   | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| spell\_start    | mediumint(8) unsigned   | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| spell\_end      | mediumint(8) unsigned   | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| event           | smallint(5) unsigned    | NO     | PRI   | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+

Fields
------

guid
----

This references the `creature <creature>`__ tables unique ID for which
the entry is valid.

entry\_id
---------

**TODO**

modelid
-------

A display model identifier. This references the
`creature\_model\_info <creature_model_info>`__ tables unique ID for
which this entry is valid.

*Notice*: set to ``0`` if only the equipment should be changed.

equipment\_id
-------------

This references the
`creature\_equip\_template <creature_equip_template>`__ tables unique ID
for which the entry is valid.

*Notice*: set to ``0`` if only the model should be changed.

spell\_start
------------

If set to a valid spell identifier from
`Spell.dbc <../dbc/Spell.dbc>`__, this will cause the create to cast the
spell upon applying the modifications.

spell\_end
----------

If set to a valid spell identifier from
`Spell.dbc <../dbc/Spell.dbc>`__, this will cause the create to cast the
spell upon removing the modifications.

event
-----

This references the `game\_event <game_event>`__ tables unique ID for
which the entry is valid.
