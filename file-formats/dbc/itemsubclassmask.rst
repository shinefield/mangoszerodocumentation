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
| 1    | subClass         | Integer              | -         | Unique ID               |
+------+------------------+----------------------+-----------+-------------------------+
| 2    | mask             | Integer (signed)     | 0         | Sub class ID.           |
+------+------------------+----------------------+-----------+-------------------------+
| 3    | name             | String (localized)   | -         | The name of the mask.   |
+------+------------------+----------------------+-----------+-------------------------+

Relations
---------

-  ``subClass`` references the key ``subClass`` of :doc:`itemsubclass`.
