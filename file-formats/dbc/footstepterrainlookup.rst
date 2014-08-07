.. _file-formats-dbc-footstepterrainlookup:

=========================
FootstepTerrainLookup.dbc
=========================

The *footstrep terrain lookup* table contains definitions for matching
footsteps with visuals and sounds.

Table structure
---------------

+------+----------------------+--------------------+-----------+-------------------------------------------+
| ID   | Name                 | Type               | Default   | Description                               |
+======+======================+====================+===========+===========================================+
| 1    | ID                   | Integer            | -         | Unique ID                                 |
+------+----------------------+--------------------+-----------+-------------------------------------------+
| 2    | creatureFootstep     | Integer            | 0         | The footstep doodad.                      |
+------+----------------------+--------------------+-----------+-------------------------------------------+
| 3    | terrainType          | Integer            | 0         | The terrain type to which this applies.   |
+------+----------------------+--------------------+-----------+-------------------------------------------+
| 4    | soundEntry           | Integer            | 0         | Sound for dry terrain.                    |
+------+----------------------+--------------------+-----------+-------------------------------------------+
| 5    | soundEntrySplash     | Integer            | 0         | Sound for wet terrain.                    |
+------+----------------------+--------------------+-----------+-------------------------------------------+

Relations
---------

-  ``creatureFootstep`` references the primary key of ``GroundEffectDoodad.dbc``.
-  ``terrainType`` references the primary key of ``TerrainType.dbc``.
-  ``soundEntry`` and ``soundEntrySplash`` reference the primary key of ``SoundEntries.dbc``.
