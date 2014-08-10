.. _file-formats-dbc-terraintype:

===============
TerrainType.dbc
===============

The *terrain type* table contains definitions for available terrain
types and the use of sound and footsteps on them.

Table structure
---------------

+------+---------------------+--------------------+-----------+----------------------------------------------------------------------------+
| ID   | Name                | Type               | Default   | Description                                                                |
+======+=====================+====================+===========+============================================================================+
| 1    | ID                  | Integer            | -         | Unique ID                                                                  |
+------+---------------------+--------------------+-----------+----------------------------------------------------------------------------+
| 2    | description         | String             | -         | The name of the terrain type.                                              |
+------+---------------------+--------------------+-----------+----------------------------------------------------------------------------+
| 3    | footstepSprayRun    | Integer            | 0         | Visual effect shown when a character is running on this terrain.           |
+------+---------------------+--------------------+-----------+----------------------------------------------------------------------------+
| 4    | footstepSprayWalk   | Integer            | 0         | Visual effect shown when a character is walking on this terrain.           |
+------+---------------------+--------------------+-----------+----------------------------------------------------------------------------+
| 5    | soundEntry          | Integer            | 0         | The sound entry to be played when a character is moving on this terrain.   |
+------+---------------------+--------------------+-----------+----------------------------------------------------------------------------+
| 6    | flags               | Integer (signed)   | 0         | See below.                                                                 |
+------+---------------------+--------------------+-----------+----------------------------------------------------------------------------+

Fields
------

flags
~~~~~

-  ``0``: do not display footsteps.
-  ``1``: display footsteps on this terrain type.

Relations
---------

-  ``footstepSprayRun`` and ``footstepSprayWalk`` reference the primary key of :doc:`spellvisualeffectname`.
-  ``terrainTypeSound`` references the primary key of :doc:`terraintypesounds`.
