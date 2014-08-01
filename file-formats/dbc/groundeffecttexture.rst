.. _file-formats-dbc-groundeffecttexture:

=======================
GroundEffectTexture.dbc
=======================

The *ground effect doodad texture* table contains definitions for what
doodads get used for the effects on textures. This file also defines,
which sounds are played, which footprints you will leave and if snow for
example is thrown up when running.

Table structure
---------------

+------+-----------------+--------------------+-----------+-------------------------------------------------+
| ID   | Name            | Type               | Default   | Description                                     |
+======+=================+====================+===========+=================================================+
| 1    | ID              | Integer (signed)   | -         | Unique ID                                       |
+------+-----------------+--------------------+-----------+-------------------------------------------------+
| 2    | doodadID1       | Integer (signed)   | 0         | References a ground effect doodad to be used.   |
+------+-----------------+--------------------+-----------+-------------------------------------------------+
| 3    | doodadID2       | Integer (signed)   | 0         | References a ground effect doodad to be used.   |
+------+-----------------+--------------------+-----------+-------------------------------------------------+
| 4    | doodadID3       | Integer (signed)   | 0         | References a ground effect doodad to be used.   |
+------+-----------------+--------------------+-----------+-------------------------------------------------+
| 5    | doodadID4       | Integer (signed)   | 0         | References a ground effect doodad to be used.   |
+------+-----------------+--------------------+-----------+-------------------------------------------------+
| 6    | density         | Integer            | 0         | The density for the texture.                    |
+------+-----------------+--------------------+-----------+-------------------------------------------------+
| 7    | terrainTypeID   | Integer (signed)   | 0         | The terrain type to be used.                    |
+------+-----------------+--------------------+-----------+-------------------------------------------------+

Relations
---------

-  ``doodadID[1-4]`` reference the primary key of
   ``GroundEffectDoodad.dbc``.
-  ``terrainTypeID`` references the primary key of ``TerrainType.dbc``.

