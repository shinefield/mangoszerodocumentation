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
| 1    | ID                        | Integer (signed)     | -         | Unique ID                                           |
+------+---------------------------+----------------------+-----------+-----------------------------------------------------+
| 2    | name                      | String               | -         | The name of the enchantment.                        |
+------+---------------------------+----------------------+-----------+-----------------------------------------------------+
| 3    | spellItemEnchantmentID1   | Integer (signed)     | 0         | References an item enchantment for this property.   |
+------+---------------------------+----------------------+-----------+-----------------------------------------------------+
| 4    | spellItemEnchantmentID2   | Integer (signed)     | 0         | References an item enchantment for this property.   |
+------+---------------------------+----------------------+-----------+-----------------------------------------------------+
| 5    | spellItemEnchantmentID3   | Integer (signed)     | 0         | References an item enchantment for this property.   |
+------+---------------------------+----------------------+-----------+-----------------------------------------------------+
| 6    | spellItemEnchantmentID4   | Integer (signed)     | 0         | References an item enchantment for this property.   |
+------+---------------------------+----------------------+-----------+-----------------------------------------------------+
| 7    | spellItemEnchantmentID5   | Integer (signed)     | 0         | References an item enchantment for this property.   |
+------+---------------------------+----------------------+-----------+-----------------------------------------------------+
| 8    | suffix                    | String (localized)   | -         | The enchantment suffix displayed in-game.           |
+------+---------------------------+----------------------+-----------+-----------------------------------------------------+

Relations
---------

-  ``spellItemEnchantmentID[1-5]`` references the primary key of
   ``SpellItemEnchantment.dbc``.
