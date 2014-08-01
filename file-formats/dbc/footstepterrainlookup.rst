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
| 1    | ID                   | Integer (signed)   | -         | Unique ID                                 |
+------+----------------------+--------------------+-----------+-------------------------------------------+
| 2    | creatureFootstepID   | Integer (signed)   | 0         | The footstep doodad.                      |
+------+----------------------+--------------------+-----------+-------------------------------------------+
| 3    | terrainTypeID        | Integer (signed)   | 0         | The terrain type to which this applies.   |
+------+----------------------+--------------------+-----------+-------------------------------------------+
| 4    | soundEntryID         | Integer (signed)   | 0         | Sound for dry terrain.                    |
+------+----------------------+--------------------+-----------+-------------------------------------------+
| 5    | soundEntryIDSplash   | Integer (signed)   | 0         | Sound for wet terrain.                    |
+------+----------------------+--------------------+-----------+-------------------------------------------+

Relations
---------

-  ``creatureFootstepID`` references the primary key of
   ``GroundEffectDoodad.dbc``.
-  ``terrainTypeID`` references the primary key of ``TerrainType.dbc``.
-  ``soundEntryID`` and ``soundEntryIDSplash`` reference the primary key
   of ``SoundEntries.dbc``.
