.. _file-formats-dbc-worldsafelocs:

=================
WorldSafeLocs.dbc
=================

The *world safe location* table contains specifies coordinates where
graveyards are located.

Table structure
---------------

+------+-------------+----------------------+-----------+-----------------------------------------------+
| ID   | Name        | Type                 | Default   | Description                                   |
+======+=============+======================+===========+===============================================+
| 1    | ID          | Integer              | -         | Unique ID                                     |
+------+-------------+----------------------+-----------+-----------------------------------------------+
| 2    | map         | Integer              | -         | The map on which the graveyard is located.    |
+------+-------------+----------------------+-----------+-----------------------------------------------+
| 3    | locationX   | Float                | 0         | X coordinate of the graveyard in the world.   |
+------+-------------+----------------------+-----------+-----------------------------------------------+
| 4    | locationY   | Float                | 0         | Y coordinate of the graveyard in the world.   |
+------+-------------+----------------------+-----------+-----------------------------------------------+
| 5    | locationZ   | Float                | 0         | Z coordinate of the graveyard in the world.   |
+------+-------------+----------------------+-----------+-----------------------------------------------+
| 6    | areaName    | String (localized)   | -         | The name of the graveyard location.           |
+------+-------------+----------------------+-----------+-----------------------------------------------+

Relations
---------

-  ``map`` references the primary key of ``Map.dbc``.
