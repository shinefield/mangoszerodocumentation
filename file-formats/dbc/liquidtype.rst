.. _file-formats-dbc-liquidtype:

==============
LiquidType.dbc
==============

The *liquid type* table contains definitions for which effects liquid
types should have.

Table structure
---------------

+------+-----------+---------------------+-----------+------------------------------------------------------------------------------+
| ID   | Name      | Type                | Default   | Description                                                                  |
+======+===========+=====================+===========+==============================================================================+
| 1    | ID        | Integer             | -         | Unique ID                                                                    |
+------+-----------+---------------------+-----------+------------------------------------------------------------------------------+
| 2    | name      | String              | -         | The name of the liquid type.                                                 |
+------+-----------+---------------------+-----------+------------------------------------------------------------------------------+
| 3    | type      | Integer (signed)    | 0         | See below.                                                                   |
+------+-----------+---------------------+-----------+------------------------------------------------------------------------------+
| 4    | spell     | Integer             | 0         | The spell to be cast when a character is on contact with this liquid type.   |
+------+-----------+---------------------+-----------+------------------------------------------------------------------------------+

Fields
------

type
~~~~

-  ``0``: fire,
-  ``2``: slime,
-  ``4``: water.

Relations
---------

-  ``spell`` references the primary key of :doc:`spell`.

Notes
-----

The liquid type table has specifically been introduced for the Naxxramas
raid zone to account for the slime which has an effect on the characters
in it, unlike normal slime liquid.
