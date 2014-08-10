.. _file-formats-dbc-itemrandomproperties:

========================
ItemRandomProperties.dbc
========================

The *item random properties* table contains definitions for enchants
assigned to items.

Table structure
---------------

+------+---------------------------+----------------------+-----------+-----------------------------------------------------+
| ID   | Name                      | Type                 | Default   | Description                                         |
+======+===========================+======================+===========+=====================================================+
| 1    | ID                        | Integer              | -         | Unique ID                                           |
+------+---------------------------+----------------------+-----------+-----------------------------------------------------+
| 2    | name                      | String               | -         | The name of the enchantment.                        |
+------+---------------------------+----------------------+-----------+-----------------------------------------------------+
| 3    | spellItemEnchantment1     | Integer              | 0         | References an item enchantment for this property.   |
+------+---------------------------+----------------------+-----------+-----------------------------------------------------+
| 4    | spellItemEnchantment2     | Integer              | 0         | References an item enchantment for this property.   |
+------+---------------------------+----------------------+-----------+-----------------------------------------------------+
| 5    | spellItemEnchantment3     | Integer              | 0         | References an item enchantment for this property.   |
+------+---------------------------+----------------------+-----------+-----------------------------------------------------+
| 6    | spellItemEnchantment4     | Integer              | 0         | References an item enchantment for this property.   |
+------+---------------------------+----------------------+-----------+-----------------------------------------------------+
| 7    | spellItemEnchantment5     | Integer              | 0         | References an item enchantment for this property.   |
+------+---------------------------+----------------------+-----------+-----------------------------------------------------+
| 8    | suffix                    | String (localized)   | -         | The enchantment suffix displayed in-game.           |
+------+---------------------------+----------------------+-----------+-----------------------------------------------------+

Relations
---------

-  ``spellItemEnchantment[1-5]`` references the primary key of :doc:`spellitemenchantment`.
