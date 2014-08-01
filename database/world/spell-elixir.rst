.. _db-world-spell-elixir:

=====================
"spell\_elixir" table
=====================

The ``spell_elixir`` table holds classifications for potion spells to
prevent simultaneous use of potion in identical classes.

.. note::

    Technically the use of classifications does not make any sense
    for vanilla WoW, since these were introduced in WoW version 2.1. In
    vanilla WoW, potions would only be marked as flasks, which disallowed
    dispelling these in PvP situations.

    In rare occasions spells for food can grant the buffs after eating for a
    specified time period. These spells are marked here, too.

Table structure
---------------

+---------+-----------------------+--------+-------+-----------+---------+
| Field   | Type                  | Null   | Key   | Default   | Extra   |
+=========+=======================+========+=======+===========+=========+
| entry   | int(11) unsigned      | NO     | PRI   | 0         |         |
+---------+-----------------------+--------+-------+-----------+---------+
| mask    | tinyint(1) unsigned   | NO     |       | 0         |         |
+---------+-----------------------+--------+-------+-----------+---------+

Fields
------

entry
-----

The spell identifier. The value has to match with a spell identifier
defined in `Spell.dbc <../dbc/Spell.dbc>`__. This is the spell cast by
the potion use.

mask
----

Defines what type of potion/food spell this is. The following table
lists the available values.

+---------+--------------------------------+
| Value   | Type                           |
+=========+================================+
| 0       | None                           |
+---------+--------------------------------+
| 3       | Flask                          |
+---------+--------------------------------+
| 16      | Food granting well fed buffs   |
+---------+--------------------------------+

