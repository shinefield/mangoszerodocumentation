.. _db-world-pet-levelstats:

=======================
"pet\_levelstats" table
=======================

The ``pet_levelstats`` table holds information on individual pet base
stats based on level.

Table structure
---------------

+-------------------+-------------------------+--------+-------+-----------+---------+
| Field             | Type                    | Null   | Key   | Default   | Extra   |
+===================+=========================+========+=======+===========+=========+
| creature\_entry   | mediumint(8) unsigned   | NO     | PRI   | NULL      |         |
+-------------------+-------------------------+--------+-------+-----------+---------+
| level             | tinyint(3) unsigned     | NO     | PRI   | NULL      |         |
+-------------------+-------------------------+--------+-------+-----------+---------+
| hp                | smallint(5) unsigned    | NO     |       | NULL      |         |
+-------------------+-------------------------+--------+-------+-----------+---------+
| mana              | smallint(5) unsigned    | NO     |       | NULL      |         |
+-------------------+-------------------------+--------+-------+-----------+---------+
| armor             | int(10) unsigned        | NO     |       | 0         |         |
+-------------------+-------------------------+--------+-------+-----------+---------+
| str               | smallint(5) unsigned    | NO     |       | NULL      |         |
+-------------------+-------------------------+--------+-------+-----------+---------+
| agi               | smallint(5) unsigned    | NO     |       | NULL      |         |
+-------------------+-------------------------+--------+-------+-----------+---------+
| sta               | smallint(5) unsigned    | NO     |       | NULL      |         |
+-------------------+-------------------------+--------+-------+-----------+---------+
| inte              | smallint(5) unsigned    | NO     |       | NULL      |         |
+-------------------+-------------------------+--------+-------+-----------+---------+
| spi               | smallint(5) unsigned    | NO     |       | NULL      |         |
+-------------------+-------------------------+--------+-------+-----------+---------+

Fields
------

creature\_entry
---------------

This references the `creature\_template <creature_template>`__ tables
unique ID of the pet's creature\_template for which the entry is valid.

level
-----

The pet level.

hp
--

The base health of the pet at currently selected level.

mana
----

The base mana of the pet at currently selected level.

armor
-----

The base armor of the pet at currently selected level.

str
---

The base strength of the pet at currently selected level.

agi
---

The base agility of the pet at currently selected level.

sta
---

The base stamina of the pet at currently selected level.

inte
----

The base intellect of the pet at currently selected level.

spi
---

The base spirit of the pet at currently selected level.
