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
| 1    | ID                     | Integer            | -         | Unique ID                                          |
+------+------------------------+--------------------+-----------+----------------------------------------------------+
| 2    | itemVisualEffects1     | Integer            | 0         | References the item enchantment visual to apply.   |
+------+------------------------+--------------------+-----------+----------------------------------------------------+
| 3    | itemVisualEffects2     | Integer            | 0         | References the item enchantment visual to apply.   |
+------+------------------------+--------------------+-----------+----------------------------------------------------+
| 4    | itemVisualEffects3     | Integer            | 0         | References the item enchantment visual to apply.   |
+------+------------------------+--------------------+-----------+----------------------------------------------------+
| 5    | itemVisualEffects4     | Integer            | 0         | References the item enchantment visual to apply.   |
+------+------------------------+--------------------+-----------+----------------------------------------------------+
| 6    | itemVisualEffects5     | Integer            | 0         | References the item enchantment visual to apply.   |
+------+------------------------+--------------------+-----------+----------------------------------------------------+

Relations
---------

-  ``itemVisualEffects[1-5]`` references the primary key of :doc:`itemvisualeffects`.
