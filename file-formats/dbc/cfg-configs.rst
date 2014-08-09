.. _file-formats-dbc-cfg-configs:

================
Cfg\_Configs.dbc
================

The *configuration* table contains definitions for realm types and their
rules.

Table structure
---------------

+------+------------------------+--------------------+-----------+-------------------------------------+
| ID   | Name                   | Type               | Default   | Description                         |
+======+========================+====================+===========+=====================================+
| 1    | ID                     | Integer            | -         | Unique ID                           |
+------+------------------------+--------------------+-----------+-------------------------------------+
| 2    | realmType              | Integer (signed)   | 0         | Type of the realm.                  |
+------+------------------------+--------------------+-----------+-------------------------------------+
| 3    | playerKillingAllowed   | Integer (signed)   | 0         | Determines if this is a PvP realm.  |
+------+------------------------+--------------------+-----------+-------------------------------------+
| 4    | rolePlaying            | Integer (signed)   | 0         | Determines if this is a RP realm.   |
+------+------------------------+--------------------+-----------+-------------------------------------+

Fields
------

playerKillingAllowed
~~~~~~~~~~~~~~~~~~~~

-  ``0``: no,
-  ``1``: yes.

rolePlaying
~~~~~~~~~~~

-  ``0``: no,
-  ``1``: yes.
