.. _file-formats-dbc-weapinimpactsounds:

======================
WeaponImpactSounds.dbc
======================

The *weapon impact sounds* table contains definitions for which sound is
played when a weapon hits.

Table structure
---------------

+------+--------------------+--------------------+-----------+---------------------------------------------------+
| ID   | Name               | Type               | Default   | Description                                       |
+======+====================+====================+===========+===================================================+
| 1    | ID                 | Integer (signed)   | -         | Unique ID                                         |
+------+--------------------+--------------------+-----------+---------------------------------------------------+
| 2    | weaponSubclassID   | Integer            | 0         | **TODO**                                          |
+------+--------------------+--------------------+-----------+---------------------------------------------------+
| 3    | parrySoundType     | Integer            | 0         | **TODO**                                          |
+------+--------------------+--------------------+-----------+---------------------------------------------------+
| 4    | impactSound        | Integer (signed)   | 0         | The sound entry to be played upon weapon swing.   |
+------+--------------------+--------------------+-----------+---------------------------------------------------+
| 5    | impactSound        | Integer (signed)   | 0         | The sound entry to be played upon weapon swing.   |
+------+--------------------+--------------------+-----------+---------------------------------------------------+
| 6    | impactSound        | Integer (signed)   | 0         | The sound entry to be played upon weapon swing.   |
+------+--------------------+--------------------+-----------+---------------------------------------------------+
| 7    | impactSound        | Integer (signed)   | 0         | The sound entry to be played upon weapon swing.   |
+------+--------------------+--------------------+-----------+---------------------------------------------------+
| 8    | impactSound        | Integer (signed)   | 0         | The sound entry to be played upon weapon swing.   |
+------+--------------------+--------------------+-----------+---------------------------------------------------+
| 9    | impactSound        | Integer (signed)   | 0         | The sound entry to be played upon weapon swing.   |
+------+--------------------+--------------------+-----------+---------------------------------------------------+
| 10   | impactSound        | Integer (signed)   | 0         | The sound entry to be played upon weapon swing.   |
+------+--------------------+--------------------+-----------+---------------------------------------------------+
| 11   | impactSound        | Integer (signed)   | 0         | The sound entry to be played upon weapon swing.   |
+------+--------------------+--------------------+-----------+---------------------------------------------------+
| 12   | impactSound        | Integer (signed)   | 0         | The sound entry to be played upon weapon swing.   |
+------+--------------------+--------------------+-----------+---------------------------------------------------+
| 13   | impactSound        | Integer (signed)   | 0         | The sound entry to be played upon weapon swing.   |
+------+--------------------+--------------------+-----------+---------------------------------------------------+
| 14   | criticalSound      | Integer (signed)   | 0         | The sound entry to be played upon weapon swing.   |
+------+--------------------+--------------------+-----------+---------------------------------------------------+
| 15   | criticalSound      | Integer (signed)   | 0         | The sound entry to be played upon weapon swing.   |
+------+--------------------+--------------------+-----------+---------------------------------------------------+
| 16   | criticalSound      | Integer (signed)   | 0         | The sound entry to be played upon weapon swing.   |
+------+--------------------+--------------------+-----------+---------------------------------------------------+
| 17   | criticalSound      | Integer (signed)   | 0         | The sound entry to be played upon weapon swing.   |
+------+--------------------+--------------------+-----------+---------------------------------------------------+
| 18   | criticalSound      | Integer (signed)   | 0         | The sound entry to be played upon weapon swing.   |
+------+--------------------+--------------------+-----------+---------------------------------------------------+
| 19   | criticalSound      | Integer (signed)   | 0         | The sound entry to be played upon weapon swing.   |
+------+--------------------+--------------------+-----------+---------------------------------------------------+
| 20   | criticalSound      | Integer (signed)   | 0         | The sound entry to be played upon weapon swing.   |
+------+--------------------+--------------------+-----------+---------------------------------------------------+
| 21   | criticalSound      | Integer (signed)   | 0         | The sound entry to be played upon weapon swing.   |
+------+--------------------+--------------------+-----------+---------------------------------------------------+
| 22   | criticalSound      | Integer (signed)   | 0         | The sound entry to be played upon weapon swing.   |
+------+--------------------+--------------------+-----------+---------------------------------------------------+
| 23   | criticalSound      | Integer (signed)   | 0         | The sound entry to be played upon weapon swing.   |
+------+--------------------+--------------------+-----------+---------------------------------------------------+

Relations
---------

-  ``impactSound[1-10]`` references the primary key of
   ``SoundEntries.dbc``.
-  ``criticalSound[1-10]`` references the primary key of
   ``SoundEntries.dbc``.

Notes
-----

Impact and critical sounds have multiple entries, and it is not yet
known which purpose these serve.
