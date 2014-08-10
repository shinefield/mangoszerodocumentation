.. _db-world-spell-pet-auras:

=========================
"spell\_pet\_auras" table
=========================

The ``spell_pet_auras`` table holds information for connecting pet
creatures to spells and auras.

Table structure
---------------

+---------+-------------------------+--------+-------+-----------+---------+
| Field   | Type                    | Null   | Key   | Default   | Extra   |
+=========+=========================+========+=======+===========+=========+
| spell   | mediumint(8) unsigned   | NO     | PRI   | NULL      |         |
+---------+-------------------------+--------+-------+-----------+---------+
| pet     | mediumint(8) unsigned   | NO     | PRI   | 0         |         |
+---------+-------------------------+--------+-------+-----------+---------+
| aura    | mediumint(8) unsigned   | NO     |       | NULL      |         |
+---------+-------------------------+--------+-------+-----------+---------+

Fields
------

spell
-----

The spell identifier. The value has to match with a spell identifier
defined in :doc:`../../file-formats/dbc/spell`.

pet
---

This references the `creature\_template <creature_template>`__ tables
unique ID for the pet.

aura
----

An aura identifier. The value has to match with a spell identifier
defined in :doc:`../../file-formats/dbc/spell`.
