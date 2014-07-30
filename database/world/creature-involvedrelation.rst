.. _db-world-creature-involvedrelation:

==================================
"creature\_involvedrelation" table
==================================

The ``creature_involvedrelation`` table holds connections between
creatures and quests. Links made here define that a creature should end
a quest.

Table structure
---------------

+---------+-------------------------+--------+-------+-----------+---------+
| Field   | Type                    | Null   | Key   | Default   | Extra   |
+=========+=========================+========+=======+===========+=========+
| id      | mediumint(8) unsigned   | NO     | PRI   | 0         |         |
+---------+-------------------------+--------+-------+-----------+---------+
| quest   | mediumint(8) unsigned   | NO     | PRI   | 0         |         |
+---------+-------------------------+--------+-------+-----------+---------+

Fields
------

id
--

This references the `creature\_template <creature_template>`__ tables
unique ID for which the entry is valid.

quest
-----

This references the `quest\_template <quest_template>`__ tables unique
ID for which the entry is valid.
