.. _db-world-locales-gossip-menu-option:

=====================================
"locales\_gossip\_menu\_option" table
=====================================

The ``locales_gossip_menu_option`` table holds localized text strings
for gossip menu options.

Table structure
---------------

+----------------------+------------------------+--------+-------+-----------+---------+
| Field                | Type                   | Null   | Key   | Default   | Extra   |
+======================+========================+========+=======+===========+=========+
| menu\_id             | smallint(6) unsigned   | NO     | PRI   | 0         |         |
+----------------------+------------------------+--------+-------+-----------+---------+
| id                   | smallint(6) unsigned   | NO     | PRI   | 0         |         |
+----------------------+------------------------+--------+-------+-----------+---------+
| option\_text\_loc1   | text                   | YES    |       | NULL      |         |
+----------------------+------------------------+--------+-------+-----------+---------+
| option\_text\_loc2   | text                   | YES    |       | NULL      |         |
+----------------------+------------------------+--------+-------+-----------+---------+
| option\_text\_loc3   | text                   | YES    |       | NULL      |         |
+----------------------+------------------------+--------+-------+-----------+---------+
| option\_text\_loc4   | text                   | YES    |       | NULL      |         |
+----------------------+------------------------+--------+-------+-----------+---------+
| option\_text\_loc5   | text                   | YES    |       | NULL      |         |
+----------------------+------------------------+--------+-------+-----------+---------+
| option\_text\_loc6   | text                   | YES    |       | NULL      |         |
+----------------------+------------------------+--------+-------+-----------+---------+
| option\_text\_loc7   | text                   | YES    |       | NULL      |         |
+----------------------+------------------------+--------+-------+-----------+---------+
| option\_text\_loc8   | text                   | YES    |       | NULL      |         |
+----------------------+------------------------+--------+-------+-----------+---------+
| box\_text\_loc1      | text                   | YES    |       | NULL      |         |
+----------------------+------------------------+--------+-------+-----------+---------+
| box\_text\_loc2      | text                   | YES    |       | NULL      |         |
+----------------------+------------------------+--------+-------+-----------+---------+
| box\_text\_loc3      | text                   | YES    |       | NULL      |         |
+----------------------+------------------------+--------+-------+-----------+---------+
| box\_text\_loc4      | text                   | YES    |       | NULL      |         |
+----------------------+------------------------+--------+-------+-----------+---------+
| box\_text\_loc5      | text                   | YES    |       | NULL      |         |
+----------------------+------------------------+--------+-------+-----------+---------+
| box\_text\_loc6      | text                   | YES    |       | NULL      |         |
+----------------------+------------------------+--------+-------+-----------+---------+
| box\_text\_loc7      | text                   | YES    |       | NULL      |         |
+----------------------+------------------------+--------+-------+-----------+---------+
| box\_text\_loc8      | text                   | YES    |       | NULL      |         |
+----------------------+------------------------+--------+-------+-----------+---------+

Fields
------

menu\_id
--------

This references the `gossip\_menu\_option <gossip_menu_option>`__ tables
``menu_id`` for which the entry is valid.

id
--

option\_text\_loc1
------------------

*Korean* localization of ``option_text`` in the
`gossip\_menu\_option <gossip_menu_option>`__ table.

option\_text\_loc2
------------------

*French* localization of ``option_text`` in the
`gossip\_menu\_option <gossip_menu_option>`__ table.

option\_text\_loc3
------------------

*German* localization of ``option_text`` in the
`gossip\_menu\_option <gossip_menu_option>`__ table.

option\_text\_loc4
------------------

*Chinese* localization of ``option_text`` in the
`gossip\_menu\_option <gossip_menu_option>`__ table.

option\_text\_loc5
------------------

*Taiwanese* localization of ``option_text`` in the
`gossip\_menu\_option <gossip_menu_option>`__ table.

option\_text\_loc6
------------------

*Spanish Spain* localization of ``option_text`` in the
`gossip\_menu\_option <gossip_menu_option>`__ table.

option\_text\_loc7
------------------

*Spanish Latin America* localization of ``option_text`` in the
`gossip\_menu\_option <gossip_menu_option>`__ table.

option\_text\_loc8
------------------

*Russian* localization of ``option_text`` in the
`gossip\_menu\_option <gossip_menu_option>`__ table.

box\_text\_loc1
---------------

*Korean* localization of ``box_text`` in the
`gossip\_menu\_option <gossip_menu_option>`__ table.

box\_text\_loc2
---------------

*French* localization of ``box_text`` in the
`gossip\_menu\_option <gossip_menu_option>`__ table.

box\_text\_loc3
---------------

*German* localization of ``box_text`` in the
`gossip\_menu\_option <gossip_menu_option>`__ table.

box\_text\_loc4
---------------

*Chinese* localization of ``box_text`` in the
`gossip\_menu\_option <gossip_menu_option>`__ table.

box\_text\_loc5
---------------

*Taiwanese* localization of ``box_text`` in the
`gossip\_menu\_option <gossip_menu_option>`__ table.

box\_text\_loc6
---------------

*Spanish Spain* localization of ``box_text`` in the
`gossip\_menu\_option <gossip_menu_option>`__ table.

box\_text\_loc7
---------------

*Spanish Latin America* localization of ``box_text`` in the
`gossip\_menu\_option <gossip_menu_option>`__ table.

box\_text\_loc8
---------------

*Russian* localization of ``box_text`` in the
`gossip\_menu\_option <gossip_menu_option>`__ table.
