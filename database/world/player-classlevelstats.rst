.. _db-world-player-classlevelstats:

"player\_classlevelstats" table
===============================

The ``player_classlevelstats`` table holds information on the base
health and mana of characters when they level up. Each class has
different level stats. All of the values in this table signify only the
base health and mana of the class at a specific level.

Table structure
---------------

+------------+------------------------+--------+-------+-----------+---------+
| Field      | Type                   | Null   | Key   | Default   | Extra   |
+============+========================+========+=======+===========+=========+
| class      | tinyint(3) unsigned    | NO     | PRI   | NULL      |         |
+------------+------------------------+--------+-------+-----------+---------+
| level      | tinyint(3) unsigned    | NO     | PRI   | NULL      |         |
+------------+------------------------+--------+-------+-----------+---------+
| basehp     | smallint(5) unsigned   | NO     |       | NULL      |         |
+------------+------------------------+--------+-------+-----------+---------+
| basemana   | smallint(5) unsigned   | NO     |       | NULL      |         |
+------------+------------------------+--------+-------+-----------+---------+

Fields
------

class
-----

A bit-mask corresponding to class that should get the spell. The value
has to match with classes defined in
`ChrClasses.dbc <../dbc/ChrClasses.dbc>`__.

level
-----

The level at which the stats should be applied.

basehp
------

The base health of the character (before stamina bonuses).

basemana
--------

The base mana of the character (before intellect bonuses).
