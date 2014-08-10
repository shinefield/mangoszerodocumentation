.. _db-world-areatrigger-teleport:

=============================
"areatrigger\_teleport" table
=============================

The ``areatrigger_teleport`` table holds information which areatrigger
teleports characters and the requirements to execute the teleport.

Table structure
---------------

+-------------------------+-------------------------+--------+-------+-----------+---------+
| Field                   | Type                    | Null   | Key   | Default   | Extra   |
+=========================+=========================+========+=======+===========+=========+
| id                      | mediumint(8) unsigned   | NO     | PRI   | 0         |         |
+-------------------------+-------------------------+--------+-------+-----------+---------+
| name                    | text                    | YES    |       | NULL      |         |
+-------------------------+-------------------------+--------+-------+-----------+---------+
| required\_level         | tinyint(3) unsigned     | NO     |       | 0         |         |
+-------------------------+-------------------------+--------+-------+-----------+---------+
| required\_item          | mediumint(8) unsigned   | NO     |       | 0         |         |
+-------------------------+-------------------------+--------+-------+-----------+---------+
| required\_item2         | mediumint(8) unsigned   | NO     |       | 0         |         |
+-------------------------+-------------------------+--------+-------+-----------+---------+
| required\_quest\_done   | int(11) unsigned        | NO     |       | 0         |         |
+-------------------------+-------------------------+--------+-------+-----------+---------+
| target\_map             | smallint(5) unsigned    | NO     |       | 0         |         |
+-------------------------+-------------------------+--------+-------+-----------+---------+
| target\_position\_x     | float                   | NO     |       | 0         |         |
+-------------------------+-------------------------+--------+-------+-----------+---------+
| target\_position\_y     | float                   | NO     |       | 0         |         |
+-------------------------+-------------------------+--------+-------+-----------+---------+
| target\_position\_z     | float                   | NO     |       | 0         |         |
+-------------------------+-------------------------+--------+-------+-----------+---------+
| target\_orientation     | float                   | NO     |       | 0         |         |
+-------------------------+-------------------------+--------+-------+-----------+---------+

Fields
------

id
--

An areatrigger identifier. The value has to match with a areatrigger
identifier defined in :doc:`../../file-formats/dbc/areatrigger`.

name
----

The name for the areatrigger. This is only used for documentation
purposes to help identifying triggers.

required\_level
---------------

The minimum level required to activate the trigger.

required\_item
--------------

Item required to activate the trigger. This references the
`item\_template <item_template>`__ tables unique ID for which the entry
is valid.

required\_item2
---------------

Another item required to activate the trigger. This references the
`item\_template <item_template>`__ tables unique ID for which the entry
is valid.

required\_quest\_done
---------------------

Quest required to be completed to activate the trigger. This references
the `quest\_template <quest_template>`__ tables unique ID for which the
entry is valid.

target\_map
-----------

The target map's identifier. The value has to match with a map
identifier defined in :doc:`../../file-formats/dbc/map`.

target\_position\_x
-------------------

The X position on the target map.

target\_position\_y
-------------------

The Y position on the target map.

target\_position\_z
-------------------

The Z position on the target map.

target\_orientation
-------------------

The orientation for the character on the target map. This is measured in
radians, ``0`` is north on the mini-map and ``pi`` is south on the
mini-map etc.
