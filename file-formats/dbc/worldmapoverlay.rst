.. _file-formats-dbc-worldmapoverlay:

===================
WorldMapOverlay.dbc
===================

The *world map overlay* table contains definitions for texture overlays
used for a sections of an area on the world map.

Table structure
---------------

+------+------------------+--------------------+-----------+------------------------------------------+
| ID   | Name             | Type               | Default   | Description                              |
+======+==================+====================+===========+==========================================+
| 1    | ID               | Integer (signed)   | -         | Unique ID                                |
+------+------------------+--------------------+-----------+------------------------------------------+
| 2    | worldMapAreaID   | Integer (signed)   | 0         | The zone in which the overlay is used.   |
+------+------------------+--------------------+-----------+------------------------------------------+
| 3    | areaTableID1     | Integer (signed)   | 0         | **TODO**                                 |
+------+------------------+--------------------+-----------+------------------------------------------+
| 4    | areaTableID2     | Integer (signed)   | 0         | **TODO**                                 |
+------+------------------+--------------------+-----------+------------------------------------------+
| 5    | areaTableID3     | Integer (signed)   | 0         | **TODO**                                 |
+------+------------------+--------------------+-----------+------------------------------------------+
| 6    | areaTableID4     | Integer (signed)   | 0         | **TODO**                                 |
+------+------------------+--------------------+-----------+------------------------------------------+
| 7    | locationX        | Integer            | 0         | **TODO**                                 |
+------+------------------+--------------------+-----------+------------------------------------------+
| 8    | locationY        | Integer            | 0         | **TODO**                                 |
+------+------------------+--------------------+-----------+------------------------------------------+
| 9    | textureName      | String             | -         | Base texture name.                       |
+------+------------------+--------------------+-----------+------------------------------------------+
| 10   | textureWidth     | Integer            | 0         | **TODO**                                 |
+------+------------------+--------------------+-----------+------------------------------------------+
| 11   | textureHeight    | Integer            | 0         | **TODO**                                 |
+------+------------------+--------------------+-----------+------------------------------------------+
| 12   | offsetX          | Integer            | 0         | **TODO**                                 |
+------+------------------+--------------------+-----------+------------------------------------------+
| 13   | offsetY          | Integer            | 0         | **TODO**                                 |
+------+------------------+--------------------+-----------+------------------------------------------+
| 14   | hitRectTop       | Integer            | 0         | **TODO**                                 |
+------+------------------+--------------------+-----------+------------------------------------------+
| 15   | hitRectLeft      | Integer            | 0         | **TODO**                                 |
+------+------------------+--------------------+-----------+------------------------------------------+
| 16   | hitRectBottom    | Integer            | 0         | **TODO**                                 |
+------+------------------+--------------------+-----------+------------------------------------------+
| 17   | hitRectRight     | Integer            | 0         | **TODO**                                 |
+------+------------------+--------------------+-----------+------------------------------------------+

Relations
---------

-  ``worldMapAreaID`` references the primary key of
   ``WorldMapArea.dbc``.
-  ``areaTableID`` references the primary key of ``AreaTable.dbc``.

Notes
-----

Textures are placed on areas of a map, relative to its pixel size. The
texture is split in a varying number of sub-textures. Each texture can
not exceed the size of ``256x256`` pixels.

Textures are found in the world map area directory which itself resides
in the ``Interface\WorldMap`` directory. The base texture name is
suffixed with an 1-based index, and prefixed with the world map area's
name (e.g. ``Interface\WorldMap\Tirisfal\Monastery1.blp``. Here the
world map area directory is Tirisfal, the base texture name is
Monastery, with sub-texture index of 1).

The world map area (aka. zone) where the overlay is placed, is
referenced by ``worldMapAreaID``, while the corresponding area is
referenced in ``areaTableID1``.
