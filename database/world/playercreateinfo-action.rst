.. _db-world-playercreateinfo-action:

================================
"playercreateinfo\_action" table
================================

The ``playercreateinfo_action`` table holds information on what default
actions a new character should start out with. Each race-class
combination can have a different default starting setup.

Table structure
---------------

+----------+------------------------+--------+-------+-----------+---------+
| Field    | Type                   | Null   | Key   | Default   | Extra   |
+==========+========================+========+=======+===========+=========+
| race     | tinyint(3) unsigned    | NO     | PRI   | 0         |         |
+----------+------------------------+--------+-------+-----------+---------+
| class    | tinyint(3) unsigned    | NO     | PRI   | 0         |         |
+----------+------------------------+--------+-------+-----------+---------+
| button   | smallint(5) unsigned   | NO     | PRI   | 0         |         |
+----------+------------------------+--------+-------+-----------+---------+
| action   | int(11) unsigned       | NO     |       | 0         |         |
+----------+------------------------+--------+-------+-----------+---------+
| type     | smallint(5) unsigned   | NO     |       | 0         |         |
+----------+------------------------+--------+-------+-----------+---------+

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

button
------

The ID of the button on the action bar where the action icon will be
placed. Special bars are used for stances, auras, pets, stealth and
other similar special modes.

+----------------+--------------------------------------+
| button ID(s)   | Set key                              |
+================+======================================+
| 1-11           | 1 (SHIFT + 1)                        |
+----------------+--------------------------------------+
| 12-23          | 2 (SHIFT + 2)                        |
+----------------+--------------------------------------+
| 24-35          | 3 (SHIFT + 3) h1. Right Side Bar     |
+----------------+--------------------------------------+
| 36-47          | 4 (SHIFT + 4) Right Side Bar 2       |
+----------------+--------------------------------------+
| 48-59          | 5 (SHIFT + 5) h1. Bottom Right Bar   |
+----------------+--------------------------------------+
| 60-71          | 6 (SHIFT + 6) Bottom Left Bar        |
+----------------+--------------------------------------+
| 72-83          | 1 SpecialA                           |
+----------------+--------------------------------------+
| 84-95          | 1 SpecialB                           |
+----------------+--------------------------------------+
| 96-107         | 1 SpecialC                           |
+----------------+--------------------------------------+
| 108-119        | 1 SpecialD                           |
+----------------+--------------------------------------+

action
------

Depending on the type value, this could reference either a spell
identifier as defined in ``Spell.dbc``, a reference to the unique
identifier of an `item\_template <item_template>`__, or the identifier
for a macro.

type
----

The following values are valid types:

+-------+---------+
| ID    | Type    |
+=======+=========+
| 0     | Spell   |
+-------+---------+
| 64    | Macro   |
+-------+---------+
| 128   | Item    |
+-------+---------+

