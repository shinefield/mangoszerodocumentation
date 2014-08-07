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
| 1    | ID                 | Integer            | -         | Unique ID                                         |
+------+--------------------+--------------------+-----------+---------------------------------------------------+
| 2    | weaponSubclass     | Integer (signed)   | 0         | **TODO**                                          |
+------+--------------------+--------------------+-----------+---------------------------------------------------+
| 3    | parrySoundType     | Integer (signed)   | 0         | **TODO**                                          |
+------+--------------------+--------------------+-----------+---------------------------------------------------+
| 4    | impactSound        | Integer            | 0         | The sound entry to be played upon weapon swing.   |
+------+--------------------+--------------------+-----------+---------------------------------------------------+
| 5    | impactSound        | Integer            | 0         | The sound entry to be played upon weapon swing.   |
+------+--------------------+--------------------+-----------+---------------------------------------------------+
| 6    | impactSound        | Integer            | 0         | The sound entry to be played upon weapon swing.   |
+------+--------------------+--------------------+-----------+---------------------------------------------------+
| 7    | impactSound        | Integer            | 0         | The sound entry to be played upon weapon swing.   |
+------+--------------------+--------------------+-----------+---------------------------------------------------+
| 8    | impactSound        | Integer            | 0         | The sound entry to be played upon weapon swing.   |
+------+--------------------+--------------------+-----------+---------------------------------------------------+
| 9    | impactSound        | Integer            | 0         | The sound entry to be played upon weapon swing.   |
+------+--------------------+--------------------+-----------+---------------------------------------------------+
| 10   | impactSound        | Integer            | 0         | The sound entry to be played upon weapon swing.   |
+------+--------------------+--------------------+-----------+---------------------------------------------------+
| 11   | impactSound        | Integer            | 0         | The sound entry to be played upon weapon swing.   |
+------+--------------------+--------------------+-----------+---------------------------------------------------+
| 12   | impactSound        | Integer            | 0         | The sound entry to be played upon weapon swing.   |
+------+--------------------+--------------------+-----------+---------------------------------------------------+
| 13   | impactSound        | Integer            | 0         | The sound entry to be played upon weapon swing.   |
+------+--------------------+--------------------+-----------+---------------------------------------------------+
| 14   | critImpactSound    | Integer            | 0         | The sound entry to be played upon weapon swing.   |
+------+--------------------+--------------------+-----------+---------------------------------------------------+
| 15   | critImpactSound    | Integer            | 0         | The sound entry to be played upon weapon swing.   |
+------+--------------------+--------------------+-----------+---------------------------------------------------+
| 16   | critImpactSound    | Integer            | 0         | The sound entry to be played upon weapon swing.   |
+------+--------------------+--------------------+-----------+---------------------------------------------------+
| 17   | critImpactSound    | Integer            | 0         | The sound entry to be played upon weapon swing.   |
+------+--------------------+--------------------+-----------+---------------------------------------------------+
| 18   | critImpactSound    | Integer            | 0         | The sound entry to be played upon weapon swing.   |
+------+--------------------+--------------------+-----------+---------------------------------------------------+
| 19   | critImpactSound    | Integer            | 0         | The sound entry to be played upon weapon swing.   |
+------+--------------------+--------------------+-----------+---------------------------------------------------+
| 20   | critImpactSound    | Integer            | 0         | The sound entry to be played upon weapon swing.   |
+------+--------------------+--------------------+-----------+---------------------------------------------------+
| 21   | critImpactSound    | Integer            | 0         | The sound entry to be played upon weapon swing.   |
+------+--------------------+--------------------+-----------+---------------------------------------------------+
| 22   | critImpactSound    | Integer            | 0         | The sound entry to be played upon weapon swing.   |
+------+--------------------+--------------------+-----------+---------------------------------------------------+
| 23   | critImpactSound    | Integer            | 0         | The sound entry to be played upon weapon swing.   |
+------+--------------------+--------------------+-----------+---------------------------------------------------+

Relations
---------

-  ``impactSound[1-10]`` references the primary key of ``SoundEntries.dbc``.
-  ``critImpactSound[1-10]`` references the primary key of ``SoundEntries.dbc``.

Notes
-----

Impact and critical sounds have multiple entries, and it is not yet
known which purpose these serve.
