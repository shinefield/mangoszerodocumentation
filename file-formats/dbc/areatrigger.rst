.. _file-formats-dbc-areatrigger:

===============
AreaTrigger.dbc
===============

The *area trigger* table contains definitions for locations which are supposed to trigger
in-game server side events. Usually these are scripted events.

Table structure
---------------

+------+-------------+--------------------+-----------+-----------------------------------------------------+
| ID   | Name        | Type               | Default   | Description                                         |
+======+=============+====================+===========+=====================================================+
| 1    | ID          | Integer            | -         | Unique ID                                           |
+------+-------------+--------------------+-----------+-----------------------------------------------------+
| 2    | map         | Integer            | 0         | The map on which the area is located.               |
+------+-------------+--------------------+-----------+-----------------------------------------------------+
| 3    | locationX   | Float              | 0         | X coordinate for the trigger.                       |
+------+-------------+--------------------+-----------+-----------------------------------------------------+
| 4    | locationY   | Float              | 0         | Y coordinate for the trigger.                       |
+------+-------------+--------------------+-----------+-----------------------------------------------------+
| 5    | locationZ   | Float              | 0         | Z coordinate for the trigger.                       |
+------+-------------+--------------------+-----------+-----------------------------------------------------+
| 6    | radius      | Float              | 0         | Box size of the area trigger.                       |
+------+-------------+--------------------+-----------+-----------------------------------------------------+
| 7    | boxLength   | Float              | 0         | Length of the box if no radius is specified.        |
+------+-------------+--------------------+-----------+-----------------------------------------------------+
| 8    | boxWidth    | Float              | 0         | Width of the box if no radius is specified.         |
+------+-------------+--------------------+-----------+-----------------------------------------------------+
| 9    | boxHeight   | Float              | 0         | Height of the box if no radius is specified.        |
+------+-------------+--------------------+-----------+-----------------------------------------------------+
| 10   | boxYaw      | Float              | 0         | Orientation of the box if no radius is specified.   |
+------+-------------+--------------------+-----------+-----------------------------------------------------+

Relations
---------

-  ``map`` references the primary key of :doc:`map`.
