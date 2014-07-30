.. _db-world-locales-item:

=====================
"locales\_item" table
=====================

The ``locales_item`` table holds localized text strings for item
templates.

Table structure
---------------

+---------------------+-------------------------+--------+-------+-----------+---------+
| Field               | Type                    | Null   | Key   | Default   | Extra   |
+=====================+=========================+========+=======+===========+=========+
| entry               | mediumint(8) unsigned   | NO     | PRI   | 0         |         |
+---------------------+-------------------------+--------+-------+-----------+---------+
| name\_loc1          | varchar(100)            | NO     |       |           |         |
+---------------------+-------------------------+--------+-------+-----------+---------+
| name\_loc2          | varchar(100)            | NO     |       |           |         |
+---------------------+-------------------------+--------+-------+-----------+---------+
| name\_loc3          | varchar(100)            | NO     |       |           |         |
+---------------------+-------------------------+--------+-------+-----------+---------+
| name\_loc4          | varchar(100)            | NO     |       |           |         |
+---------------------+-------------------------+--------+-------+-----------+---------+
| name\_loc5          | varchar(100)            | NO     |       |           |         |
+---------------------+-------------------------+--------+-------+-----------+---------+
| name\_loc6          | varchar(100)            | NO     |       |           |         |
+---------------------+-------------------------+--------+-------+-----------+---------+
| name\_loc7          | varchar(100)            | NO     |       |           |         |
+---------------------+-------------------------+--------+-------+-----------+---------+
| name\_loc8          | varchar(100)            | NO     |       |           |         |
+---------------------+-------------------------+--------+-------+-----------+---------+
| description\_loc1   | varchar(255)            | YES    |       | NULL      |         |
+---------------------+-------------------------+--------+-------+-----------+---------+
| description\_loc2   | varchar(255)            | YES    |       | NULL      |         |
+---------------------+-------------------------+--------+-------+-----------+---------+
| description\_loc3   | varchar(255)            | YES    |       | NULL      |         |
+---------------------+-------------------------+--------+-------+-----------+---------+
| description\_loc4   | varchar(255)            | YES    |       | NULL      |         |
+---------------------+-------------------------+--------+-------+-----------+---------+
| description\_loc5   | varchar(255)            | YES    |       | NULL      |         |
+---------------------+-------------------------+--------+-------+-----------+---------+
| description\_loc6   | varchar(255)            | YES    |       | NULL      |         |
+---------------------+-------------------------+--------+-------+-----------+---------+
| description\_loc7   | varchar(255)            | YES    |       | NULL      |         |
+---------------------+-------------------------+--------+-------+-----------+---------+
| description\_loc8   | varchar(255)            | YES    |       | NULL      |         |
+---------------------+-------------------------+--------+-------+-----------+---------+

Fields
------

entry
-----

This references the `item\_template <item_template>`__ tables unique ID
for which the entry is valid.

name\_loc1
----------

*Korean* localization of ``name`` in the
`item\_template <item_template>`__ table.

name\_loc2
----------

*French* localization of ``name`` in the
`item\_template <item_template>`__ table.

name\_loc3
----------

*German* localization of ``name`` in the
`item\_template <item_template>`__ table.

name\_loc4
----------

*Chinese* localization of ``name`` in the
`item\_template <item_template>`__ table.

name\_loc5
----------

*Taiwanese* localization of ``name`` in the
`item\_template <item_template>`__ table.

name\_loc6
----------

*Spanish Spain* localization of ``name`` in the
`item\_template <item_template>`__ table.

name\_loc7
----------

*Spanish Latin America* localization of ``name`` in the
`item\_template <item_template>`__ table.

name\_loc8
----------

*Russian* localization of ``name`` in the
`item\_template <item_template>`__ table.

description\_loc1
-----------------

*Korean* localization of ``description`` in the
`item\_template <item_template>`__ table.

description\_loc2
-----------------

*French* localization of ``description`` in the
`item\_template <item_template>`__ table.

description\_loc3
-----------------

*German* localization of ``description`` in the
`item\_template <item_template>`__ table.

description\_loc4
-----------------

*Chinese* localization of ``description`` in the
`item\_template <item_template>`__ table.

description\_loc5
-----------------

*Taiwanese* localization of ``description`` in the
`item\_template <item_template>`__ table.

description\_loc6
-----------------

*Spanish Spain* localization of ``description`` in the
`item\_template <item_template>`__ table.

description\_loc7
-----------------

*Spanish Latin America* localization of ``description`` in the
`item\_template <item_template>`__ table.

description\_loc8
-----------------

*Russian* localization of ``description`` in the
`item\_template <item_template>`__ table.
