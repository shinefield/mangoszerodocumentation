.. _db-world-playercreateinfo:

========================
"playercreateinfo" table
========================

The ``playercreateinfo`` table holds the start positions of each
class/race combinations for newly created characters.

Table structure
---------------

+---------------+-------------------------+--------+-------+-----------+---------+
| Field         | Type                    | Null   | Key   | Default   | Extra   |
+===============+=========================+========+=======+===========+=========+
| race          | tinyint(3) unsigned     | NO     | PRI   | 0         |         |
+---------------+-------------------------+--------+-------+-----------+---------+
| class         | tinyint(3) unsigned     | NO     | PRI   | 0         |         |
+---------------+-------------------------+--------+-------+-----------+---------+
| map           | smallint(5) unsigned    | NO     |       | 0         |         |
+---------------+-------------------------+--------+-------+-----------+---------+
| zone          | mediumint(8) unsigned   | NO     |       | 0         |         |
+---------------+-------------------------+--------+-------+-----------+---------+
| position\_x   | float                   | NO     |       | 0         |         |
+---------------+-------------------------+--------+-------+-----------+---------+
| position\_y   | float                   | NO     |       | 0         |         |
+---------------+-------------------------+--------+-------+-----------+---------+
| position\_z   | float                   | NO     |       | 0         |         |
+---------------+-------------------------+--------+-------+-----------+---------+
| orientation   | float                   | NO     |       | 0         |         |
+---------------+-------------------------+--------+-------+-----------+---------+

Fields
------

race
----

A bit-mask corresponding to races that should get the spell. The value
has to match with races defined in :doc:`../../file-formats/dbc/chrraces`.

class
-----

A bit-mask corresponding to class that should get the spell. The value
has to match with classes defined in
:doc:`../../file-formats/dbc/chrclasses`.

map
---

A map identifier. The value has to match with a map identifier defined
in :doc:`../../file-formats/dbc/map`.

zone
----

A zone identifier. The value has to match with a map identifier defined
in :doc:`../../file-formats/dbc/areatable`.

position\_x
-----------

The X position for the characters initial position.

position\_y
-----------

The Y position for the characters initial position.

position\_z
-----------

The Z position for the characters initial position.

orientation
-----------

The orientation for the characters initial position.
