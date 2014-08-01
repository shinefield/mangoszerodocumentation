.. _file-formats-dbc-sheathesoundlookups:

=======================
SheatheSoundLookups.dbc
=======================

The *sheathe sound lookups* table contains definitions for which sound
to play when sheathing items.

Table structure
---------------

+------+--------------------+--------------------+-----------+-----------------------------------------------------------+
| ID   | Name               | Type               | Default   | Description                                               |
+======+====================+====================+===========+===========================================================+
| 1    | ID                 | Integer (signed)   | -         | Unique ID                                                 |
+------+--------------------+--------------------+-----------+-----------------------------------------------------------+
| 2    | itemClass          | Integer (signed)   | 0         | The item class to which the sound applies.                |
+------+--------------------+--------------------+-----------+-----------------------------------------------------------+
| 3    | itemSubclass       | Integer (signed)   | 0         | The items subclass to which the sound applies.            |
+------+--------------------+--------------------+-----------+-----------------------------------------------------------+
| 4    | itemEnvTypes       | Integer            | 0         | See below.                                                |
+------+--------------------+--------------------+-----------+-----------------------------------------------------------+
| 5    | isShield           | Integer            | 0         | See below.                                                |
+------+--------------------+--------------------+-----------+-----------------------------------------------------------+
| 6    | sheathSoundID      | Integer (signed)   | 0         | The sound entry to be played when sheathing the item.     |
+------+--------------------+--------------------+-----------+-----------------------------------------------------------+
| 7    | undsheathSoundID   | Integer (signed)   | 0         | The sound entry to be played when unsheathing the item.   |
+------+--------------------+--------------------+-----------+-----------------------------------------------------------+

Fields
------

itemEnvTypes
------------

-  ``0``: shield,
-  ``1``: metal weapon,
-  ``2``: wood weapon.

isShield
--------

-  ``0``: a shield,
-  ``1``: not a shield.

Relations
---------

-  ``itemClass`` references the primary key of ``ItemClass.dbc``.
-  ``itemSubclass`` references the primary key of ``ItemSubClass.dbc``.
-  ``sheathSoundID`` and ``sheathSoundID`` reference the primary key of
   ``SoundEntries.dbc``.

