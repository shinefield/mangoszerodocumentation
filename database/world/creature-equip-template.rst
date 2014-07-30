.. _db-world-creature-equip-template:

=================================
"creature\_equip\_template" table
=================================

The ``creature_equip_template`` table holds information in items that
creatures should wear.

Table structure
---------------

+---------------+-------------------------+--------+-------+-----------+---------+
| Field         | Type                    | Null   | Key   | Default   | Extra   |
+===============+=========================+========+=======+===========+=========+
| entry         | mediumint(8) unsigned   | NO     | PRI   | 0         |         |
+---------------+-------------------------+--------+-------+-----------+---------+
| equipentry1   | mediumint(8) unsigned   | NO     |       | 0         |         |
+---------------+-------------------------+--------+-------+-----------+---------+
| equipentry2   | mediumint(8) unsigned   | NO     |       | 0         |         |
+---------------+-------------------------+--------+-------+-----------+---------+
| equipentry3   | mediumint(8) unsigned   | NO     |       | 0         |         |
+---------------+-------------------------+--------+-------+-----------+---------+

Fields
------

entry
-----

The unique identifier for the equipment template.

equipentry1
-----------

The item the creature should wear in the right hand.

equipentry2
-----------

The item the creature should wear in the left hand.

equipentry3
-----------

The ranged item the creature should wear.
