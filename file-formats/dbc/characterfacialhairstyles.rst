.. _file-formats-dbc-characterfacialhairstyles:

=============================
CharacterFacialHairStyles.dbc
=============================

The *character facial hair styles* table contains definitions for
attributes use to customize a characters facial style.

Table structure
---------------

+------+---------------+--------------------+-----------+----------------------------------------------------+
| ID   | Name          | Type               | Default   | Description                                        |
+======+===============+====================+===========+====================================================+
| 1    | raceID        | Integer (signed)   | 0         | References the race for which the style applies.   |
+------+---------------+--------------------+-----------+----------------------------------------------------+
| 2    | sexID         | Integer            | 0         | See below.                                         |
+------+---------------+--------------------+-----------+----------------------------------------------------+
| 3    | variationID   | Integer (signed)   | 0         | References the the actual variation to apply.      |
+------+---------------+--------------------+-----------+----------------------------------------------------+
| 4    | geoset1       | Integer            | 0         | References a geoset ID in a model.                 |
+------+---------------+--------------------+-----------+----------------------------------------------------+
| 5    | geoset2       | Integer            | 0         | References a geoset ID in a model.                 |
+------+---------------+--------------------+-----------+----------------------------------------------------+
| 6    | geoset3       | Integer            | 0         | References a geoset ID in a model.                 |
+------+---------------+--------------------+-----------+----------------------------------------------------+
| 7    | geoset4       | Integer            | 0         | References a geoset ID in a model.                 |
+------+---------------+--------------------+-----------+----------------------------------------------------+
| 8    | geoset5       | Integer            | 0         | References a geoset ID in a model.                 |
+------+---------------+--------------------+-----------+----------------------------------------------------+
| 9    | geoset6       | Integer            | 0         | References a geoset ID in a model.                 |
+------+---------------+--------------------+-----------+----------------------------------------------------+

Fields
------

sexID
~~~~~

-  ``0``: male,
-  ``1``: female.

Relations
---------

-  ``raceID`` references the primary key of ``ChrRaces.dbc``.
-  ``variationID`` references the primary key of ``CharVariations.dbc``.

Notes
-----

This table does not have a primary key.
