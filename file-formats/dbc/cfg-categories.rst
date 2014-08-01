.. _file-formats-dbc-cfg-categories:

===================
Cfg\_Categories.dbc
===================

The *configuration categories* table contains definitions for grouping
realms in the realm selection dialogue.

Table structure
---------------

+------+----------+----------------------+-----------+--------------------------------------------+
| ID   | Name     | Type                 | Default   | Description                                |
+======+==========+======================+===========+============================================+
| 1    | tab      | Integer              | 0         | The tab on the realm selection dialogue.   |
+------+----------+----------------------+-----------+--------------------------------------------+
| 2    | region   | Integer              | 0         | The region's ID.                           |
+------+----------+----------------------+-----------+--------------------------------------------+
| 3    | name     | String (localized)   | -         | The name of the realm group.               |
+------+----------+----------------------+-----------+--------------------------------------------+

Notes
-----

This table does not have a primary key.
