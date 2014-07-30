.. _db-world-playercreateinfo-item:

==============================
"playercreateinfo\_item" table
==============================

The ``playercreateinfo_item`` table holds information on items a
character should receive upon creation.

Items received can be restricted by races and classes.

Table structure
---------------

+----------+-------------------------+--------+-------+-----------+---------+
| Field    | Type                    | Null   | Key   | Default   | Extra   |
+==========+=========================+========+=======+===========+=========+
| race     | tinyint(3) unsigned     | NO     | MUL   | 0         |         |
+----------+-------------------------+--------+-------+-----------+---------+
| class    | tinyint(3) unsigned     | NO     |       | 0         |         |
+----------+-------------------------+--------+-------+-----------+---------+
| itemid   | mediumint(8) unsigned   | NO     |       | 0         |         |
+----------+-------------------------+--------+-------+-----------+---------+
| amount   | tinyint(3) unsigned     | NO     |       | 1         |         |
+----------+-------------------------+--------+-------+-----------+---------+

Fields
------

race
----

A bit-mask corresponding to races that should get the spell. The value
has to match with races defined in
`ChrRaces.dbc <../dbc/ChrRaces.dbc>`__.

class
-----

A bit-mask corresponding to class that should get the spell. The value
has to match with classes defined in
`ChrClasses.dbc <../dbc/ChrClasses.dbc>`__.

itemid
------

The item a character should receive upon creation. This references the
`item\_template <item_template>`__ tables unique ID.

amount
------

The number of copies of the item to be awarded.
