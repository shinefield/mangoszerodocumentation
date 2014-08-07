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
| 1    | ID             | Integer            | -         | Unique ID                                     |
+------+----------------+--------------------+-----------+-----------------------------------------------+
| 2    | emotesText     | Integer            | 0         | The emotes text to which the sound applies.   |
+------+----------------+--------------------+-----------+-----------------------------------------------+
| 3    | race           | Integer            | 0         | The race to which the emote sound applies.    |
+------+----------------+--------------------+-----------+-----------------------------------------------+
| 4    | sex            | Integer (signed)   | 0         | See below.                                    |
+------+----------------+--------------------+-----------+-----------------------------------------------+
| 5    | sound          | Integer            | 0         | The sound to be played.                       |
+------+----------------+--------------------+-----------+-----------------------------------------------+

Fields
------

sex
~~~

-  ``0``: male,
-  ``1``: female.

Relations
---------

-  ``emotesText`` references the primary key of ``EmotesText.dbc``.
-  ``race`` references the primary key of ``ChrRaces.dbc``.
-  ``sound`` references the primary key of ``SoundEntries.dbc``.
