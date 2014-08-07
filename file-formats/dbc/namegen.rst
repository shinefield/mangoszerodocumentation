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
| 1    | ID       | Integer            | -         | Unique ID                                   |
+------+----------+--------------------+-----------+---------------------------------------------+
| 2    | name     | String             | -         | A given random player name.                 |
+------+----------+--------------------+-----------+---------------------------------------------+
| 3    | race     | Integer            | 0         | References a race to which this applies     |
+------+----------+--------------------+-----------+---------------------------------------------+
| 4    | sex      | Integer (signed)   | 0         | References the sex to which this applies.   |
+------+----------+--------------------+-----------+---------------------------------------------+

Fields
------

sex
~~~

-  ``0``: male,
-  ``1``: female.

Relations
---------

-  ``race`` references the primary key of ``ChrRaces.dbc``.
