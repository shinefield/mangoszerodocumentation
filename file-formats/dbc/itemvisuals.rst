.. _file-formats-dbc-itemvisuals:

===============
ItemVisuals.dbc
===============

The *item visuals* table contains definitions for sets of item
enchantment effects.

Table structure
---------------

+------+------------------------+--------------------+-----------+----------------------------------------------------+
| ID   | Name                   | Type               | Default   | Description                                        |
+======+========================+====================+===========+====================================================+
| 1    | ID                     | Integer (signed)   | -         | Unique ID                                          |
+------+------------------------+--------------------+-----------+----------------------------------------------------+
| 2    | itemVisualEffectsID1   | Integer (signed)   | 0         | References the item enchantment visual to apply.   |
+------+------------------------+--------------------+-----------+----------------------------------------------------+
| 3    | itemVisualEffectsID2   | Integer (signed)   | 0         | References the item enchantment visual to apply.   |
+------+------------------------+--------------------+-----------+----------------------------------------------------+
| 4    | itemVisualEffectsID3   | Integer (signed)   | 0         | References the item enchantment visual to apply.   |
+------+------------------------+--------------------+-----------+----------------------------------------------------+
| 5    | itemVisualEffectsID4   | Integer (signed)   | 0         | References the item enchantment visual to apply.   |
+------+------------------------+--------------------+-----------+----------------------------------------------------+
| 6    | itemVisualEffectsID5   | Integer (signed)   | 0         | References the item enchantment visual to apply.   |
+------+------------------------+--------------------+-----------+----------------------------------------------------+

Relations
---------

-  ``itemVisualEffectsID[1-5]`` references the primary key of
   ``ItemVisualEffects.dbc``.
