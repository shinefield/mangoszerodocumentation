.. _db-world-locales-point-of-interest:

=====================================
"locales\_points\_of\_interest" table
=====================================

The ``locales_points_of_interest`` table holds localized text strings
for points of interest.

Table structure
---------------

+--------------------+-------------------------+--------+-------+-----------+---------+
| Field              | Type                    | Null   | Key   | Default   | Extra   |
+====================+=========================+========+=======+===========+=========+
| entry              | mediumint(8) unsigned   | NO     | PRI   | 0         |         |
+--------------------+-------------------------+--------+-------+-----------+---------+
| icon\_name\_loc1   | text                    | YES    |       | NULL      |         |
+--------------------+-------------------------+--------+-------+-----------+---------+
| icon\_name\_loc2   | text                    | YES    |       | NULL      |         |
+--------------------+-------------------------+--------+-------+-----------+---------+
| icon\_name\_loc3   | text                    | YES    |       | NULL      |         |
+--------------------+-------------------------+--------+-------+-----------+---------+
| icon\_name\_loc4   | text                    | YES    |       | NULL      |         |
+--------------------+-------------------------+--------+-------+-----------+---------+
| icon\_name\_loc5   | text                    | YES    |       | NULL      |         |
+--------------------+-------------------------+--------+-------+-----------+---------+
| icon\_name\_loc6   | text                    | YES    |       | NULL      |         |
+--------------------+-------------------------+--------+-------+-----------+---------+
| icon\_name\_loc7   | text                    | YES    |       | NULL      |         |
+--------------------+-------------------------+--------+-------+-----------+---------+
| icon\_name\_loc8   | text                    | YES    |       | NULL      |         |
+--------------------+-------------------------+--------+-------+-----------+---------+

Fields
------

entry
-----

This references the `points\_of\_interest <points_of_interest>`__ tables
unique ID for which the entry is valid.

icon\_name\_loc1
----------------

*Korean* localization of ``icon_name`` in the
`points\_of\_interest <points_of_interest>`__ table.

icon\_name\_loc2
----------------

*French* localization of ``icon_name`` in the
`points\_of\_interest <points_of_interest>`__ table.

icon\_name\_loc3
----------------

*German* localization of ``icon_name`` in the
`points\_of\_interest <points_of_interest>`__ table.

icon\_name\_loc4
----------------

*Chinese* localization of ``icon_name`` in the
`points\_of\_interest <points_of_interest>`__ table.

icon\_name\_loc5
----------------

*Taiwanese* localization of ``icon_name`` in the
`points\_of\_interest <points_of_interest>`__ table.

icon\_name\_loc6
----------------

*Spanish Spain* localization of ``icon_name`` in the
`points\_of\_interest <points_of_interest>`__ table.

icon\_name\_loc7
----------------

*Spanish Latin America* localization of ``icon_name`` in the
`points\_of\_interest <points_of_interest>`__ table.

icon\_name\_loc8
----------------

*Russian* localization of ``icon_name`` in the
`points\_of\_interest <points_of_interest>`__ table.
