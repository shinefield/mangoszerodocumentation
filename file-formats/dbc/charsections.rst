.. _file-formats-dbc-charsections:

================
CharSections.dbc
================

The *character sections* table contains definitions for textures that
make up the different character variations, e.g. hair, beards, the base
skin.

Table structure
---------------

+------+------------------+--------------------+-----------+-----------------------------------------------------+
| ID   | Name             | Type               | Default   | Description                                         |
+======+==================+====================+===========+=====================================================+
| 1    | ID               | Integer (signed)   | -         | Unique ID                                           |
+------+------------------+--------------------+-----------+-----------------------------------------------------+
| 2    | raceID           | Integer (signed)   | 0         | References the race to which the section applies.   |
+------+------------------+--------------------+-----------+-----------------------------------------------------+
| 3    | sexID            | Integer            | 0         | See below.                                          |
+------+------------------+--------------------+-----------+-----------------------------------------------------+
| 4    | sectionType      | Integer            | 0         | See below.                                          |
+------+------------------+--------------------+-----------+-----------------------------------------------------+
| 5    | variationIndex   | Integer            | 0         | **TODO**                                            |
+------+------------------+--------------------+-----------+-----------------------------------------------------+
| 6    | colorIndex       | Integer            | 0         | An index                                            |
+------+------------------+--------------------+-----------+-----------------------------------------------------+
| 7    | textureName1     | String             | -         | The name of the matching texture file.              |
+------+------------------+--------------------+-----------+-----------------------------------------------------+
| 8    | textureName2     | String             | -         | The name of the matching texture file.              |
+------+------------------+--------------------+-----------+-----------------------------------------------------+
| 9    | textureName3     | String             | -         | The name of the matching texture file.              |
+------+------------------+--------------------+-----------+-----------------------------------------------------+
| 10   | flags            | Integer            | 0         | See below.                                          |
+------+------------------+--------------------+-----------+-----------------------------------------------------+

Fields
------

sexID
-----

-  ``0``: male,
-  ``1``: female.

sectionType
-----------

Each ``sectionType`` value indicates a different use case for the fields
``colorIndex``, ``TextureName1``, ``TextureName2`` and ``TextureName3``.

-  ``0``: *base skin* indicates that ``colorIndex`` points to a *skin
   colour*, ``TextureName1`` points to a *skin texture*,
   ``TextureName2`` points to *extra skin* and ``TextureName3`` is
   empty.
-  ``1``: *face* indicates that ``colorIndex`` points to a *skin
   colour*, ``TextureName1`` points to a *face texture*,
   ``TextureName2`` points to an *upper face texture* and
   ``TextureName3`` is empty.
-  ``2``: *facial hair* indicates that ``colorIndex`` points to a *hair
   colour*, ``TextureName1`` points to a *facial hair texture*,
   ``TextureName2`` points to an *upper face texture* and
   ``TextureName3`` points to *nothing*.
-  ``3``: *hair* indicates that ``colorIndex`` points to a *hair
   colour*, ``TextureName1`` points to a *hair texture*,
   ``TextureName2`` points to a *lower scalp texture* and
   ``TextureName3`` points to an *upper scalp texture*.
-  ``4``: *underwear* indicates that ``colorIndex`` points to a *skin
   colour*, ``TextureName1`` points to a *underwear texture*,
   ``TextureName2`` points to a *torso texture* and ``TextureName3`` is
   empty.

flags
-----

This indicates if an entry is valid for a player character. Currently
only entries for *Goblins* are marked as non-playable.

-  ``0``: section for playable races,
-  ``1``: section for non-playable races.

Relations
---------

-  ``raceID`` references the primary key of ``ChrRaces.dbc``.

