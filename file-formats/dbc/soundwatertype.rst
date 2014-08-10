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
| 1    | ID             | Integer            | -         | Unique ID                                                |
+------+----------------+--------------------+-----------+----------------------------------------------------------+
| 2    | liquidType     | Integer            | 0         | References the liquid type to which the sound applies.   |
+------+----------------+--------------------+-----------+----------------------------------------------------------+
| 3    | fluidSpeed     | Integer (signed)   | 0         | See below.                                               |
+------+----------------+--------------------+-----------+----------------------------------------------------------+
| 4    | soundEntry     | Integer            | 0         | The sound to apply to the liquid type.                   |
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

-  ``liquidType`` references the primary key of :doc:`liquidtype`.
-  ``soundEntry`` references the primary key of :doc:`soundentries`.
