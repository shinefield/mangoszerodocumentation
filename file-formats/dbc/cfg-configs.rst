.. _file-formats-dbc-cfg-configs:

================
Cfg\_Configs.dbc
================

The *configuration* table contains definitions for realm types and their
rules.

Table structure
---------------

+------+------------------------+--------------------+-----------+---------------------+
| ID   | Name                   | Type               | Default   | Description         |
+======+========================+====================+===========+=====================+
| 1    | ID                     | Integer (signed)   | -         | Unique ID           |
+------+------------------------+--------------------+-----------+---------------------+
| 2    | realmType              | Integer            | 0         | Type of the realm   |
+------+------------------------+--------------------+-----------+---------------------+
| 3    | playerKillingAllowed   | Integer            | 0         | See below.          |
+------+------------------------+--------------------+-----------+---------------------+
| 4    | roleplaying            | Integer            | 0         | See below.          |
+------+------------------------+--------------------+-----------+---------------------+

Fields
------

playerKillingAllowed
~~~~~~~~~~~~~~~~~~~~

-  ``0``: no,
-  ``1``: yes.

roleplaying
~~~~~~~~~~~

-  ``0``: no,
-  ``1``: yes.
