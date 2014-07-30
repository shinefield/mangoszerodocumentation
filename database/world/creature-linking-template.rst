.. _db-world-creature-linking-template:

===================================
"creature\_linking\_template" table
===================================

The ``creature_linking_template`` table holds details how creature
templates linked to a master creature template should act in combat and
non-combat situations.

Table structure
---------------

+-----------------+-------------------------+--------+-------+-----------+---------+
| Field           | Type                    | Null   | Key   | Default   | Extra   |
+=================+=========================+========+=======+===========+=========+
| entry           | mediumint(8) unsigned   | NO     | PRI   | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| map             | smallint(5) unsigned    | NO     | PRI   | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| master\_entry   | mediumint(8) unsigned   | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| flag            | mediumint(8) unsigned   | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| search\_range   | mediumint(8) unsigned   | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+

Fields
------

entry
-----

This references the `creature\_template <creature_template>`__ tables
unique ID for which the entry is valid. This is a creature template
bound to the master creature template.

map
---

A map identifier. The value has to match with a map identifier defined
in `Map.dbc <../dbc/Map.dbc>`__. This is the map where creature
templates are located.

master\_entry
-------------

This references the `creature\_template <creature_template>`__ tables
unique ID for which the entry is valid. This is the master creature
template which defines behaviour for the linked creature template.

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

search\_range
-------------

This fields allows to set a range within the creature should look for
it's master.
