.. _file-formats-dbc-questsort:

=============
QuestSort.dbc
=============

The *quest sort* table contains definitions for quest categories.
Entries from ``AreaTable.dbc`` may also be used as quest categories.

Table structure
---------------

+------+------------+----------------------+-----------+-----------------------------------+
| ID   | Name       | Type                 | Default   | Description                       |
+======+============+======================+===========+===================================+
| 1    | ID         | Integer (signed)     | -         | Unique ID                         |
+------+------------+----------------------+-----------+-----------------------------------+
| 2    | sortName   | String (localized)   | -         | The name of the quest category.   |
+------+------------+----------------------+-----------+-----------------------------------+

