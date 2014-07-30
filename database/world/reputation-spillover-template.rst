.. _db-world-reputation-spillover-template:

=======================================
"reputation\_spillover\_template" table
=======================================

The ``reputation_spillover_template`` table holds information for
alternative factions which can be awarded reputation, if the faction
originally rewarded for is already and the highest reachable level.

Table structure
---------------

+------------+------------------------+--------+-------+-----------+---------+
| Field      | Type                   | Null   | Key   | Default   | Extra   |
+============+========================+========+=======+===========+=========+
| faction    | smallint(6) unsigned   | NO     | PRI   | 0         |         |
+------------+------------------------+--------+-------+-----------+---------+
| faction1   | smallint(6) unsigned   | NO     |       | 0         |         |
+------------+------------------------+--------+-------+-----------+---------+
| rate\_1    | float                  | NO     |       | 0         |         |
+------------+------------------------+--------+-------+-----------+---------+
| rank\_1    | tinyint(3) unsigned    | NO     |       | 0         |         |
+------------+------------------------+--------+-------+-----------+---------+
| faction2   | smallint(6) unsigned   | NO     |       | 0         |         |
+------------+------------------------+--------+-------+-----------+---------+
| rate\_2    | float                  | NO     |       | 0         |         |
+------------+------------------------+--------+-------+-----------+---------+
| rank\_2    | tinyint(3) unsigned    | NO     |       | 0         |         |
+------------+------------------------+--------+-------+-----------+---------+
| faction3   | smallint(6) unsigned   | NO     |       | 0         |         |
+------------+------------------------+--------+-------+-----------+---------+
| rate\_3    | float                  | NO     |       | 0         |         |
+------------+------------------------+--------+-------+-----------+---------+
| rank\_3    | tinyint(3) unsigned    | NO     |       | 0         |         |
+------------+------------------------+--------+-------+-----------+---------+
| faction4   | smallint(6) unsigned   | NO     |       | 0         |         |
+------------+------------------------+--------+-------+-----------+---------+
| rate\_4    | float                  | NO     |       | 0         |         |
+------------+------------------------+--------+-------+-----------+---------+
| rank\_4    | tinyint(3) unsigned    | NO     |       | 0         |         |
+------------+------------------------+--------+-------+-----------+---------+

Fields
------

faction
-------

A faction for which reputation is awarded. The value has to match with a
faction identifier defined in `Faction.dbc <../dbc/Faction.dbc>`__. This
is the faction for which reputation could not be rewarded any more.

faction1
--------

A faction for which reputation is awarded. The value has to match with a
faction identifier defined in `Faction.dbc <../dbc/Faction.dbc>`__. This
is an alternative to the ``faction`` defined.

rate\_1
-------

The rate at which reputation is awarded.

rank\_1
-------

The maximum rank up to which reputation will be awarded.

faction2
--------

A faction for which reputation is awarded. The value has to match with a
faction identifier defined in `Faction.dbc <../dbc/Faction.dbc>`__. This
is an alternative to the ``faction`` defined.

rate\_2
-------

The rate at which reputation is awarded.

rank\_2
-------

The maximum rank up to which reputation will be awarded.

faction3
--------

A faction for which reputation is awarded. The value has to match with a
faction identifier defined in `Faction.dbc <../dbc/Faction.dbc>`__. This
is an alternative to the ``faction`` defined.

rate\_3
-------

The rate at which reputation is awarded.

rank\_3
-------

The maximum rank up to which reputation will be awarded.

faction4
--------

A faction for which reputation is awarded. The value has to match with a
faction identifier defined in `Faction.dbc <../dbc/Faction.dbc>`__. This
is an alternative to the ``faction`` defined.

rate\_4
-------

The rate at which reputation is awarded.

rank\_4
-------

The maximum rank up to which reputation will be awarded.
