.. _db-world-creature-template-spells:

==================================
"creature\_template\_spells" table
==================================

The ``creature_template_spells`` table holds information on the spells
to which a creature\_template has access.

Table structure
---------------

+----------+-------------------------+--------+-------+-----------+---------+
| Field    | Type                    | Null   | Key   | Default   | Extra   |
+==========+=========================+========+=======+===========+=========+
| entry    | mediumint(8) unsigned   | NO     | PRI   | NULL      |         |
+----------+-------------------------+--------+-------+-----------+---------+
| spell1   | mediumint(8) unsigned   | NO     |       | NULL      |         |
+----------+-------------------------+--------+-------+-----------+---------+
| spell2   | mediumint(8) unsigned   | NO     |       | 0         |         |
+----------+-------------------------+--------+-------+-----------+---------+
| spell3   | mediumint(8) unsigned   | NO     |       | 0         |         |
+----------+-------------------------+--------+-------+-----------+---------+
| spell4   | mediumint(8) unsigned   | NO     |       | 0         |         |
+----------+-------------------------+--------+-------+-----------+---------+

Fields
------

entry
-----

This references the :doc:`creature-template` tables
unique ID for which the entry is valid.

spell1
------

The spell identifier. The value has to match with a spell identifier
defined in :doc:`../../file-formats/dbc/spell`.

spell2
------

The spell identifier. The value has to match with a spell identifier
defined in :doc:`../../file-formats/dbc/spell`.

spell3
------

The spell identifier. The value has to match with a spell identifier
defined in :doc:`../../file-formats/dbc/spell`.

spell4
------

The spell identifier. The value has to match with a spell identifier
defined in :doc:`../../file-formats/dbc/spell`.
