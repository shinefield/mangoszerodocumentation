.. _db-world-areatrigger-involvedrelation:

=====================================
"areatrigger\_involvedrelation" table
=====================================

The ``areatrigger_involvedrelation`` table holds connections between
triggers and quests.

If there is a record in the table for a quest, the quest will not be
completed until the player activates the areatriger. The quest is not
necessarily finished after that, but that one condition of the quest is
satisfied. If the only condition of the quest is to explore an area,
then the quest will be complete.

Table structure
---------------

+---------+-------------------------+--------+-------+-----------+---------+
| Field   | Type                    | Null   | Key   | Default   | Extra   |
+=========+=========================+========+=======+===========+=========+
| id      | mediumint(8) unsigned   | NO     | PRI   | 0         |         |
+---------+-------------------------+--------+-------+-----------+---------+
| quest   | mediumint(8) unsigned   | NO     |       | 0         |         |
+---------+-------------------------+--------+-------+-----------+---------+

Fields
------

id
--

An areatrigger identifier. The value has to match with a areatrigger
identifier defined in :doc:`../../file-formats/dbc/areatrigger`.

quest
-----

This references the :doc:`quest-template` tables unique
ID for which the entry is valid.
