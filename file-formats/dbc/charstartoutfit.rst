.. _file-formats-dbc-charstartoutfit:

===================
CharStartOutfit.dbc
===================

The *character start outfit* table contains definitions for the items a
new character should receive.

Table structure
---------------

+------+-----------+--------------------+-----------+-----------------------------------------------------+
| ID   | Name      | Type               | Default   | Description                                         |
+======+===========+====================+===========+=====================================================+
| 1    | ID        | Integer (signed)   | -         | Unique ID                                           |
+------+-----------+--------------------+-----------+-----------------------------------------------------+
| 2    | RaceID    | Byte (signed)      | 0         | References the race to which the outfit applies.    |
+------+-----------+--------------------+-----------+-----------------------------------------------------+
| 3    | ClassID   | Byte (signed)      | 0         | References the class to which the outfit applies.   |
+------+-----------+--------------------+-----------+-----------------------------------------------------+
| 4    | sexID     | Byte               | 0         | See below.                                          |
+------+-----------+--------------------+-----------+-----------------------------------------------------+
| 5    | flag      | Byte               | 0         | **TODO**                                            |
+------+-----------+--------------------+-----------+-----------------------------------------------------+

Fields
------

sexID
-----

-  ``0``: male,
-  ``1``: female.

flag
----

**TODO**

Relations
---------

-  ``RaceID`` references the primary key of ``ChrRaces.dbc``.
-  ``ClassID`` references the primary key of ``ChrClasses.dbc``.

