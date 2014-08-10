.. _db-world-skill-fishing-base-level:

===================================
"skill\_fishing\_base\_level" table
===================================

The ``skill_fishing_base_level`` table holds information on the required
fishing skill for an area.

Table structure
---------------

+---------+-------------------------+--------+-------+-----------+---------+
| Field   | Type                    | Null   | Key   | Default   | Extra   |
+=========+=========================+========+=======+===========+=========+
| entry   | mediumint(8) unsigned   | NO     | PRI   | 0         |         |
+---------+-------------------------+--------+-------+-----------+---------+
| skill   | smallint(6)             | NO     |       | 0         |         |
+---------+-------------------------+--------+-------+-----------+---------+

Fields
------

entry
-----

A zone identifier. The value has to match with a zone identifier defined
in :doc:`../../file-formats/dbc/areatable`.

skill
-----

The minimum amount of skill points to fish in the referenced zone.
