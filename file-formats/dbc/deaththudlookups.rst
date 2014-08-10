.. _file-formats-dbc-deaththudlookups:

====================
DeathThudLookups.dbc
====================

The *death thud lookups* table defines which models and sounds should be
used when a creature dies, depending on it's size.

Table structure
---------------

+------+---------------------+---------------------+-----------+-----------------------+
| ID   | Name                | Type                | Default   | Description           |
+======+=====================+=====================+===========+=======================+
| 1    | ID                  | Integer             | -         | Unique ID             |
+------+---------------------+---------------------+-----------+-----------------------+
| 2    | sizeClass           | Integer (signed)    | 0         | See below.            |
+------+---------------------+---------------------+-----------+-----------------------+
| 3    | terrainType         | Integer             | 0         | Type of terrain.      |
+------+---------------------+---------------------+-----------+-----------------------+
| 4    | soundEntry          | Integer             | 0         | Dirt sound effect.    |
+------+---------------------+---------------------+-----------+-----------------------+
| 5    | soundEntryWater     | Integer             | 0         | Water sound effect.   |
+------+---------------------+---------------------+-----------+-----------------------+

Fields
------

sizeClass
~~~~~~~~~

-  ``0``: small,
-  ``1``: medium,
-  ``2``: large,
-  ``3``: giant,
-  ``4``: colossal.

Relations
---------

-  ``terrainType`` references the primary key of :doc:`terraintype`.
-  ``soundEntry`` and ``soundEntryWater`` reference the primary key of :doc:`soundentries`.
