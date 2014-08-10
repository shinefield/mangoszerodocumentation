.. _db-world-playercreateinfo-spell:

===============================
"playercreateinfo\_spell" table
===============================

The ``playercreateinfo_spell`` table holds information on what spells
newly created characters should start out with. A character in this
table is defined by his/her race and class combination.

Table structure
---------------

+---------+-------------------------+--------+-------+-----------+---------+
| Field   | Type                    | Null   | Key   | Default   | Extra   |
+=========+=========================+========+=======+===========+=========+
| race    | tinyint(3) unsigned     | NO     | PRI   | 0         |         |
+---------+-------------------------+--------+-------+-----------+---------+
| class   | tinyint(3) unsigned     | NO     | PRI   | 0         |         |
+---------+-------------------------+--------+-------+-----------+---------+
| Spell   | mediumint(8) unsigned   | NO     | PRI   | 0         |         |
+---------+-------------------------+--------+-------+-----------+---------+
| Note    | varchar(255)            | YES    |       | NULL      |         |
+---------+-------------------------+--------+-------+-----------+---------+

Fields
------

race
----

A bit-mask corresponding to races that should get the spell. The value
has to match with races defined in :doc:`../../file-formats/dbc/chrraces`.

class
-----

A bit-mask corresponding to class that should get the spell. The value
has to match with classes defined in :doc:`../../file-formats/dbc/chrclasses`.

Spell
-----

The spell identifier. The value has to match with a spell identifier
defined in :doc:`../../file-formats/dbc/spell`.

Note
----

A note explaining what the spell is. This is only for reference
purposes.
