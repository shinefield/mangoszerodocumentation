.. _db-world-spell-bonus-data:

==========================
"spell\_bonus\_data" table
==========================

The ``spell_bonus_data`` table holds information on bonus modifiers for
spells.

A bonus can modify damage done, healing done, and also attack power.

Table structure
---------------

+------------------+------------------------+--------+-------+-----------+---------+
| Field            | Type                   | Null   | Key   | Default   | Extra   |
+==================+========================+========+=======+===========+=========+
| entry            | smallint(5) unsigned   | NO     | PRI   | NULL      |         |
+------------------+------------------------+--------+-------+-----------+---------+
| direct\_bonus    | float                  | NO     |       | 0         |         |
+------------------+------------------------+--------+-------+-----------+---------+
| dot\_bonus       | float                  | NO     |       | 0         |         |
+------------------+------------------------+--------+-------+-----------+---------+
| ap\_bonus        | float                  | NO     |       | 0         |         |
+------------------+------------------------+--------+-------+-----------+---------+
| ap\_dot\_bonus   | float                  | NO     |       | 0         |         |
+------------------+------------------------+--------+-------+-----------+---------+
| comments         | varchar(255)           | YES    |       | NULL      |         |
+------------------+------------------------+--------+-------+-----------+---------+

Fields
------

entry
-----

The spell identifier. The value has to match with a spell identifier
defined in `Spell.dbc <../dbc/Spell.dbc>`__.

direct\_bonus
-------------

The bonus applied to the spell power damage.

-  if < 0: calculate default spell power coefficient.
-  if = 0: do not apply any spell power coefficient (do not scale damage
   with spell power).
-  if > 0: use this as new spell power coefficient.

dot\_bonus
----------

The bonus applied to the damage over time.

-  if < 0: calculate default spell power coefficient.
-  if = 0: do not apply any spell power coefficient (do not scale damage
   with spell power).
-  if > 0: use this as new spell power coefficient.

ap\_bonus
---------

The bonus applied to melee or ranged damage.

-  if < 0: calculate default attack power coefficient.
-  if = 0: do not apply any attack power coefficient (do not scale
   damage with attack power).
-  if > 0: use this as new attack power coefficient.

ap\_dot\_bonus
--------------

The bonus applied to melee or ranged damaged over time.

-  if < 0: calculate default attack power coefficient.
-  if = 0: do not apply any attack power coefficient (do not scale
   damage with attack power).
-  if > 0: use this as new attack power coefficient.

comments
--------

A comment describing why the bonus is granted. Entries without comment
should be considered invalid, and immediately be verified and commented.
