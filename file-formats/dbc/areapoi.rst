.. _file-formats-dbc-areapoi:

=============
AreaPOI.dbc
=============

The *area points of interest* table contains points of interest within zones. This can be global points
of interest, faction specific ones, or even PvP related points of interest

Table structure
---------------

+------+----------------+----------------------+-----------+-------------------------------------------------------------------------------+
| ID   | Name           | Type                 | Default   | Description                                                                   |
+======+================+======================+===========+===============================================================================+
| 1    | ID             | Integer              | -         | Unique ID                                                                     |
+------+----------------+----------------------+-----------+-------------------------------------------------------------------------------+
| 2    | importance     | Integer (signed)     | 0         | The importance level of the point of interest.                                |
+------+----------------+----------------------+-----------+-------------------------------------------------------------------------------+
| 3    | icon           | Integer (signed)     | 0         | Refers to an icon on the `Interface\Minimap\POIICONS` file.                   |
+------+----------------+----------------------+-----------+-------------------------------------------------------------------------------+
| 4    | faction        | Integer              | 0         | References a faction to which the POI belongs.                                |
+------+----------------+----------------------+-----------+-------------------------------------------------------------------------------+
| 5    | locationX      | Float                | 0         | X coordinate for the point of interest.                                       |
+------+----------------+----------------------+-----------+-------------------------------------------------------------------------------+
| 6    | locationY      | Float                | 0         | Y coordinate for the point of interest.                                       |
+------+----------------+----------------------+-----------+-------------------------------------------------------------------------------+
| 7    | locationZ      | Float                | 0         | Z coordinate for the point of interest.                                       |
+------+----------------+----------------------+-----------+-------------------------------------------------------------------------------+
| 8    | map            | Integer              | 0         | References a map on which this point of interest is located.                  |
+------+----------------+----------------------+-----------+-------------------------------------------------------------------------------+
| 9    | flags          | Integer (signed)     | 0         | Determines where a point of interest will be shown.                           |
+------+----------------+----------------------+-----------+-------------------------------------------------------------------------------+
| 10   | areaTable      | Integer (signed)     | 0         | References the areatable on which this point of interest is located.          |
+------+----------------+----------------------+-----------+-------------------------------------------------------------------------------+
| 11   | name           | String (localized)   | -         | The name of the point of interest.                                            |
+------+----------------+----------------------+-----------+-------------------------------------------------------------------------------+
| 12   | description    | String (localized)   | -         | A description for the point of interest.                                      |
+------+----------------+----------------------+-----------+-------------------------------------------------------------------------------+
| 13   | worldState     | Integer              | 0         | References a world state associated with the point of interest.               |
+------+----------------+----------------------+-----------+-------------------------------------------------------------------------------+

Fields
------

Relations
---------

-  ``faction`` references the primary key of :doc:`faction`.
-  ``map`` references the primary key of :doc:`map`.
-  ``areaTable`` references the primary key of :doc:`areatable`.
-  ``worldState`` references the primary key of :doc:`worldstateui`.
