.. _file-formats-dbc-wepaonswingsounds2:

======================
WeaponSwingSounds2.dbc
======================

The *weapon swing sounds* table contains definitions for which sound is
played when a weapon swings.

Table structure
---------------

+------+----------------+--------------------+-----------+---------------------------------------------------+
| ID   | Name           | Type               | Default   | Description                                       |
+======+================+====================+===========+===================================================+
| 1    | ID             | Integer (signed)   | -         | Unique ID                                         |
+------+----------------+--------------------+-----------+---------------------------------------------------+
| 2    | swingType      | Integer            | 0         | The weight of the weapon used.                    |
+------+----------------+--------------------+-----------+---------------------------------------------------+
| 3    | isCritical     | Integer            | 0         | See below.                                        |
+------+----------------+--------------------+-----------+---------------------------------------------------+
| 4    | soundEntryID   | Integer (signed)   | 0         | The sound entry to be played upon weapon swing.   |
+------+----------------+--------------------+-----------+---------------------------------------------------+

Fields
------

swingType
~~~~~~~~~

-  ``0``: light. E.g. a knife.
-  ``1``: medium. E.g. 1H sword/axe.
-  ``2``: heavy. E.g. 2H sword/stave.

isCritical
~~~~~~~~~~

-  ``0``: non-critical hit
-  ``1``: critical hit

Relations
---------

-  ``soundEntryID`` references the primary key of ``SoundEntries.dbc``.
