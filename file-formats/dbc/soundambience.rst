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
| 1    | ID                  | Integer            | -         | Unique ID                       |
+------+---------------------+--------------------+-----------+---------------------------------+
| 2    | daySoundEntry       | Integer            | 0         | Sound ambience for the day.     |
+------+---------------------+--------------------+-----------+---------------------------------+
| 3    | nightSoundEntry     | Integer            | 0         | Ambience sound for the night.   |
+------+---------------------+--------------------+-----------+---------------------------------+

Relations
---------

-  ``daySoundEntry`` and ``nightSoundEntry`` reference the primary key of :doc:`soundentries`.
