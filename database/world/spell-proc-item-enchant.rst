.. _db-world-spell-proc-item-enchant:

==================================
"spell\_proc\_item\_enchant" table
==================================

The ``spell_proc_item_enchant`` table holds information for proc chances
of spells which enchant weapons.

This e.g. includes shaman weapon enchants.

Table structure
---------------

+-----------+-------------------------+--------+-------+-----------+---------+
| Field     | Type                    | Null   | Key   | Default   | Extra   |
+===========+=========================+========+=======+===========+=========+
| entry     | mediumint(8) unsigned   | NO     | PRI   | NULL      |         |
+-----------+-------------------------+--------+-------+-----------+---------+
| ppmRate   | float                   | NO     |       | 0         |         |
+-----------+-------------------------+--------+-------+-----------+---------+

Fields
------

entry
-----

The spell identifier. The value has to match with a spell identifier
defined in :doc:`../../file-formats/dbc/spell`.

ppmRate
-------

This field controls the times per minute that the spell should proc. If
zero, then the value is taken from the DBC entry.
