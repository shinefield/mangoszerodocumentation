.. _file-formats-dbc-gmticketcategory:

====================
GMTicketCategory.dbc
====================

The *game master ticket category* table contains definitions for
categories in which in-game tickets can be created.

Table structure
---------------

+------+------------+----------------------+-----------+------------------------------------+
| ID   | Name       | Type                 | Default   | Description                        |
+======+============+======================+===========+====================================+
| 1    | ID         | Integer (signed)     | -         | Unique ID                          |
+------+------------+----------------------+-----------+------------------------------------+
| 2    | category   | String (localized)   | -         | The name of the ticket category.   |
+------+------------+----------------------+-----------+------------------------------------+
