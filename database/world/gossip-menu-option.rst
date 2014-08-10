.. _db-world-gossip-menu-option:

============================
"gossip\_menu\_option" table
============================

The ``gossip_menu_option`` table holds informations on each entry
assigned to a ``gossip_menu``.

Table structure
---------------

+------------------------+-------------------------+--------+-------+-----------+---------+
| Field                  | Type                    | Null   | Key   | Default   | Extra   |
+========================+=========================+========+=======+===========+=========+
| menu\_id               | smallint(6) unsigned    | NO     | PRI   | 0         |         |
+------------------------+-------------------------+--------+-------+-----------+---------+
| id                     | smallint(6) unsigned    | NO     | PRI   | 0         |         |
+------------------------+-------------------------+--------+-------+-----------+---------+
| option\_icon           | mediumint(8) unsigned   | NO     |       | 0         |         |
+------------------------+-------------------------+--------+-------+-----------+---------+
| option\_text           | text                    | YES    |       | NULL      |         |
+------------------------+-------------------------+--------+-------+-----------+---------+
| option\_id             | tinyint(3) unsigned     | NO     |       | 0         |         |
+------------------------+-------------------------+--------+-------+-----------+---------+
| npc\_option\_npcflag   | int(10) unsigned        | NO     |       | 0         |         |
+------------------------+-------------------------+--------+-------+-----------+---------+
| action\_menu\_id       | mediumint(8)            | NO     |       | 0         |         |
+------------------------+-------------------------+--------+-------+-----------+---------+
| action\_poi\_id        | mediumint(8) unsigned   | NO     |       | 0         |         |
+------------------------+-------------------------+--------+-------+-----------+---------+
| action\_script\_id     | mediumint(8) unsigned   | NO     |       | 0         |         |
+------------------------+-------------------------+--------+-------+-----------+---------+
| box\_coded             | tinyint(3) unsigned     | NO     |       | 0         |         |
+------------------------+-------------------------+--------+-------+-----------+---------+
| box\_money             | int(11) unsigned        | NO     |       | 0         |         |
+------------------------+-------------------------+--------+-------+-----------+---------+
| box\_text              | text                    | YES    |       | NULL      |         |
+------------------------+-------------------------+--------+-------+-----------+---------+
| condition\_id          | mediumint(8) unsigned   | NO     |       | 0         |         |
+------------------------+-------------------------+--------+-------+-----------+---------+

Fields
------

menu\_id
--------

This references the :doc:`gossip-menu` tables unique ID for
which the entry is valid.

id
--

The unique identifier for this gossip\_menu\_option.

option\_icon
------------

The value of this field determines which icon the game client will
display in front of an option. The following table shows all valid
icons:

+---------+-----------------------------+-------------------------------------+
| Value   | Icon name                   | Description                         |
+=========+=============================+=====================================+
| 0       | GOSSIP\_ICON\_CHAT          | white chat bubble                   |
+---------+-----------------------------+-------------------------------------+
| 1       | GOSSIP\_ICON\_VENDOR        | brown bag                           |
+---------+-----------------------------+-------------------------------------+
| 2       | GOSSIP\_ICON\_TAXI          | flight                              |
+---------+-----------------------------+-------------------------------------+
| 3       | GOSSIP\_ICON\_TRAINER       | book                                |
+---------+-----------------------------+-------------------------------------+
| 4       | GOSSIP\_ICON\_INTERACT\_1   | interaction wheel                   |
+---------+-----------------------------+-------------------------------------+
| 5       | GOSSIP\_ICON\_INTERACT\_2   | interaction wheel                   |
+---------+-----------------------------+-------------------------------------+
| 6       | GOSSIP\_ICON\_MONEY\_BAG    | brown bag with coin                 |
+---------+-----------------------------+-------------------------------------+
| 7       | GOSSIP\_ICON\_TALK          | white chat bubble with black dots   |
+---------+-----------------------------+-------------------------------------+
| 8       | GOSSIP\_ICON\_TABARD        | tabard                              |
+---------+-----------------------------+-------------------------------------+
| 9       | GOSSIP\_ICON\_BATTLE        | two swords                          |
+---------+-----------------------------+-------------------------------------+
| 10      | GOSSIP\_ICON\_DOT           | yellow dot                          |
+---------+-----------------------------+-------------------------------------+

option\_text
------------

The text to be displayed for the gossip\_menu\_option entry.

option\_id
----------

The value of this field tells the client which kind of user interface
the menu will require. The following table shows all valid option types:

