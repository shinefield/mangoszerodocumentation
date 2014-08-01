.. _file-formats-dbc-vocaluisounds:

=================
VocalUISounds.dbc
=================

The *vocal UI sounds* table contains definitions for UI error sounds for
all the different races and genders.

Table structure
---------------

+------+----------------------------+--------------------+-----------+-----------------+
| ID   | Name                       | Type               | Default   | Description     |
+======+============================+====================+===========+=================+
| 1    | ID                         | Integer (signed)   | -         | Unique ID       |
+------+----------------------------+--------------------+-----------+-----------------+
| 2    | vocalUIEnum                | Integer            | 0         | **TODO**        |
+------+----------------------------+--------------------+-----------+-----------------+
| 3    | raceID                     | Integer (signed)   | 0         | The race.       |
+------+----------------------------+--------------------+-----------+-----------------+
| 4    | normalMaleSoundEntryID     | Integer (signed)   | 0         | Male sound.     |
+------+----------------------------+--------------------+-----------+-----------------+
| 5    | normalFemaleSoundEntryID   | Integer (signed)   | 0         | Female sound.   |
+------+----------------------------+--------------------+-----------+-----------------+
| 6    | pissedMaleSoundEntryID     | Integer (signed)   | 0         | Male sound.     |
+------+----------------------------+--------------------+-----------+-----------------+
| 7    | pissedFemaleSoundEntryID   | Integer (signed)   | 0         | Female sound.   |
+------+----------------------------+--------------------+-----------+-----------------+

Relations
---------

-  ``raceID`` references the primary key of ``ChrRaces.dbc``.
-  ``normalMaleSoundEntryID``, ``normalFemaleSoundEntryID``,
   ``pissedMaleSoundEntryID`` and ``pissedFemaleSoundEntryID`` reference
   the primary key of ``SoundEntries.dbc``.
