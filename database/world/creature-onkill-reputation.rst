.. _db-world-creature-onkill-reputation:

====================================
"creature\_onkill\_reputation" table
====================================

The ``creature_onkill_reputation`` table holds information on reputation
awarded to characters when killing the creature.

.. note::

    Reputation is awarded only on ``creature_template`` level, but
    not for individual spawns.

Table structure
---------------

+------------------------+-------------------------+--------+-------+-----------+---------+
| Field                  | Type                    | Null   | Key   | Default   | Extra   |
+========================+=========================+========+=======+===========+=========+
| creature\_id           | mediumint(8) unsigned   | NO     | PRI   | 0         |         |
+------------------------+-------------------------+--------+-------+-----------+---------+
| RewOnKillRepFaction1   | smallint(6)             | NO     |       | 0         |         |
+------------------------+-------------------------+--------+-------+-----------+---------+
| RewOnKillRepFaction2   | smallint(6)             | NO     |       | 0         |         |
+------------------------+-------------------------+--------+-------+-----------+---------+
| MaxStanding1           | tinyint(4)              | NO     |       | 0         |         |
+------------------------+-------------------------+--------+-------+-----------+---------+
| IsTeamAward1           | tinyint(4)              | NO     |       | 0         |         |
+------------------------+-------------------------+--------+-------+-----------+---------+
| RewOnKillRepValue1     | mediumint(9)            | NO     |       | 0         |         |
+------------------------+-------------------------+--------+-------+-----------+---------+
| MaxStanding2           | tinyint(4)              | NO     |       | 0         |         |
+------------------------+-------------------------+--------+-------+-----------+---------+
| IsTeamAward2           | tinyint(4)              | NO     |       | 0         |         |
+------------------------+-------------------------+--------+-------+-----------+---------+
| RewOnKillRepValue2     | mediumint(9)            | NO     |       | 0         |         |
+------------------------+-------------------------+--------+-------+-----------+---------+
| TeamDependent          | tinyint(3) unsigned     | NO     |       | 0         |         |
+------------------------+-------------------------+--------+-------+-----------+---------+

Fields
------

creature\_id
------------

This references the `creature\_template <creature_template>`__ tables
unique ID for which the entry is valid.

RewOnKillRepFaction1
--------------------

A faction for which reputation is awarded. The value has to match with a
faction identifier defined in :doc:`../../file-formats/dbc/faction`. This
is the default faction for which reputation will be gained. If the
reputation awarded is faction specific, this is the faction Alliance
characters will gain reputation for.

RewOnKillRepFaction2
--------------------

A faction for which reputation is awarded. The value has to match with a
faction identifier defined in :doc:`../../file-formats/dbc/faction`. If
the reputation awarded is faction specific, this is the faction Horde
characters will gain reputation for.

MaxStanding1
------------

The maximum standing up to which a creature will award reputation
towards ``RewOnKillRepFaction1``. The following table lists valid
entries for the maximum standing.

+---------+--------------+
| Value   | Standing     |
+=========+==============+
| 0       | Hated        |
+---------+--------------+
| 1       | Hostile      |
+---------+--------------+
| 2       | Unfriendly   |
+---------+--------------+
| 3       | Neutral      |
+---------+--------------+
| 4       | Friendly     |
+---------+--------------+
| 5       | Honored      |
+---------+--------------+
| 6       | Revered      |
+---------+--------------+
| 7       | Exalted      |
+---------+--------------+

IsTeamAward1
------------

Decides if characters will gain reputation only for
``RewOnKillRepFaction2``, or for the faction's group, too. If group
faction is granted, this is half of the value of ``RewOnKillRepValue1``.

RewOnKillRepValue1
------------------

The reputation value characters will gain from ``RewOnKillRepFaction1``.

MaxStanding2
------------

The maximum standing up to which a creature will award reputation
towards ``RewOnKillRepFaction2``. The following table lists valid
entries for the maximum standing.

+---------+--------------+
| Value   | Standing     |
+=========+==============+
| 0       | Hated        |
+---------+--------------+
| 1       | Hostile      |
+---------+--------------+
| 2       | Unfriendly   |
+---------+--------------+
| 3       | Neutral      |
+---------+--------------+
| 4       | Friendly     |
+---------+--------------+
| 5       | Honored      |
+---------+--------------+
| 6       | Revered      |
+---------+--------------+
| 7       | Exalted      |
+---------+--------------+

IsTeamAward2
------------

Decides if characters will gain reputation only for
``RewOnKillRepFaction2``, or for the faction's group, too. If group
faction is granted, this is half of the value of ``RewOnKillRepValue2``.

RewOnKillRepValue2
------------------

The reputation value characters will gain from ``RewOnKillRepFaction2``.

TeamDependent
-------------

This field decides if a reputation entry will be awarded for all
character factions, or if different factions applied to Alliance and
Horde characters.

+---------+------------------------------------------------------------------------------------------------------------------------+
| Value   | Description                                                                                                            |
+=========+========================================================================================================================+
| 0       | Reputation will be awarded to both Alliance and Horde from ``RewOnKillRepFaction1`` **and** ``RewOnKillRepFaction2``   |
+---------+------------------------------------------------------------------------------------------------------------------------+
| 1       | Reputation will be awarded to Alliance from ``RewOnKillRepFaction1`` and to Horde from ``RewOnKillRepFaction2``        |
+---------+------------------------------------------------------------------------------------------------------------------------+

