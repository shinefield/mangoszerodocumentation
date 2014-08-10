.. _db-world-petcreateinfo-spell:

============================
"petcreateinfo\_spell" table
============================

The ``petcreateinfo_spell`` table holds spells which are assigned to
tameable creatures.

Table structure
---------------

+----------+-------------------------+--------+-------+-----------+---------+
| Field    | Type                    | Null   | Key   | Default   | Extra   |
+==========+=========================+========+=======+===========+=========+
| entry    | mediumint(8) unsigned   | NO     | PRI   | 0         |         |
+----------+-------------------------+--------+-------+-----------+---------+
| Spell1   | mediumint(8) unsigned   | NO     |       | 0         |         |
+----------+-------------------------+--------+-------+-----------+---------+
| Spell2   | mediumint(8) unsigned   | NO     |       | 0         |         |
+----------+-------------------------+--------+-------+-----------+---------+
| Spell3   | mediumint(8) unsigned   | NO     |       | 0         |         |
+----------+-------------------------+--------+-------+-----------+---------+
| Spell4   | mediumint(8) unsigned   | NO     |       | 0         |         |
+----------+-------------------------+--------+-------+-----------+---------+

Fields
------

entry
-----

This references the :doc:`creature-template` tables
unique ID for which the entry is valid.

Spell1
------

The spell identifier. The value has to match with a spell identifier
defined in :doc:`../../file-formats/dbc/spell`.

Spell2
------

The spell identifier. The value has to match with a spell identifier
defined in :doc:`../../file-formats/dbc/spell`.

Spell3
------

The spell identifier. The value has to match with a spell identifier
defined in :doc:`../../file-formats/dbc/spell`.

Spell4
------

The spell identifier. The value has to match with a spell identifier
defined in :doc:`../../file-formats/dbc/spell`.
