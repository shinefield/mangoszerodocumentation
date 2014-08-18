.. _file-formats-dbc-groundeffecttexture:

=======================
GroundEffectTexture.dbc
=======================

The *ground effect doodad texture* table connects terrain types to flower doodads.

Table structure
---------------

+------+-----------------+--------------------+-----------+-------------------------------------------------+
| ID   | Name            | Type               | Default   | Description                                     |
+======+=================+====================+===========+=================================================+
| 1    | ID              | Integer            | -         | Unique ID                                       |
+------+-----------------+--------------------+-----------+-------------------------------------------------+
| 2    | doodad1         | Integer (signed)   | 0         | References a ground effect doodad to be used.   |
+------+-----------------+--------------------+-----------+-------------------------------------------------+
| 3    | doodad2         | Integer (signed)   | 0         | References a ground effect doodad to be used.   |
+------+-----------------+--------------------+-----------+-------------------------------------------------+
| 4    | doodad3         | Integer (signed)   | 0         | References a ground effect doodad to be used.   |
+------+-----------------+--------------------+-----------+-------------------------------------------------+
| 5    | doodad4         | Integer (signed)   | 0         | References a ground effect doodad to be used.   |
+------+-----------------+--------------------+-----------+-------------------------------------------------+
| 6    | density         | Integer (signed)   | 0         | The density for the texture.                    |
+------+-----------------+--------------------+-----------+-------------------------------------------------+
| 7    | terrainType     | Integer            | 0         | The terrain type to be used.                    |
+------+-----------------+--------------------+-----------+-------------------------------------------------+

Relations
---------

-  ``doodad[1-4]`` reference the primary key of :doc:`groundeffectdoodad`.
-  ``terrainType`` references the primary key of :doc:`terraintype`.
