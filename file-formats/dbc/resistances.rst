.. _file-formats-dbc-resistances:

===============
Resistances.dbc
===============

The *resistances* table contains definitions for available resistance
types.

Table structure
---------------

+------+----------------------+----------------------+-----------+---------------------------------+
| ID   | Name                 | Type                 | Default   | Description                     |
+======+======================+======================+===========+=================================+
| 1    | ID                   | Integer              | -         | Unique ID                       |
+------+----------------------+----------------------+-----------+---------------------------------+
| 2    | flags                | Integer (signed)     | 0         | See below.                      |
+------+----------------------+----------------------+-----------+---------------------------------+
| 3    | fizzleSoundEntry     | Integer              | 0         | The sound entry to be played.   |
+------+----------------------+----------------------+-----------+---------------------------------+
| 4    | name                 | String (localized)   | -         | The name of the resistance.     |
+------+----------------------+----------------------+-----------+---------------------------------+

Fields
------

flags
~~~~~

-  ``0``: non-physical damage,
-  ``1``: physical damage

Relations
---------

-  ``fizzleSoundEntry`` references the primary key of :doc:`soundentries`.
