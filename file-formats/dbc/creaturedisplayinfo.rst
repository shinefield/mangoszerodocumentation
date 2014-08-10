.. _file-formats-dbc-creaturedisplayinfo:

=======================
CreatureDisplayInfo.dbc
=======================

The *creature display information* table contains definitions for
textures, scales, models and other data required to display a creature.

Table structure
---------------

+------+-------------------------+--------------------+-----------+--------------------------------------------------------------+
| ID   | Name                    | Type               | Default   | Description                                                  |
+======+=========================+====================+===========+==============================================================+
| 1    | ID                      | Integer            | -         | Unique ID                                                    |
+------+-------------------------+--------------------+-----------+--------------------------------------------------------------+
| 2    | model                   | Integer            | 0         | References a display model.                                  |
+------+-------------------------+--------------------+-----------+--------------------------------------------------------------+
| 3    | sound                   | Integer            | 0         | References a sound entry.                                    |
+------+-------------------------+--------------------+-----------+--------------------------------------------------------------+
| 4    | extendedDisplayInfo     | Integer            | 0         | References an extra display model.                           |
+------+-------------------------+--------------------+-----------+--------------------------------------------------------------+
| 5    | creatureModelScale      | Float              | 1         | Default scale, if not set by server. 1 is the normal size.   |
+------+-------------------------+--------------------+-----------+--------------------------------------------------------------+
| 5    | creatureModelAlpha      | Integer (signed)   | 255       | 0 (transparent) to 255 (opaque).                             |
+------+-------------------------+--------------------+-----------+--------------------------------------------------------------+
| 6    | textureVariation1       | String             | -         | Skin used in the model.                                      |
+------+-------------------------+--------------------+-----------+--------------------------------------------------------------+
| 7    | textureVariation2       | String             | -         | Skin used in the model.                                      |
+------+-------------------------+--------------------+-----------+--------------------------------------------------------------+
| 8    | textureVariation3       | String             | -         | Skin used in the model.                                      |
+------+-------------------------+--------------------+-----------+--------------------------------------------------------------+
| 9    | sizeClass               | Integer (signed)   | 0         | See below.                                                   |
+------+-------------------------+--------------------+-----------+--------------------------------------------------------------+
| 10   | blood                   | Integer            | 0         | Blood effect to be used for the NPC.                         |
+------+-------------------------+--------------------+-----------+--------------------------------------------------------------+
| 11   | NPCSound                | Integer            | 0,        | Sounds used when interacting with the NPC.                   |
+------+-------------------------+--------------------+-----------+--------------------------------------------------------------+

Fields
------

sizeClass
~~~~~~~~~

-  ``0``: small,
-  ``1``: medium,
-  ``2``: large,
-  ``3``: giant,
-  ``4``: colossal.

Relations
---------

-  ``model`` references the primary key of :doc:`creaturemodeldata`.
-  ``sound`` references the primary key of :doc:`creaturesounddata`.
-  ``extendedDisplayInfo`` references the primary key of :doc:`creaturedisplayinfoextra`.
-  ``blood`` references the primary key of :doc:`unitblood`.
-  ``NPCSound`` references the primary key of :doc:`npcsounds`.