+---------+------------------------------------+
| Value   | Option types                       |
+=========+====================================+
| 0       | GOSSIP\_OPTION\_NONE               |
+---------+------------------------------------+
| 1       | GOSSIP\_OPTION\_GOSSIP             |
+---------+------------------------------------+
| 2       | GOSSIP\_OPTION\_QUESTGIVER         |
+---------+------------------------------------+
| 3       | GOSSIP\_OPTION\_VENDOR             |
+---------+------------------------------------+
| 4       | GOSSIP\_OPTION\_TAXIVENDOR         |
+---------+------------------------------------+
| 5       | GOSSIP\_OPTION\_TRAINER            |
+---------+------------------------------------+
| 6       | GOSSIP\_OPTION\_SPIRITHEALER       |
+---------+------------------------------------+
| 7       | GOSSIP\_OPTION\_SPIRITGUIDE        |
+---------+------------------------------------+
| 8       | GOSSIP\_OPTION\_INNKEEPER          |
+---------+------------------------------------+
| 9       | GOSSIP\_OPTION\_BANKER             |
+---------+------------------------------------+
| 10      | GOSSIP\_OPTION\_PETITIONER         |
+---------+------------------------------------+
| 11      | GOSSIP\_OPTION\_TABARDDESIGNER     |
+---------+------------------------------------+
| 12      | GOSSIP\_OPTION\_BATTLEFIELD        |
+---------+------------------------------------+
| 13      | GOSSIP\_OPTION\_AUCTIONEER         |
+---------+------------------------------------+
| 14      | GOSSIP\_OPTION\_STABLEPET          |
+---------+------------------------------------+
| 15      | GOSSIP\_OPTION\_ARMORER            |
+---------+------------------------------------+
| 16      | GOSSIP\_OPTION\_UNLEARNTALENTS     |
+---------+------------------------------------+
| 17      | GOSSIP\_OPTION\_UNLEARNPETSKILLS   |
+---------+------------------------------------+

.. note::

    In order for gossip\_menu\_option entries to work, the
    ``npcflag`` of the :doc:`creature-template` table
    entry needs to be set appropriately.

npc\_option\_npcflag
--------------------

Each option requires a matching ``npcflag``. The following table shows
option IDs and their flag pair:

+-----------+----------------------------------+
| flag      | option ID                        |
+===========+==================================+
| 0         | GOSSIP\_OPTION\_NONE             |
+-----------+----------------------------------+
| 1         | GOSSIP\_OPTION\_GOSSIP           |
+-----------+----------------------------------+
| 2         | GOSSIP\_OPTION\_QUESTGIVER       |
+-----------+----------------------------------+
| 16        | GOSSIP\_OPTION\_TRAINER          |
+-----------+----------------------------------+
| 128       | GOSSIP\_OPTION\_VENDOR           |
+-----------+----------------------------------+
| 4096      | GOSSIP\_OPTION\_ARMORER          |
+-----------+----------------------------------+
| 8192      | GOSSIP\_OPTION\_TAXIVENDOR       |
+-----------+----------------------------------+
| 16384     | GOSSIP\_OPTION\_SPIRITHEALER     |
+-----------+----------------------------------+
| 32768     | GOSSIP\_OPTION\_SPIRITGUIDE      |
+-----------+----------------------------------+
| 65536     | GOSSIP\_OPTION\_INNKEEPER        |
+-----------+----------------------------------+
| 131072    | GOSSIP\_OPTION\_BANKER           |
+-----------+----------------------------------+
| 262144    | GOSSIP\_OPTION\_PETITIONER       |
+-----------+----------------------------------+
| 524288    | GOSSIP\_OPTION\_TABARDDESIGNER   |
+-----------+----------------------------------+
| 1048576   | GOSSIP\_OPTION\_BATTLEFIELD      |
+-----------+----------------------------------+
| 2097152   | GOSSIP\_OPTION\_AUCTIONEER       |
+-----------+----------------------------------+
| 4194304   | GOSSIP\_OPTION\_STABLEPET        |
+-----------+----------------------------------+

The following are flags are bonus options for creatures marked as
trainers, or pet trainers.

+--------+------------------------------------+
| flag   | option ID                          |
+========+====================================+
| 16     | GOSSIP\_OPTION\_UNLEARNTALENTS     |
+--------+------------------------------------+
| 16     | GOSSIP\_OPTION\_UNLEARNPETSKILLS   |
+--------+------------------------------------+

action\_menu\_id
----------------

To create a sub-menu, this can reference the
:doc:`gossip-menu` tables unique ID for which the entry is
valid.

.. note::

    If you want the gossip\_menu\_option to close the gossip
    window, set this field to ``-1``.

action\_poi\_id
---------------

This references the :doc:`points-of-interest` tables
unique ID for which the entry is valid.

action\_script\_id
------------------

This references the :doc:`dbscripts-on-gossip`
tables unique ID for which the entry is valid.

box\_coded
----------

If you want the gossip\_menu\_option to display an input box, where
players have to enter a code, set this field to ``1``.

box\_money
----------

If a coded box is to be displayed and the player should be asked for
money, set this to the money asked in copper.

box\_text
---------

If a coded box is to be displayed, set this to a text value to show it
in the coded box.

condition\_id
-------------

This references the :doc:`conditions` tables unique ID for
which the entry is valid.
