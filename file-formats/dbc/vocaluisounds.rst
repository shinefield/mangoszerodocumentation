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
| 1    | ID                         | Integer            | -         | Unique ID       |
+------+----------------------------+--------------------+-----------+-----------------+
| 2    | vocalUIEnum                | Integer (signed)   | 0         | **TODO**        |
+------+----------------------------+--------------------+-----------+-----------------+
| 3    | race                       | Integer            | 0         | The race.       |
+------+----------------------------+--------------------+-----------+-----------------+
| 4    | normalMaleSoundEntry       | Integer (signed)   | 0         | Male sound.     |
+------+----------------------------+--------------------+-----------+-----------------+
| 5    | normalFemaleSoundEntry     | Integer (signed)   | 0         | Female sound.   |
+------+----------------------------+--------------------+-----------+-----------------+
| 6    | pissedMaleSoundEntry       | Integer (signed)   | 0         | Male sound.     |
+------+----------------------------+--------------------+-----------+-----------------+
| 7    | pissedFemaleSoundEntry     | Integer (signed)   | 0         | Female sound.   |
+------+----------------------------+--------------------+-----------+-----------------+

Relations
---------

-  ``race`` references the primary key of :doc:`chrraces`.
-  ``normalMaleSoundEntry``, ``normalFemaleSoundEntry``,
   ``pissedMaleSoundEntry`` and ``pissedFemaleSoundEntry`` reference
   the primary key of :doc:`soundentries`.
