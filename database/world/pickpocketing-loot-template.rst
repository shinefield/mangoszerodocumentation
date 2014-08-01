.. _db-world-pickpocketing-loot-template:

=====================================
"pickpocketing\_loot\_template" table
=====================================

The ``pickpocketing_loot_template`` table holds definitions on items
dropped by pickpocketing creatures.

.. note::

    pickpocketing loot is handed out to rogues only. Bad luck, hunters!

Table structure
---------------

+-----------------------+-------------------------+--------+-------+-----------+---------+
| Field                 | Type                    | Null   | Key   | Default   | Extra   |
+=======================+=========================+========+=======+===========+=========+
| entry                 | mediumint(8) unsigned   | NO     | PRI   | 0         |         |
+-----------------------+-------------------------+--------+-------+-----------+---------+
| item                  | mediumint(8) unsigned   | NO     | PRI   | 0         |         |
+-----------------------+-------------------------+--------+-------+-----------+---------+
| ChanceOrQuestChance   | float                   | NO     |       | 100       |         |
+-----------------------+-------------------------+--------+-------+-----------+---------+
| groupid               | tinyint(3) unsigned     | NO     |       | 0         |         |
+-----------------------+-------------------------+--------+-------+-----------+---------+
| mincountOrRef         | mediumint(9)            | NO     |       | 1         |         |
+-----------------------+-------------------------+--------+-------+-----------+---------+
| maxcount              | tinyint(3) unsigned     | NO     |       | 1         |         |
+-----------------------+-------------------------+--------+-------+-----------+---------+
| condition\_id         | mediumint(8) unsigned   | NO     |       | 0         |         |
+-----------------------+-------------------------+--------+-------+-----------+---------+

Fields
------

entry
-----

This references the `creature\_template <creature_template>`__ tables
unique ID for which the entry is valid.

item
----

This references the `item\_template <item_template>`__ tables unique ID
for which the entry is valid.

ChanceOrQuestChance
-------------------

This field determines if an item should drop by chance, or by the
character looting having a quest. The meaning is determined by the
fields signedness and the value of the ``mincountOrRef`` field's value.

The following table shows possible combinations and their meanings.

+-----------------------+-----------------+------------------------------------------------+
| ChanceOrQuestChance   | mincountOrRef   | Description                                    |
+=======================+=================+================================================+
| > 0                   | > 0             | A simple percentage based drop chance.         |
+-----------------------+-----------------+------------------------------------------------+
| < 0                   | > 0             | A quest based drop chance.                     |
+-----------------------+-----------------+------------------------------------------------+
| > 0                   | < 0             | A drop chance which has a chance to be used.   |
+-----------------------+-----------------+------------------------------------------------+

.. note::

    setting ``ChanceOrQuestChance`` to ``0`` is only allowed for
    entries which are part of a loot group (aka. have a ``groupid`` set).
    Also note that non-zero values are subject to multiplication based on
    the drop rate configured in the world server configuration if they are
    not part of a loot group.

groupid
-------

A group is a set of loot definitions processed in such a way that at any
given looting event the loot generated can receive one (or none) item
from the items declared in the loot definitions of the group.

Groups are formed by loot definitions having the same values of
``entry`` and ``groupid`` fields and having ``mincountOrRef`` set to a
value greater than ``0``.

mincountOrRef
-------------

Depending on the value of the field it may either define the minimum
number of copies for the item to be dropped, or it may reference another
loot template.

-  positive values indicate that a minimum amount should be dropped,
-  negative values indicate a reference to another loot template.

maxcount
--------

This field may either designated the maximum number of items to drop
from a loot template, or how many times a referenced loot template
should be processed.

-  when ``mincountOrRef`` is positive, this indicates the maximum number
   of items to drop from the loot template,
-  when ``mincountOrRef`` is negative, this indicates how many times the
   loot template referenced in ``mincountOrRef`` should be processed.

condition\_id
-------------

This references the `conditions <conditions>`__ tables unique ID for
which the entry is valid.
