.. _file-formats-dbc-itemclass:

=============
ItemClass.dbc
=============

The *item class* table contains definitions for available item classes.

Table structure
---------------

+------+-----------------+----------------------+-----------+---------------------------------+
| ID   | Name            | Type                 | Default   | Description                     |
+======+=================+======================+===========+=================================+
| 1    | ID              | Integer (signed)     | -         | Unique ID                       |
+------+-----------------+----------------------+-----------+---------------------------------+
| 2    | subclassMapID   | Integer (signed)     | 0         | References the item subclass.   |
+------+-----------------+----------------------+-----------+---------------------------------+
| 3    | flags           | Integer              | 0         | See below.                      |
+------+-----------------+----------------------+-----------+---------------------------------+
| 4    | classname       | String (localized)   | -         | The name of the item class.     |
+------+-----------------+----------------------+-----------+---------------------------------+

Fields
------

flags
-----

-  ``0``: item,
-  ``1``: weapon.

Relations
---------

-  ``subclassMapID`` references the primary key of ``ItemSubClass.dbc``.

