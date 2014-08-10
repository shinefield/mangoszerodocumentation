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
| 1    | ID            | Integer            | -         | Unique ID                                         |
+------+---------------+--------------------+-----------+---------------------------------------------------+
| 2    | race          | Integer            | 0         | References the race to which the style applies.   |
+------+---------------+--------------------+-----------+---------------------------------------------------+
| 3    | sex           | Integer (signed)   | 0         | See below.                                        |
+------+---------------+--------------------+-----------+---------------------------------------------------+
| 4    | variation     | Integer            | 0         | References the actual style to apply.             |
+------+---------------+--------------------+-----------+---------------------------------------------------+
| 5    | geoset        | Integer (signed)   | 0         | References a geoset ID in a model.                |
+------+---------------+--------------------+-----------+---------------------------------------------------+
| 6    | showScalp     | Integer (signed)   | 0         | See below.                                        |
+------+---------------+--------------------+-----------+---------------------------------------------------+

Fields
------

sex
~~~

-  ``0``: male,
-  ``1``: female.

showScalp
~~~~~~~~~

-  ``0``: not bald,
-  ``1``: bald.

Relations
---------

-  ``race`` references the primary key of :doc:`chrraces`.
-  ``variation`` references the primary key of :doc:`charvariations`.
