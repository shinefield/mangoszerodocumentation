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
| 1    | ID              | Integer              | -         | Unique ID                       |
+------+-----------------+----------------------+-----------+---------------------------------+
| 2    | subclassMap     | Integer              | 0         | References the item subclass.   |
+------+-----------------+----------------------+-----------+---------------------------------+
| 3    | flags           | Integer (signed)     | 0         | See below.                      |
+------+-----------------+----------------------+-----------+---------------------------------+
| 4    | classname       | String (localized)   | -         | The name of the item class.     |
+------+-----------------+----------------------+-----------+---------------------------------+

Fields
------

flags
~~~~~

-  ``0``: item,
-  ``1``: weapon.

Relations
---------

-  ``subclassMap`` references the primary key of ``ItemSubClass.dbc``.
