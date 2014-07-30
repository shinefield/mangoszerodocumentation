.. _db-world-npc-vendor:

===================
"npc\_vendor" table
===================

The ``npc_vendor`` table holds item lists used for a singular vendor to
provide.

Table structure
---------------

+-----------------+-------------------------+--------+-------+-----------+---------+
| Field           | Type                    | Null   | Key   | Default   | Extra   |
+=================+=========================+========+=======+===========+=========+
| entry           | mediumint(8) unsigned   | NO     | PRI   | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| item            | mediumint(8) unsigned   | NO     | PRI   | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| maxcount        | tinyint(3) unsigned     | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| incrtime        | int(10) unsigned        | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| condition\_id   | mediumint(8) unsigned   | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+

Fields
------

entry
-----

The vendor which should sell this item. This references the
`creature\_template <creature_template>`__ tables unique ID for which
the entry is valid.

item
----

The item a vendor should sell. This references the
`item\_template <item_template>`__ tables unique ID.

maxcount
--------

The maximum amount of the item a vendor should carry. Set to ``0`` to
provide unlimited supplies.

incrtime
--------

This field decides how frequently a vendor will restock and item having
a maximum count. The value is given in seconds, and for limited items,
the ``BuyCount`` column of the `item\_template <item_template>`__ is
taken into account when restocking.

condition\_id
-------------

This references the `conditions <conditions>`__ tables unique ID for
which the entry is valid.
