.. _db-world-npc-trainer-template:

==============================
"npc\_trainer\_template" table
==============================

The ``npc_trainer_template`` table holds holds spell lists usable for
multiple training creatures.

Table structure
---------------

+-----------------+-------------------------+--------+-------+-----------+---------+
| Field           | Type                    | Null   | Key   | Default   | Extra   |
+=================+=========================+========+=======+===========+=========+
| entry           | mediumint(8) unsigned   | NO     | PRI   | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| spell           | mediumint(8) unsigned   | NO     | PRI   | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| spellcost       | int(10) unsigned        | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| reqskill        | smallint(5) unsigned    | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| reqskillvalue   | smallint(5) unsigned    | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| reqlevel        | tinyint(3) unsigned     | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+

Fields
------

entry
-----

The unique identifier for the training template. A
`creature\_template <creature_template>`__ references this from its
``trainer_id`` column.

spell
-----

The spell identifier. The value has to match with a spell identifier
defined in :doc:`../../file-formats/dbc/spell`. This has to be a spell
which teaches the actual spell.

spellcost
---------

The cost that the player needs to pay in order to learn the spell in
copper.

reqskill
--------

The required skill to be able to learn the spell. This references the
skill's entry in the :doc:`../../file-formats/dbc/skillline` table.

reqskillvalue
-------------

The minimum skill level required for the skill referenced in
``reqskill``.

reqlevel
--------

The character level required in order to learn the spell.
