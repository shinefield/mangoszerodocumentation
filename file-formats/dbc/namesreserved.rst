.. _file-formats-dbc-namesreserved:

=================
NamesReserved.dbc
=================

The *names reserved* table contains definitions for characters names
which are reserved for creatures, or unavailable due to being a real
persons name.

Table structure
---------------

+------+--------+--------------------+-----------+----------------------------------------+
| ID   | Name   | Type               | Default   | Description                            |
+======+========+====================+===========+========================================+
| 1    | ID     | Integer (signed)   | -         | Unique ID                              |
+------+--------+--------------------+-----------+----------------------------------------+
| 2    | name   | String             | -         | The name or a name pattern reserved.   |
+------+--------+--------------------+-----------+----------------------------------------+

