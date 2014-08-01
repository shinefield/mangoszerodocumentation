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
| 1    | ID              | Integer (signed)   | -         | Unique ID                               |
+------+-----------------+--------------------+-----------+-----------------------------------------+
| 2    | soundEntryID1   | Integer (signed)   | 0         | Sound to play when item is picked up.   |
+------+-----------------+--------------------+-----------+-----------------------------------------+
| 3    | soundEntryID2   | Integer (signed)   | 0         | Sound to play when item is put down.    |
+------+-----------------+--------------------+-----------+-----------------------------------------+
| 4    | soundEntryID3   | Integer (signed)   | 0         | **TODO**                                |
+------+-----------------+--------------------+-----------+-----------------------------------------+
| 5    | soundEntryID4   | Integer (signed)   | 0         | **TODO**                                |
+------+-----------------+--------------------+-----------+-----------------------------------------+

Relations
---------

-  ``soundEntryID[1-4]`` reference the primary key of
   ``SoundEntries.dbc``.

