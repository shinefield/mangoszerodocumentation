.. _db-world-creature-equip-template-raw:

======================================
"creature\_equip\_template\_raw" table
======================================

The ``creature_equip_template_raw`` table holds information in items
that creatures should wear.

.. deprecated::

    this table is *deprecated*. Do not use it, as it will be
    removed in a future update and is just here to ease transition to the
    new ``creature_equip_template`` table.

Table structure
---------------

+---------------+-------------------------+--------+-------+-----------+---------+
| Field         | Type                    | Null   | Key   | Default   | Extra   |
+===============+=========================+========+=======+===========+=========+
| entry         | mediumint(8) unsigned   | NO     | PRI   | 0         |         |
+---------------+-------------------------+--------+-------+-----------+---------+
| equipmodel1   | mediumint(8) unsigned   | NO     |       | 0         |         |
+---------------+-------------------------+--------+-------+-----------+---------+
| equipmodel2   | mediumint(8) unsigned   | NO     |       | 0         |         |
+---------------+-------------------------+--------+-------+-----------+---------+
| equipmodel3   | mediumint(8) unsigned   | NO     |       | 0         |         |
+---------------+-------------------------+--------+-------+-----------+---------+
| equipinfo1    | int(10) unsigned        | NO     |       | 0         |         |
+---------------+-------------------------+--------+-------+-----------+---------+
| equipinfo2    | int(10) unsigned        | NO     |       | 0         |         |
+---------------+-------------------------+--------+-------+-----------+---------+
| equipinfo3    | int(10) unsigned        | NO     |       | 0         |         |
+---------------+-------------------------+--------+-------+-----------+---------+
| equipslot1    | int(11)                 | NO     |       | 0         |         |
+---------------+-------------------------+--------+-------+-----------+---------+
| equipslot2    | int(11)                 | NO     |       | 0         |         |
+---------------+-------------------------+--------+-------+-----------+---------+
| equipslot3    | int(11)                 | NO     |       | 0         |         |
+---------------+-------------------------+--------+-------+-----------+---------+

