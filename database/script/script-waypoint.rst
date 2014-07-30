.. _db-script-script-waypoint:

=========================
"script\_waypoints" table
=========================

The ``script_waypoints`` table holds waypoint definitions for escort
quests.

Table structure
---------------

+------------------+-------------------------+--------+-------+-----------+---------+
| Field            | Type                    | Null   | Key   | Default   | Extra   |
+==================+=========================+========+=======+===========+=========+
| entry            | mediumint(8) unsigned   | NO     | PRI   | 0         |         |
+------------------+-------------------------+--------+-------+-----------+---------+
| pointid          | mediumint(8) unsigned   | NO     | PRI   | 0         |         |
+------------------+-------------------------+--------+-------+-----------+---------+
| location\_x      | float                   | NO     |       | 0         |         |
+------------------+-------------------------+--------+-------+-----------+---------+
| location\_y      | float                   | NO     |       | 0         |         |
+------------------+-------------------------+--------+-------+-----------+---------+
| location\_z      | float                   | NO     |       | 0         |         |
+------------------+-------------------------+--------+-------+-----------+---------+
| waittime         | int(10) unsigned        | NO     |       | 0         |         |
+------------------+-------------------------+--------+-------+-----------+---------+
| point\_comment   | text                    | YES    |       | NULL      |         |
+------------------+-------------------------+--------+-------+-----------+---------+

Fields
------

entry
-----

This references the creature for which the waypoint script is meant to
be executed and references the identifier in the
`creature\_template <../world/creature_template>`__ table.

pointid
-------

An index count for all waypoints attached to a script. Starts with ``1``
and increments by one.

location\_x
-----------

The X position for the script's waypoint.

location\_y
-----------

The Y position for the script's waypoint.

location\_z
-----------

The Z position for the script's waypoint.

waittime
--------

If the creature should wait at the movement point, set this to the time
in milliseconds. Otherwise set to zero for the creature to immediately
proceed to the next movement point.

point\_comment
--------------

A common rules is to add comments to any waypoint where something
special is happening. This means: do not comment every point, but
comment those where an action is executed, e.g. a text emote, a quest
completion is activated.
