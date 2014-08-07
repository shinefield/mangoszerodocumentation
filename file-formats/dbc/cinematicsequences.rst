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
| 1    | ID                   | Integer            | -         | Unique ID                                      |
+------+----------------------+--------------------+-----------+------------------------------------------------+
| 2    | soundEntry           | Integer            | 0         | A sound entry to be played for the sequence.   |
+------+----------------------+--------------------+-----------+------------------------------------------------+
| 3    | cinematicCamera1     | Integer            | 0         | A camera to be used in the sequence.           |
+------+----------------------+--------------------+-----------+------------------------------------------------+
| 4    | cinematicCamera2     | Integer            | 0         | A camera to be used in the sequence.           |
+------+----------------------+--------------------+-----------+------------------------------------------------+
| 5    | cinematicCamera3     | Integer            | 0         | A camera to be used in the sequence.           |
+------+----------------------+--------------------+-----------+------------------------------------------------+
| 6    | cinematicCamera4     | Integer            | 0         | A camera to be used in the sequence.           |
+------+----------------------+--------------------+-----------+------------------------------------------------+
| 7    | cinematicCamera5     | Integer            | 0         | A camera to be used in the sequence.           |
+------+----------------------+--------------------+-----------+------------------------------------------------+
| 8    | cinematicCamera6     | Integer            | 0         | A camera to be used in the sequence.           |
+------+----------------------+--------------------+-----------+------------------------------------------------+
| 9    | cinematicCamera7     | Integer            | 0         | A camera to be used in the sequence.           |
+------+----------------------+--------------------+-----------+------------------------------------------------+
| 10   | cinematicCamera8     | Integer            | 0         | A camera to be used in the sequence.           |
+------+----------------------+--------------------+-----------+------------------------------------------------+

Relations
---------

-  ``soundEntry`` references the primary key of ``SoundEntries.dbc``.
-  ``cinematicCamera[1-8]`` references the primary key of ``CinematicCamera.dbc``.
