.. _db-world-player-levelstats:

==========================
"player\_levelstats" table
==========================

The ``player_levelstats`` table holds information on what stats are
gained by characters when they level up. Each race-class combination has
different level stats. All of the values in this table signify only the
base stats of the race-class combination at a specific level.

Table structure
---------------

+---------+-----------------------+--------+-------+-----------+---------+
| Field   | Type                  | Null   | Key   | Default   | Extra   |
+=========+=======================+========+=======+===========+=========+
| race    | tinyint(3) unsigned   | NO     | PRI   | NULL      |         |
+---------+-----------------------+--------+-------+-----------+---------+
| class   | tinyint(3) unsigned   | NO     | PRI   | NULL      |         |
+---------+-----------------------+--------+-------+-----------+---------+
| level   | tinyint(3) unsigned   | NO     | PRI   | NULL      |         |
+---------+-----------------------+--------+-------+-----------+---------+
| str     | tinyint(3) unsigned   | NO     |       | NULL      |         |
+---------+-----------------------+--------+-------+-----------+---------+
| agi     | tinyint(3) unsigned   | NO     |       | NULL      |         |
+---------+-----------------------+--------+-------+-----------+---------+
| sta     | tinyint(3) unsigned   | NO     |       | NULL      |         |
+---------+-----------------------+--------+-------+-----------+---------+
| inte    | tinyint(3) unsigned   | NO     |       | NULL      |         |
+---------+-----------------------+--------+-------+-----------+---------+
| spi     | tinyint(3) unsigned   | NO     |       | NULL      |         |
+---------+-----------------------+--------+-------+-----------+---------+

Fields
------

race
----

A bit-mask corresponding to races that should get the spell. The value
has to match with races defined in
`ChrRaces.dbc <../dbc/ChrRaces.dbc>`__.

class
-----

A bit-mask corresponding to class that should get the spell. The value
has to match with classes defined in
`ChrClasses.dbc <../dbc/ChrClasses.dbc>`__.

level
-----

The level at which the stats should be applied.

str
---

The base strength of the character.

agi
---

The base agility of the character.

sta
---

The base stamina of the character.

inte
----

The base intellect of the character.

spi
---

The base spirit of the character.
