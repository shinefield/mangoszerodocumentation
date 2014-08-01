.. _file-formats-dbc-charbaseinfo:

================
CharBaseInfo.dbc
================

The *character base information* table contains definitions for which
race may create what character classes.

Table structure
---------------

+------+-----------+--------------------+-----------+---------------------------------------+
| ID   | Name      | Type               | Default   | Description                           |
+======+===========+====================+===========+=======================================+
| 1    | raceID    | Integer (signed)   | 0         | References the race which is used.    |
+------+-----------+--------------------+-----------+---------------------------------------+
| 2    | classID   | Integer (signed)   | 0         | References the class which is used.   |
+------+-----------+--------------------+-----------+---------------------------------------+

Relations
---------

-  ``raceID`` references the primary key of ``ChrRaces.dbc``.
-  ``classID`` references the primary key of ``ChrClasses.dbc``.

Notes
-----

This table does not have a primary key.
