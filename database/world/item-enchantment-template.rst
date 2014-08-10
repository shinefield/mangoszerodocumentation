.. _db-world-item-enchantment-template:

===================================
"item\_enchantment\_template" table
===================================

The ``item_enchantment_template`` table holds chances for the properties
of items which have a random properties attached.

Table structure
---------------

+----------+-------------------------+--------+-------+-----------+---------+
| Field    | Type                    | Null   | Key   | Default   | Extra   |
+==========+=========================+========+=======+===========+=========+
| entry    | mediumint(8) unsigned   | NO     | PRI   | 0         |         |
+----------+-------------------------+--------+-------+-----------+---------+
| ench     | mediumint(8) unsigned   | NO     | PRI   | 0         |         |
+----------+-------------------------+--------+-------+-----------+---------+
| chance   | float unsigned          | NO     |       | 0         |         |
+----------+-------------------------+--------+-------+-----------+---------+

Fields
------

entry
-----

The random properties unique identifier. This is referenced from the
:doc:`item-template` table's ``RandomProperty`` table.

ench
----

The actual enchantment which should be applied to the item. This
references an entry in the :doc:`../../file-formats/dbc/itemrandomproperties`
table.

chance
------

The chance for a random property to be applied to the item.

For each entry in this table, the combined chances of all properties
needs to equal ``100``, otherwise the item may not get a random
enchantment on it.
