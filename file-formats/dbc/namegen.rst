.. _file-formats-dbc-namegen:

===========
NameGen.dbc
===========

The *name gen* table contains definitions for random names for
characters.

Table structure
---------------

+------+----------+--------------------+-----------+---------------------------------------------+
| ID   | Name     | Type               | Default   | Description                                 |
+======+==========+====================+===========+=============================================+
| 1    | ID       | Integer (signed)   | -         | Unique ID                                   |
+------+----------+--------------------+-----------+---------------------------------------------+
| 2    | name     | String             | -         | A given random player name.                 |
+------+----------+--------------------+-----------+---------------------------------------------+
| 3    | raceID   | Integer (signed)   | 0         | References a race to which this applies     |
+------+----------+--------------------+-----------+---------------------------------------------+
| 4    | sexID    | Integer            | 0         | References the sex to which this applies.   |
+------+----------+--------------------+-----------+---------------------------------------------+

Fields
------

sexID
~~~~~

-  ``0``: male,
-  ``1``: female.

Relations
---------

-  ``raceID`` references the primary key of ``ChrRaces.dbc``.
