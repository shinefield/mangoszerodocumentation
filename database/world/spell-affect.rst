.. _db-world-spell-affect:

=====================
"spell\_affect" table
=====================

The ``spell_affect`` table holds information on what spells are affected
by spell modifiers.

All spells in this table need to apply an aura that either adds a flat
modifier to other spells, or adds a percent modifier to other spells.
Each entry applies to *one* spell effect, thus spells with multiple
effects will require multiple entries.

Table structure
---------------

+-------------------+------------------------+--------+-------+-----------+---------+
| Field             | Type                   | Null   | Key   | Default   | Extra   |
+===================+========================+========+=======+===========+=========+
| entry             | smallint(5) unsigned   | NO     | PRI   | 0         |         |
+-------------------+------------------------+--------+-------+-----------+---------+
| effectId          | tinyint(3) unsigned    | NO     | PRI   | 0         |         |
+-------------------+------------------------+--------+-------+-----------+---------+
| SpellFamilyMask   | bigint(20) unsigned    | NO     |       | 0         |         |
+-------------------+------------------------+--------+-------+-----------+---------+

Fields
------

entry
-----

The spell identifier. The value has to match with a spell identifier
defined in :doc:`../../file-formats/dbc/spell`.

effectId
--------

This holds an index to the referenced spells effect. Three spell effects
may be contained in a single spell, thus valid indexes are ``0``, ``1``
and ``2``.

SpellFamilyMask
---------------

A spell class identifier. The value has to match with a spell class
identifier from :doc:`../../file-formats/dbc/spell`, and references the
``spellClassSet`` field in that file.
