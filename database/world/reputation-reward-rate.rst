.. _db-world-reputation-reward-rate:

================================
"reputation\_reward\_rate" table
================================

The ``reputation_reward_rate`` table holds multipliers for reputation
awarded to specific factions.

Table structure
---------------

+------------------+-------------------------+--------+-------+-----------+---------+
| Field            | Type                    | Null   | Key   | Default   | Extra   |
+==================+=========================+========+=======+===========+=========+
| faction          | mediumint(8) unsigned   | NO     | PRI   | 0         |         |
+------------------+-------------------------+--------+-------+-----------+---------+
| quest\_rate      | float                   | NO     |       | 1         |         |
+------------------+-------------------------+--------+-------+-----------+---------+
| creature\_rate   | float                   | NO     |       | 1         |         |
+------------------+-------------------------+--------+-------+-----------+---------+
| spell\_rate      | float                   | NO     |       | 1         |         |
+------------------+-------------------------+--------+-------+-----------+---------+

Fields
------

faction
-------

A faction for which reputation is awarded. The value has to match with a
faction identifier defined in :doc:`../../file-formats/dbc/faction`.

quest\_rate
-----------

The rate for reputation gain from quests.

creature\_rate
--------------

The rate for reputation gain from creatures.

spell\_rate
-----------

The rate for reputation gain from spells.
