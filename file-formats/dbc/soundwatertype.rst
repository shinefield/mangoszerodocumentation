.. _file-formats-dbc-soundwatertype:

==================
SoundWaterType.dbc
==================

The *sound water type* table contains definitions for connecting liquids
and matching sounds.

Table structure
---------------

+------+----------------+--------------------+-----------+----------------------------------------------------------+
| ID   | Name           | Type               | Default   | Description                                              |
+======+================+====================+===========+==========================================================+
| 1    | ID             | Integer (signed)   | -         | Unique ID                                                |
+------+----------------+--------------------+-----------+----------------------------------------------------------+
| 2    | liquidTypeID   | Integer (signed)   | 0         | References the liquid type to which the sound applies.   |
+------+----------------+--------------------+-----------+----------------------------------------------------------+
| 3    | fluidSpeed     | Integer            | 0         | See below.                                               |
+------+----------------+--------------------+-----------+----------------------------------------------------------+
| 4    | soundEntryID   | Integer (signed)   | 0         | The sound to apply to the liquid type.                   |
+------+----------------+--------------------+-----------+----------------------------------------------------------+

Fields
------

fluidSpeed
~~~~~~~~~~

-  ``0``: still,
-  ``4``: slow,
-  ``8``: fast.

Relations
---------

-  ``liquidTypeID`` references the primary key of ``LiquidType.dbc``.
-  ``soundEntryID`` references the primary key of ``SoundEntries.dbc``.
