.. _db-world-locales-gameobject:

===========================
"locales\_gameobject" table
===========================

The ``locales_gameobject`` table holds localized text strings for game
object templates.

Table structure
---------------

+--------------+-------------------------+--------+-------+-----------+---------+
| Field        | Type                    | Null   | Key   | Default   | Extra   |
+==============+=========================+========+=======+===========+=========+
| entry        | mediumint(8) unsigned   | NO     | PRI   | 0         |         |
+--------------+-------------------------+--------+-------+-----------+---------+
| name\_loc1   | varchar(100)            | NO     |       |           |         |
+--------------+-------------------------+--------+-------+-----------+---------+
| name\_loc2   | varchar(100)            | NO     |       |           |         |
+--------------+-------------------------+--------+-------+-----------+---------+
| name\_loc3   | varchar(100)            | NO     |       |           |         |
+--------------+-------------------------+--------+-------+-----------+---------+
| name\_loc4   | varchar(100)            | NO     |       |           |         |
+--------------+-------------------------+--------+-------+-----------+---------+
| name\_loc5   | varchar(100)            | NO     |       |           |         |
+--------------+-------------------------+--------+-------+-----------+---------+
| name\_loc6   | varchar(100)            | NO     |       |           |         |
+--------------+-------------------------+--------+-------+-----------+---------+
| name\_loc7   | varchar(100)            | NO     |       |           |         |
+--------------+-------------------------+--------+-------+-----------+---------+
| name\_loc8   | varchar(100)            | NO     |       |           |         |
+--------------+-------------------------+--------+-------+-----------+---------+

Fields
------

entry
-----

This references the `gameobject\_template <gameobject_template>`__
tables unique ID for which the entry is valid.

name\_loc1
----------

*Korean* localization of ``name`` in the
`gameobject\_template <gameobject_template>`__ table.

name\_loc2
----------

*French* localization of ``name`` in the
`gameobject\_template <gameobject_template>`__ table.

name\_loc3
----------

*German* localization of ``name`` in the
`gameobject\_template <gameobject_template>`__ table.

name\_loc4
----------

*Chinese* localization of ``name`` in the
`gameobject\_template <gameobject_template>`__ table.

name\_loc5
----------

*Taiwanese* localization of ``name`` in the
`gameobject\_template <gameobject_template>`__ table.

name\_loc6
----------

*Spanish Spain* localization of ``name`` in the
`gameobject\_template <gameobject_template>`__ table.

name\_loc7
----------

*Spanish Latin America* localization of ``name`` in the
`gameobject\_template <gameobject_template>`__ table.

name\_loc8
----------

*Russian* localization of ``name`` in the
`gameobject\_template <gameobject_template>`__ table.
