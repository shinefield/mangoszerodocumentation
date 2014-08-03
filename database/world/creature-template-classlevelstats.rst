.. _db-world-creature-template-classlevelstats:

===========================================
"creature\_template\_classlevelstats" table
===========================================

The ``creature_template_classlevelstats`` table holds definitions which
modify a ``creature_template`` entries state based on class and level.

Table structure
---------------

+-------------------------+-------------------------+--------+-------+-----------+---------+
| Field                   | Type                    | Null   | Key   | Default   | Extra   |
+=========================+=========================+========+=======+===========+=========+
| Level                   | tinyint(4)              | NO     |       |           |         |
+-------------------------+-------------------------+--------+-------+-----------+---------+
| Class                   | tinyint(4)              | NO     |       |           |         |
+-------------------------+-------------------------+--------+-------+-----------+---------+
| BaseHealthExp0          | mediumint(8) unsigned   | NO     |       | 1         |         |
+-------------------------+-------------------------+--------+-------+-----------+---------+
| BaseMana                | mediumint(8) unsigned   | NO     |       | 0         |         |
+-------------------------+-------------------------+--------+-------+-----------+---------+
| BaseDamageExp0          | float                   | NO     |       | 0         |         |
+-------------------------+-------------------------+--------+-------+-----------+---------+
| BaseMeleeAttackPower    | float                   | NO     |       | 0         |         |
+-------------------------+-------------------------+--------+-------+-----------+---------+
| BaseRangedAttackPower   | float                   | NO     |       | 0         |         |
+-------------------------+-------------------------+--------+-------+-----------+---------+
| BaseArmor               | mediumint(8) unsigned   | NO     |       | 0         |         |
+-------------------------+-------------------------+--------+-------+-----------+---------+

Fields
------

Level
-----

Creature level for the stats. Could Be ``MinLevel`` or ``MaxLevel`` or both, could Be Same if
the creature only has a single level.

Class
-----

A creature's class. The following table describes the available classes.

+---------+-----------+-----------------------------------------+
| Value   | Name      | Description                             |
+=========+===========+=========================================+
| 1       | Warrior   | Has increased health and no mana        |
+---------+-----------+-----------------------------------------+
| 2       | Paladin   | Has increased health and low mana       |
+---------+-----------+-----------------------------------------+
| 4       | Rogue     | Has increased damage, but lower armor   |
+---------+-----------+-----------------------------------------+
| 8       | Mage      | Has low health, but increased mana      |
+---------+-----------+-----------------------------------------+

BaseHealthExp0
--------------

Base health value for expansion 0 aka. vanilla WoW.

BaseMana
--------

Base mana value for any creature of this level and class.

BaseDamageExp0
--------------

Base damage value for expansion 0 aka. vanilla WoW.

BaseMeleeAttackPower
--------------------

Base melee attack power that has been factored for low level creatures.

.. tip::

    This is raw base value to be used for all melee damage calculations.

BaseRangedAttackPower
---------------------

Base ranged attack power.

.. tip::

    This is raw base value to be used for all ranged damage calculations.


BaseArmor
---------

Base armor value for any creature of this level and class.
