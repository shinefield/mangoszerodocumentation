.. _file-formats-dbc-cinematicsequences:

======================
CinematicSequences.dbc
======================

The *cinematic sequences* table contains definitions for chaining of
cinematic cameras.

Table structure
---------------

+------+----------------------+--------------------+-----------+------------------------------------------------+
| ID   | Name                 | Type               | Default   | Description                                    |
+======+======================+====================+===========+================================================+
| 1    | ID                   | Integer (signed)   | -         | Unique ID                                      |
+------+----------------------+--------------------+-----------+------------------------------------------------+
| 2    | soundEntryID         | Integer (signed)   | 0         | A sound entry to be played for the sequence.   |
+------+----------------------+--------------------+-----------+------------------------------------------------+
| 3    | cinematicCameraID1   | Integer (signed)   | 0         | A camera to be used in the sequence.           |
+------+----------------------+--------------------+-----------+------------------------------------------------+
| 4    | cinematicCameraID2   | Integer (signed)   | 0         | A camera to be used in the sequence.           |
+------+----------------------+--------------------+-----------+------------------------------------------------+
| 5    | cinematicCameraID3   | Integer (signed)   | 0         | A camera to be used in the sequence.           |
+------+----------------------+--------------------+-----------+------------------------------------------------+
| 6    | cinematicCameraID4   | Integer (signed)   | 0         | A camera to be used in the sequence.           |
+------+----------------------+--------------------+-----------+------------------------------------------------+
| 7    | cinematicCameraID5   | Integer (signed)   | 0         | A camera to be used in the sequence.           |
+------+----------------------+--------------------+-----------+------------------------------------------------+
| 8    | cinematicCameraID6   | Integer (signed)   | 0         | A camera to be used in the sequence.           |
+------+----------------------+--------------------+-----------+------------------------------------------------+
| 9    | cinematicCameraID7   | Integer (signed)   | 0         | A camera to be used in the sequence.           |
+------+----------------------+--------------------+-----------+------------------------------------------------+
| 10   | cinematicCameraID8   | Integer (signed)   | 0         | A camera to be used in the sequence.           |
+------+----------------------+--------------------+-----------+------------------------------------------------+

Relations
---------

-  ``soundEntryID`` references the primary key of ``SoundEntries.dbc``.
-  ``cinematicCameraID[1-8]`` references the primary key of
   ``CinematicCamera.dbc``.

