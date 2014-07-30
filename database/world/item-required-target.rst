.. _db-world-item-required-target:

==============================
"item\_required\_target" table
==============================

The ``item_required_target`` table defines which targets are required
for the spells effect on an item.

Table structure
---------------

+---------------+-------------------------+--------+-------+-----------+---------+
| Field         | Type                    | Null   | Key   | Default   | Extra   |
+===============+=========================+========+=======+===========+=========+
| entry         | mediumint(8) unsigned   | NO     | PRI   | NULL      |         |
+---------------+-------------------------+--------+-------+-----------+---------+
| type          | tinyint(3) unsigned     | NO     | PRI   | 0         |         |
+---------------+-------------------------+--------+-------+-----------+---------+
| targetEntry   | mediumint(8) unsigned   | NO     | PRI   | 0         |         |
+---------------+-------------------------+--------+-------+-----------+---------+

Fields
------

entry
-----

This references the `item\_template <item_template>`__ tables unique ID.

type
----

Describes which type of target the spell requires. The following table
shows all valid target types.

+---------+--------------------------+
| Value   | Description              |
+=========+==========================+
| 0       | Game object              |
+---------+--------------------------+
| 1       | Creature template        |
+---------+--------------------------+
| 2       | Dead creature template   |
+---------+--------------------------+

targetEntry
-----------

Depending on the ``type`` value this references the
`creature\_template <creature_template>`__ tables unique ID, or the
`gameobject\_template <gameobject_template>`__ tables unique ID.
