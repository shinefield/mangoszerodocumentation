.. _file-formats-dbc-soundambience:

=================
SoundAmbience.dbc
=================

The *sound ambience* table contains definitions for day and night
ambience sounds.

Table structure
---------------

+------+---------------------+--------------------+-----------+---------------------------------+
| ID   | Name                | Type               | Default   | Description                     |
+======+=====================+====================+===========+=================================+
| 1    | ID                  | Integer (signed)   | -         | Unique ID                       |
+------+---------------------+--------------------+-----------+---------------------------------+
| 2    | daySoundEntryID     | Integer (signed)   | 0         | Sound ambience for the day.     |
+------+---------------------+--------------------+-----------+---------------------------------+
| 3    | nightSoundEntryID   | Integer (signed)   | 0         | Ambience sound for the night.   |
+------+---------------------+--------------------+-----------+---------------------------------+

Relations
---------

-  ``daySoundEntryID`` and ``nightSoundEntryID`` reference the primary
   key of ``SoundEntries.dbc``.

