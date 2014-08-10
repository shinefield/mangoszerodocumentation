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
| 1    | ID              | Integer            | -         | Unique ID                                  |
+------+-----------------+--------------------+-----------+--------------------------------------------+
| 2    | soundEntry1     | Integer (signed)   | 0         | References the sound entry to be played.   |
+------+-----------------+--------------------+-----------+--------------------------------------------+
| 3    | soundEntry2     | Integer (signed)   | 0         | References the sound entry to be played.   |
+------+-----------------+--------------------+-----------+--------------------------------------------+
| 4    | soundEntry3     | Integer (signed)   | 0         | References the sound entry to be played.   |
+------+-----------------+--------------------+-----------+--------------------------------------------+
| 5    | soundEntry4     | Integer (signed)   | 0         | References the sound entry to be played.   |
+------+-----------------+--------------------+-----------+--------------------------------------------+

Relations
---------

-  ``soundEntry[1-4]`` reference the primary key of :doc:`soundentries`.
