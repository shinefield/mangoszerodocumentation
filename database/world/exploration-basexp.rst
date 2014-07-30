.. _db-world-exploration-basexp:

===========================
"exploration\_basexp" table
===========================

The ``exploration_basexp`` table holds definitions for experience
rewarded upon exploring zones.

Table structure
---------------

+----------+----------------+--------+-------+-----------+---------+
| Field    | Type           | Null   | Key   | Default   | Extra   |
+==========+================+========+=======+===========+=========+
| level    | tinyint(4)     | NO     | PRI   | 0         |         |
+----------+----------------+--------+-------+-----------+---------+
| basexp   | mediumint(9)   | NO     |       | 0         |         |
+----------+----------------+--------+-------+-----------+---------+

Fields
------

level
-----

The character level.

basexp
------

The experience rewarded at the specified level.
