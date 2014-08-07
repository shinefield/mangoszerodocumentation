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
| 1    | ID        | Integer            | -         | Unique ID                                           |
+------+-----------+--------------------+-----------+-----------------------------------------------------+
| 2    | race      | Byte               | 0         | References the race to which the outfit applies.    |
+------+-----------+--------------------+-----------+-----------------------------------------------------+
| 3    | class     | Byte               | 0         | References the class to which the outfit applies.   |
+------+-----------+--------------------+-----------+-----------------------------------------------------+
| 4    | sex       | Byte (signed)      | 0         | See below.                                          |
+------+-----------+--------------------+-----------+-----------------------------------------------------+
| 5    | flag      | Byte (signed)      | 0         | **TODO**                                            |
+------+-----------+--------------------+-----------+-----------------------------------------------------+

Fields
------

sex
~~~

-  ``0``: male,
-  ``1``: female.

flag
~~~~

**TODO**

Relations
---------

-  ``race`` references the primary key of ``ChrRaces.dbc``.
-  ``class`` references the primary key of ``ChrClasses.dbc``.
