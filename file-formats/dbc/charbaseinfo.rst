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
| 1    | race      | Integer            | 0         | References the race which is used.    |
+------+-----------+--------------------+-----------+---------------------------------------+
| 2    | class     | Integer            | 0         | References the class which is used.   |
+------+-----------+--------------------+-----------+---------------------------------------+

Relations
---------

-  ``race`` references the primary key of :doc:`chrraces`.
-  ``class`` references the primary key of :doc:`chrclasses`.

Notes
-----

This table does not have a primary key.
