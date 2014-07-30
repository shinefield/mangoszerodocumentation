.. _db-world-spell-script-target:

=============================
"spell\_script\_target" table
=============================

The ``spell_script_target`` table defines which targets are allowed for
spells having an ImplicitTarget[A,B] of 7, 8, 38, 40, 46, 52.

Targets can be game objects, or creatures (both alive and dead.)

Table structure
---------------

+---------------------+-------------------------+--------+-------+-----------+---------+
| Field               | Type                    | Null   | Key   | Default   | Extra   |
+=====================+=========================+========+=======+===========+=========+
| entry               | mediumint(8) unsigned   | NO     | PRI   | NULL      |         |
+---------------------+-------------------------+--------+-------+-----------+---------+
| type                | tinyint(3) unsigned     | NO     | PRI   | 0         |         |
+---------------------+-------------------------+--------+-------+-----------+---------+
| targetEntry         | mediumint(8) unsigned   | NO     | PRI   | 0         |         |
+---------------------+-------------------------+--------+-------+-----------+---------+
| inverseEffectMask   | mediumint(8) unsigned   | NO     |       | 0         |         |
+---------------------+-------------------------+--------+-------+-----------+---------+

Fields
------

entry
-----

The spell identifier. The value has to match with a spell identifier
defined in `Spell.dbc <../dbc/Spell.dbc>`__.

type
----

Describes which type of target the spell requires. The following table
shows all valid target types.

+---------+--------------------------+
| Value   | Description              |
+=========+==========================+
| 0       | Game object              |
+---------+--------------------------+
| 1       | Creature template        |
+---------+--------------------------+
| 2       | Dead creature template   |
+---------+--------------------------+

targetEntry
-----------

Depending on the ``type`` value this references the
`creature\_template <creature_template>`__ tables unique ID, or the
`gameobject\_template <gameobject_template>`__ tables unique ID.

inverseEffectMask
-----------------

**TODO**: takes a value for an effect, and shifts it.
