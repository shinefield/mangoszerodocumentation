.. _db-world-creature-linking:

=========================
"creature\_linking" table
=========================

The ``creature_linking`` table holds details how creatures linked to a
master creature should act in combat and non-combat situations.

Table structure
---------------

+----------------+-------------------------+--------+-------+-----------+---------+
| Field          | Type                    | Null   | Key   | Default   | Extra   |
+================+=========================+========+=======+===========+=========+
| guid           | int(10) unsigned        | NO     | PRI   | NULL      |         |
+----------------+-------------------------+--------+-------+-----------+---------+
| master\_guid   | int(10) unsigned        | NO     |       | NULL      |         |
+----------------+-------------------------+--------+-------+-----------+---------+
| flag           | mediumint(8) unsigned   | NO     |       | NULL      |         |
+----------------+-------------------------+--------+-------+-----------+---------+

Fields
------

guid
----

This references the `creature <creature>`__ tables unique ID for which
the entry is valid. This is a creature spawn bound to the master
creature.

master\_guid
------------

This references the `creature <creature>`__ tables unique ID for which
the entry is valid. This is the master creature which defines behaviour
for the linked creature.

flag
----

This flag determines how a linked creature will act, when the master is
changing it's combat state. Flags provide support for combat state, non
combat state and life state.

The following flags determine the behaviour if the master is in combat
state.

+---------+--------------------------------+-----------------------------------------------+
| Value   | Name                           | Description                                   |
+=========+================================+===============================================+
| 1       | FLAG\_AGGRO\_ON\_AGGRO         | the slave aggroes when the master aggroes     |
+---------+--------------------------------+-----------------------------------------------+
| 2       | FLAG\_TO\_AGGRO\_ON\_AGGRO     | the master aggroes when the slave aggroes     |
+---------+--------------------------------+-----------------------------------------------+
| 4       | FLAG\_RESPAWN\_ON\_EVADE       | the slave respawns when the master evades     |
+---------+--------------------------------+-----------------------------------------------+
| 8       | FLAG\_TO\_RESPAWN\_ON\_EVADE   | the master respawns when the slave evades     |
+---------+--------------------------------+-----------------------------------------------+
| 4096    | FLAG\_DESPAWN\_ON\_EVADE       | the slave despawn after the master evade      |
+---------+--------------------------------+-----------------------------------------------+
| 16      | FLAG\_DESPAWN\_ON\_DEATH       | the slave despawns when the master dies       |
+---------+--------------------------------+-----------------------------------------------+
| 32      | FLAG\_SELFKILL\_ON\_DEATH      | the slave goes suicide when the master dies   |
+---------+--------------------------------+-----------------------------------------------+
| 64      | FLAG\_RESPAWN\_ON\_DEATH       | the slave respawn when the master dies        |
+---------+--------------------------------+-----------------------------------------------+
| 128     | FLAG\_RESPAWN\_ON\_RESPAWN     | the slave respawns on master respawn          |
+---------+--------------------------------+-----------------------------------------------+
| 256     | FLAG\_DESPAWN\_ON\_RESPAWN     | the slave despawns on master respawn          |
+---------+--------------------------------+-----------------------------------------------+

The following flags determine the behaviour if the master is out of
combat state.

+---------+----------------+--------------------------------+
| Value   | Name           | Description                    |
+=========+================+================================+
| 512     | FLAG\_FOLLOW   | the slave follows the master   |
+---------+----------------+--------------------------------+

The following flags determine the behaviour for any combat state.

+---------+--------------------------------------+------------------------------------------------+
| Value   | Name                                 | Description                                    |
+=========+======================================+================================================+
| 1024    | FLAG\_CANT\_SPAWN\_IF\_BOSS\_DEAD    | the slave cannot respawn while boss is dead    |
+---------+--------------------------------------+------------------------------------------------+
| 2048    | FLAG\_CANT\_SPAWN\_IF\_BOSS\_ALIVE   | the slave cannot respawn while boss is alive   |
+---------+--------------------------------------+------------------------------------------------+

