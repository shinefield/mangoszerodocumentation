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
| 1    | ID                  | Integer (signed),   | -         | Unique ID             |
+------+---------------------+---------------------+-----------+-----------------------+
| 2    | sizeClass           | Integer,            | 0         | See below.            |
+------+---------------------+---------------------+-----------+-----------------------+
| 3    | terrainTypeID       | Integer (signed),   | 0         | Type of terrain.      |
+------+---------------------+---------------------+-----------+-----------------------+
| 4    | soundEntryID        | Integer (signed),   | 0         | Dirt sound effect.    |
+------+---------------------+---------------------+-----------+-----------------------+
| 5    | soundEntryIDWater   | Integer (signed),   | 0         | Water sound effect.   |
+------+---------------------+---------------------+-----------+-----------------------+

Fields
------

sizeClass
---------

-  ``0``: small,
-  ``1``: medium,
-  ``2``: large,
-  ``3``: giant,
-  ``4``: colossal.

Relations
---------

-  ``terrainTypeID`` references the primary key of ``TerrainType.dbc``.
-  ``soundEntryID`` and ``soundEntryIDWater`` reference the primary key
   of ``SoundEntries.dbc``.

