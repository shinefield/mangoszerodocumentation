.. _file-formats-dbc-emotestextsound:

===================
EmotesTextSound.dbc
===================

The *emotes text sound* table contains definitions for which sound
entries are connected to which emote text.

Table structure
---------------

+------+----------------+--------------------+-----------+-----------------------------------------------+
| ID   | Name           | Type               | Default   | Description                                   |
+======+================+====================+===========+===============================================+
| 1    | ID             | Integer (signed)   | -         | Unique ID                                     |
+------+----------------+--------------------+-----------+-----------------------------------------------+
| 2    | emotesTextID   | Integer (signed)   | 0         | The emotes text to which the sound applies.   |
+------+----------------+--------------------+-----------+-----------------------------------------------+
| 3    | raceID         | Integer (signed)   | 0         | The race to which the emote sound applies.    |
+------+----------------+--------------------+-----------+-----------------------------------------------+
| 4    | sexID          | Integer            | 0         | See below.                                    |
+------+----------------+--------------------+-----------+-----------------------------------------------+
| 5    | soundID        | Integer (signed)   | 0         | The sound to be played.                       |
+------+----------------+--------------------+-----------+-----------------------------------------------+

Fields
------

sexID
~~~~~

-  ``0``: male,
-  ``1``: female.

Relations
---------

-  ``emotesTextID`` references the primary key of ``EmotesText.dbc``.
-  ``raceID`` references the primary key of ``ChrRaces.dbc``.
-  ``soundID`` references the primary key of ``SoundEntries.dbc``.
