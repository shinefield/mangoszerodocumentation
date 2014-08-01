.. _file-formats-dbc-npcsounds:

=============
NPCSounds.dbc
=============

The *non-player creature sounds* table contains definitions for which
sounds a creature will make upon being clicked.

Table structure
---------------

+------+-----------------+--------------------+-----------+--------------------------------------------+
| ID   | Name            | Type               | Default   | Description                                |
+======+=================+====================+===========+============================================+
| 1    | ID              | Integer (signed)   | -         | Unique ID                                  |
+------+-----------------+--------------------+-----------+--------------------------------------------+
| 2    | soundEntryID1   | Integer (signed)   | 0         | References the sound entry to be played.   |
+------+-----------------+--------------------+-----------+--------------------------------------------+
| 3    | soundEntryID2   | Integer (signed)   | 0         | References the sound entry to be played.   |
+------+-----------------+--------------------+-----------+--------------------------------------------+
| 4    | soundEntryID3   | Integer (signed)   | 0         | References the sound entry to be played.   |
+------+-----------------+--------------------+-----------+--------------------------------------------+
| 5    | soundEntryID4   | Integer (signed)   | 0         | References the sound entry to be played.   |
+------+-----------------+--------------------+-----------+--------------------------------------------+

Relations
---------

-  ``soundEntryID[1-4]`` reference the primary key of
   ``SoundEntries.dbc``.
