.. _file-formats-dbc-itemgroupsounds:

===================
ItemGroupSounds.dbc
===================

The *item group sounds* table contains definitions for groups of sounds
that are used for items.

Table structure
---------------

+------+-----------------+--------------------+-----------+-----------------------------------------+
| ID   | Name            | Type               | Default   | Description                             |
+======+=================+====================+===========+=========================================+
| 1    | ID              | Integer            | -         | Unique ID                               |
+------+-----------------+--------------------+-----------+-----------------------------------------+
| 2    | soundEntry1     | Integer            | 0         | Sound to play when item is picked up.   |
+------+-----------------+--------------------+-----------+-----------------------------------------+
| 3    | soundEntry2     | Integer            | 0         | Sound to play when item is put down.    |
+------+-----------------+--------------------+-----------+-----------------------------------------+
| 4    | soundEntry3     | Integer            | 0         | **TODO**                                |
+------+-----------------+--------------------+-----------+-----------------------------------------+
| 5    | soundEntry4     | Integer            | 0         | **TODO**                                |
+------+-----------------+--------------------+-----------+-----------------------------------------+

Relations
---------

-  ``soundEntry[1-4]`` reference the primary key of ``SoundEntries.dbc``.
