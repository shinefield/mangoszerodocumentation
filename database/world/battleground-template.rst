.. _db-world-battleground-template:

==============================
"battleground\_template" table
==============================

The ``battleground_template`` table holds information on requirements
for each battleground which have to be met in order to start a battle.

-  Battlegrounds are set to run in tiers. A tier is a fixed level range
   set differently for every battleground. A tier is usually 9 levels,
   i.e. 51-60
-  Participating players *have* to be from the same tier.

Table structure
---------------

+---------------------+-------------------------+--------+-------+-----------+---------+
| Field               | Type                    | Null   | Key   | Default   | Extra   |
+=====================+=========================+========+=======+===========+=========+
| id                  | mediumint(8) unsigned   | NO     | PRI   | NULL      |         |
+---------------------+-------------------------+--------+-------+-----------+---------+
| MinPlayersPerTeam   | smallint(5) unsigned    | NO     |       | 0         |         |
+---------------------+-------------------------+--------+-------+-----------+---------+
| MaxPlayersPerTeam   | smallint(5) unsigned    | NO     |       | 0         |         |
+---------------------+-------------------------+--------+-------+-----------+---------+
| MinLvl              | tinyint(3) unsigned     | NO     |       | 0         |         |
+---------------------+-------------------------+--------+-------+-----------+---------+
| MaxLvl              | tinyint(3) unsigned     | NO     |       | 0         |         |
+---------------------+-------------------------+--------+-------+-----------+---------+
| AllianceStartLoc    | mediumint(8) unsigned   | NO     |       | NULL      |         |
+---------------------+-------------------------+--------+-------+-----------+---------+
| AllianceStartO      | float                   | NO     |       | NULL      |         |
+---------------------+-------------------------+--------+-------+-----------+---------+
| HordeStartLoc       | mediumint(8) unsigned   | NO     |       | NULL      |         |
+---------------------+-------------------------+--------+-------+-----------+---------+
| HordeStartO         | float                   | NO     |       | NULL      |         |
+---------------------+-------------------------+--------+-------+-----------+---------+

Fields
------

id
--

A unique identifier for the battleground. The following list provides
all valid identifiers.

+---------+------------------+
| Value   | Description      |
+=========+==================+
| 1       | Alterac Valley   |
+---------+------------------+
| 2       | Warsong Gulch    |
+---------+------------------+
| 3       | Arathi Basin     |
+---------+------------------+

MinPlayersPerTeam
-----------------

This field defines the minimum number of characters required to join
from each faction in order to start a battle.

MaxPlayersPerTeam
-----------------

This field defines the maximum number of characters allowed to join from
each faction in order to start a battle. If set to ``0``, the server
will use the value from `Map.dbc <../dbc/Map.dbc>`__.

MinLvl
------

The minimum level required to enter the battleground. If set to ``0``,
the server will use the value from `Map.dbc <../dbc/Map.dbc>`__.

MaxLvl
------

The maximum level allowed to enter the battleground. If set to ``0``,
the server will use the value from `Map.dbc <../dbc/Map.dbc>`__.

AllianceStartLoc
----------------

The location where Alliance characters initially will spawn. This
references a safe location value from
`WorldSafeLocs.dbc <WorldSafeLocs.dbc>`__.

AllianceStartO
--------------

The orientation used for Alliance players when spawn on the initial
location. The orientation is measured in radians where ``0`` is north on
the mini-map and ``pi`` is south on the mini-map.

HordeStartLoc
-------------

The location where Horde characters initially will spawn. This
references a safe location value from
`WorldSafeLocs.dbc <WorldSafeLocs.dbc>`__.

HordeStartO
-----------

The orientation used for Horde players when spawn on the initial
location. The orientation is measured in radians where ``0`` is north on
the mini-map and ``pi`` is south on the mini-map.
