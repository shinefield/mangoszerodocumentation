.. _db-world-points-of-interest:

============================
"points\_of\_interest" table
============================

The ``points_of_interest`` table holds definitions for points of
interests in various locations.

Table structure
---------------

+--------------+-------------------------+--------+-------+-----------+---------+
| Field        | Type                    | Null   | Key   | Default   | Extra   |
+==============+=========================+========+=======+===========+=========+
| entry        | mediumint(8) unsigned   | NO     | PRI   | 0         |         |
+--------------+-------------------------+--------+-------+-----------+---------+
| x            | float                   | NO     |       | 0         |         |
+--------------+-------------------------+--------+-------+-----------+---------+
| y            | float                   | NO     |       | 0         |         |
+--------------+-------------------------+--------+-------+-----------+---------+
| icon         | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------+-------------------------+--------+-------+-----------+---------+
| flags        | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------+-------------------------+--------+-------+-----------+---------+
| data         | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------+-------------------------+--------+-------+-----------+---------+
| icon\_name   | text                    | NO     |       | NULL      |         |
+--------------+-------------------------+--------+-------+-----------+---------+

Fields
------

entry
-----

The identifier for the point of interest.

x
-

The X coordinate for the point of interest.

y
-

The Y coordinate for the point of interest.

icon
----

The icon to be used for this point of interest. This references an icon
entry from `SpellIcon.dbc <../dbc/SpellIcon.dbc>`__

flags
-----

**TODO**

data
----

Custom data to be sent for a point of interest. This currently is ``0``
for all points of interests in vanilla WoW.

icon\_name
----------

The text to display as tooltip for the icon on the in-game map.
