.. _file-formats-dbc-itemsubclassmask:

====================
ItemSubClassMask.dbc
====================

The *item sub class mask* table contains definitions for grouping
weapons and armour into sub classes.

Table structure
---------------

+------+------------------+----------------------+-----------+-------------------------+
| ID   | Name             | Type                 | Default   | Description             |
+======+==================+======================+===========+=========================+
| 1    | ID               | Integer (signed)     | -         | Unique ID               |
+------+------------------+----------------------+-----------+-------------------------+
| 2    | itemSubClassID   | Integer (signed)     | 0         | Sub class ID.           |
+------+------------------+----------------------+-----------+-------------------------+
| 3    | name             | String (localized)   | -         | The name of the mask.   |
+------+------------------+----------------------+-----------+-------------------------+

Relations
---------

-  ``itemSubClassID`` references the key ``subClassID`` of
   ``ItemSubClass.dbc``.
