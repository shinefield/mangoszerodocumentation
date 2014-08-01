.. _file-formats-dbc-charvariations:

==================
CharVariations.dbc
==================

The *character variations* table contains definitions for character
models, and seems to indicate where models vary from the default model.

Currently it is assumed that the masks indicated the display of foot
items, or required modification of head items due to tusks, or horns
since these masks are only set for Tauren and Trolls.

Table structure
---------------

+------+----------+--------------------+-----------+--------------------------------------------------------+
| ID   | Name     | Type               | Default   | Description                                            |
+======+==========+====================+===========+========================================================+
| 1    | RaceID   | Integer (signed)   | 0         | References the race to which to apply the variation.   |
+------+----------+--------------------+-----------+--------------------------------------------------------+
| 2    | sexID    | Integer            | 0         | See below.                                             |
+------+----------+--------------------+-----------+--------------------------------------------------------+
| 3    | unk1     | Integer            | 0         | **TODO**                                               |
+------+----------+--------------------+-----------+--------------------------------------------------------+
| 4    | mask1    | Integer            | 0         | **TODO**                                               |
+------+----------+--------------------+-----------+--------------------------------------------------------+
| 5    | mask2    | Integer            | 0         | **TODO**                                               |
+------+----------+--------------------+-----------+--------------------------------------------------------+
| 6    | unk4     | Integer            | 0         | **TODO**                                               |
+------+----------+--------------------+-----------+--------------------------------------------------------+

Fields
------

sexID
~~~~~

-  ``0``: male,
-  ``1``: female.

unk1
~~~~

**TODO**

mask1
~~~~~

-  ``512``: seems to indicate feet/head variations.

mask2
~~~~~

-  ``512``: seems to indicate feet/head variations.

unk4
~~~~

**TODO**

Relations
---------

-  ``RaceID`` references the primary key of ``ChrRaces.dbc``.

Notes
-----

This table does not have a primary key. It only covers playable races.
