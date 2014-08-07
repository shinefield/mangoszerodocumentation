.. _file-formats-dbc-groundeffectdoodad:

======================
GroundEffectDoodad.dbc
======================

The *ground effect doodad* table contains definitions for use-able game
objects placed on the ground.

Table structure
---------------

+------+--------------+--------------------+-----------+---------------------------------+
| ID   | Name         | Type               | Default   | Description                     |
+======+==============+====================+===========+=================================+
| 1    | ID           | Integer            | -         | Unique ID                       |
+------+--------------+--------------------+-----------+---------------------------------+
| 2    | internalID   | Integer (signed)   | 0         | Internal ID.                    |
+------+--------------+--------------------+-----------+---------------------------------+
| 3    | doodadPath   | String             | -         | The path to the doodad model.   |
+------+--------------+--------------------+-----------+---------------------------------+
