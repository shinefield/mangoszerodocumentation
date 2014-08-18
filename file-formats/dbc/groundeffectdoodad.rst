.. _file-formats-dbc-groundeffectdoodad:

======================
GroundEffectDoodad.dbc
======================

The *ground effect doodad* table contains definitions for doodads to be placed on the ground,
specifically flower models.

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
