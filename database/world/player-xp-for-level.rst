.. _db-world-player-xp-for-level:

==============================
"player\_xp\_for\_level" table
==============================

The ``player_xp_for_level`` table holds how many experience points are
required to progress from one level to the next.

Table structure
---------------

+------------------------+--------------------+--------+-------+-----------+---------+
| Field                  | Type               | Null   | Key   | Default   | Extra   |
+========================+====================+========+=======+===========+=========+
| lvl                    | int(3) unsigned    | NO     | PRI   | NULL      |         |
+------------------------+--------------------+--------+-------+-----------+---------+
| xp\_for\_next\_level   | int(10) unsigned   | NO     |       | NULL      |         |
+------------------------+--------------------+--------+-------+-----------+---------+

Fields
------

lvl
---

The player's level.

xp\_for\_next\_level
--------------------

The experience needed to upgrade from the value in ``lvl`` field to
``lvl`` +1.
