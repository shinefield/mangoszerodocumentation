.. _file-formats-dbc-charhairgeosets:

===================
CharHairGeosets.dbc
===================

The *character hair geosets* table contains definitions for allowed hair
styles for races/genders.

Table structure
---------------

+------+---------------+--------------------+-----------+---------------------------------------------------+
| ID   | Name          | Type               | Default   | Description                                       |
+======+===============+====================+===========+===================================================+
| 1    | ID            | Integer (signed)   | -         | Unique ID                                         |
+------+---------------+--------------------+-----------+---------------------------------------------------+
| 2    | raceID        | Integer (signed)   | 0         | References the race to which the style applies.   |
+------+---------------+--------------------+-----------+---------------------------------------------------+
| 3    | sexID         | Integer            | 0         | See below.                                        |
+------+---------------+--------------------+-----------+---------------------------------------------------+
| 4    | variationID   | Integer (signed)   | 0         | References the actual style to apply.             |
+------+---------------+--------------------+-----------+---------------------------------------------------+
| 5    | geosetID      | Integer            | 0         | References a geoset ID in a model.                |
+------+---------------+--------------------+-----------+---------------------------------------------------+
| 6    | showScalp     | Integer            | 0         | See below.                                        |
+------+---------------+--------------------+-----------+---------------------------------------------------+

Fields
------

sexID
-----

-  ``0``: male,
-  ``1``: female.

showScalp
---------

-  ``0``: not bald,
-  ``1``: bald.

Relations
---------

-  ``raceID`` references the primary key of ``ChrRaces.dbc``.
-  ``variationID`` references the primary key of ``CharVariations.dbc``.

