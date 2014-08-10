.. _db-world-transports:

==================
"transports" table
==================

The ``transports`` table holds informations on available world
transports. This includes boats and Zeppelins.

Table structure
---------------

+----------+-------------------------+--------+-------+-----------+---------+
| Field    | Type                    | Null   | Key   | Default   | Extra   |
+==========+=========================+========+=======+===========+=========+
| entry    | mediumint(8) unsigned   | NO     | PRI   | 0         |         |
+----------+-------------------------+--------+-------+-----------+---------+
| name     | text                    | YES    |       | NULL      |         |
+----------+-------------------------+--------+-------+-----------+---------+
| period   | mediumint(8) unsigned   | NO     |       | 0         |         |
+----------+-------------------------+--------+-------+-----------+---------+

Fields
------

entry
-----

This references the `gameobject\_template <gameobject_template>`__
tables unique ID of the game object of type 15 (boats and Zeppelins) for
which the entry is valid.

name
----

A name describing the transport. This is not used in-game, but only here
to ease locking up data.

period
------

This is the amount of time that it take for the transport to make one
full pass through all the frames in
:doc:`../../file-formats/dbc/taxinodes`. When a client change occurs,
usually this field must be updated. This values is set in milliseconds.
