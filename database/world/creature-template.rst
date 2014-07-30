.. _db-world-creature-template:

==========================
"creature\_template" table
==========================

The ``creature_template`` table holds information on every creature that
exists in the game.

Table structure
---------------

+--------------------------+-------------------------+--------+-------+-----------+---------+
| Field                    | Type                    | Null   | Key   | Default   | Extra   |
+==========================+=========================+========+=======+===========+=========+
| entry                    | mediumint(8) unsigned   | NO     | PRI   | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| KillCredit1              | int(11) unsigned        | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| KillCredit2              | int(11) unsigned        | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| modelid\_1               | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| modelid\_2               | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| name                     | char(100)               | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| subname                  | char(100)               | YES    |       | NULL      |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| gossip\_menu\_id         | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| minlevel                 | tinyint(3) unsigned     | NO     |       | 1         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| maxlevel                 | tinyint(3) unsigned     | NO     |       | 1         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| minhealth                | int(10) unsigned        | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| maxhealth                | int(10) unsigned        | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| minmana                  | int(10) unsigned        | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| maxmana                  | int(10) unsigned        | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| armor                    | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| faction\_A               | smallint(5) unsigned    | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| faction\_H               | smallint(5) unsigned    | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| npcflag                  | int(10) unsigned        | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| speed\_walk              | float                   | NO     |       | 1         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| speed\_run               | float                   | NO     |       | 1.14286   |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| scale                    | float                   | NO     |       | 1         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| rank                     | tinyint(3) unsigned     | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| mindmg                   | float                   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| maxdmg                   | float                   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| dmgschool                | tinyint(4)              | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| attackpower              | int(10) unsigned        | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| dmg\_multiplier          | float                   | NO     |       | 1         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| baseattacktime           | int(10) unsigned        | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| rangeattacktime          | int(10) unsigned        | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| unit\_class              | tinyint(3) unsigned     | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| unit\_flags              | int(10) unsigned        | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| dynamicflags             | int(10) unsigned        | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| family                   | tinyint(4)              | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| trainer\_type            | tinyint(4)              | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| trainer\_spell           | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| trainer\_class           | tinyint(3) unsigned     | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| trainer\_race            | tinyint(3) unsigned     | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| minrangedmg              | float                   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| maxrangedmg              | float                   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| rangedattackpower        | smallint(5) unsigned    | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| type                     | tinyint(3) unsigned     | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| type\_flags              | int(10) unsigned        | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| lootid                   | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| pickpocketloot           | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| skinloot                 | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| resistance1              | smallint(5)             | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| resistance2              | smallint(5)             | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| resistance3              | smallint(5)             | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| resistance4              | smallint(5)             | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| resistance5              | smallint(5)             | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| resistance6              | smallint(5)             | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| PetSpellDataId           | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| mingold                  | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| maxgold                  | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| AIName                   | char(64)                | YES    |       | NULL      |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| MovementType             | tinyint(3) unsigned     | YES    |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| InhabitType              | tinyint(3) unsigned     | NO     |       | 3         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| Civilian                 | tinyint(3) unsigned     | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| RacialLeader             | tinyint(3) unsigned     | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| RegenHealth              | tinyint(3) unsigned     | NO     |       | 1         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| equipment\_id            | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| trainer\_id              | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| vendor\_id               | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| mechanic\_immune\_mask   | int(10) unsigned        | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| flags\_extra             | int(10) unsigned        | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| ScriptName               | char(64)                | YES    |       | NULL      |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+

Fields
------

entry
-----

The unique identifier of the creature template entry.

KillCredit1
-----------

If killing a creature should credit towards a different
``creature_template``, this should be set to the creature template's
identifier.

KillCredit2
-----------

If killing a creature should credit towards a different
``creature_template``, this should be set to the creature template's
identifier.

modelid\_1
----------

A display model identifier for the creature\_template. This references
the `creature\_model\_info <creature_model_info>`__ tables unique ID for
which this entry is valid.

modelid\_2
----------

A display model identifier for the creature\_template. This references
the `creature\_model\_info <creature_model_info>`__ tables unique ID for
which this entry is valid.

name
----

The creature's name that will be displayed.

subname
-------

An optional tag, which will be shown below the creature's name.

gossip\_menu\_id
----------------

This references the `gossip\_menu <gossip_menu>`__ tables unique ID for
which the entry is valid, if the creature\_template should have a gossip
dialogue.

minlevel
--------

The minimum level of the creature if the creature has a level range.

maxlevel
--------

The maximum level of the creature if the creature has a level range.
When added to world, a level in chosen in the specified level range.

minhealth
---------

The minimum health of the creature if the creature has variable health.

maxhealth
---------

The maximum health of the creature if the creature has a variable
health. When added to world, the health value is chosen in proportion to
the level chosen.

minmana
-------

The miminum mana of the creature if the creature has variable mana.

maxmana
-------

The maximum mana of the creature if the creature has variable mana. When
added to world, the mana value is chosen in proportion to the level
chosen.

armor
-----

The armor value of the creature. It controls how much damage reduction
the creature gets from physical attacks.

faction\_A
----------

A faction for creatures on the Alliance side. The value has to match
with a faction template identifier defined in
`FactionTemplate.dbc <../dbc/FactionTemplate.dbc>`__.

*Notice*: This field also controls the creature family assistance
mechanic. Only creatures with the same faction will assist each other.

faction\_H
----------

A faction for creatures on the Horde side. The value has to match with a
faction template identifier defined in
`FactionTemplate.dbc <../dbc/FactionTemplate.dbc>`__.

*Notice*: This field also controls the creature family assistance
mechanic. Only creatures with the same faction will assist each other.

npcflag
-------

This field is used to flag a creature\_template with the features it
should support. Since this is a bit field, multiple flags can be
combined as needed. A list of supported flags is provided below.

+-------------+------------------+------------+
| Value       | Description      | Comments   |
+=============+==================+============+
| 0           | None             |            |
+-------------+------------------+------------+
| 1           | Gossip           |            |
+-------------+------------------+------------+
| 2           | Questgiver       |            |
+-------------+------------------+------------+
| 4           | Vendor           |            |
+-------------+------------------+------------+
| 8           | Flightmaster     |            |
+-------------+------------------+------------+
| 16          | Trainer          |            |
+-------------+------------------+------------+
| 32          | Spirithealer     |            |
+-------------+------------------+------------+
| 64          | Spiritguide      |            |
+-------------+------------------+------------+
| 128         | Innkeeper        |            |
+-------------+------------------+------------+
| 256         | Banker           |            |
+-------------+------------------+------------+
| 512         | Petitioner       |            |
+-------------+------------------+------------+
| 1024        | Tabarddesigner   |            |
+-------------+------------------+------------+
| 2048        | Battlemaster     |            |
+-------------+------------------+------------+
| 4096        | Auctioneer       |            |
+-------------+------------------+------------+
| 8192        | Stablemaster     |            |
+-------------+------------------+------------+
| 16384       | Repair           |            |
+-------------+------------------+------------+
| 536870912   | Outdoor PvP      | Custom     |
+-------------+------------------+------------+

speed\_walk
-----------

Controls how fast the creature can move in walking mode.

speed\_run
----------

Controls how fast the creature can move in running mode.

scale
-----

If non-zero, this field defines how the size of the model appears in
game. If zero, it will use default model size taken from
`CreatureDisplayInfo.dbc <../dbc/CreatureDisplayInfo.dbc>`__.

rank
----

The rank of a creature determines which border the game client will draw
around the creature tooltip in the user interface. The following table
lists all valid values:

+---------+--------------+-------------------------------------------------+
| Value   | Name         | Description                                     |
+=========+==============+=================================================+
| 0       | Normal       | Default type                                    |
+---------+--------------+-------------------------------------------------+
| 1       | Elite        | Increased health, damage, better loot           |
+---------+--------------+-------------------------------------------------+
| 2       | Rare elite   | Like Elite but with increased respawn time      |
+---------+--------------+-------------------------------------------------+
| 3       | World boss   | Highest rank, best loot, highest respawn time   |
+---------+--------------+-------------------------------------------------+
| 4       | Rare         | Increased respawn time, better loot             |
+---------+--------------+-------------------------------------------------+

mindmg
------

Minimum damage the creature deals in melee combat. This field is
combined with the attackpower field to calculate the damage.

maxdmg
------

Maximum damage the creature deals in melee combat. This field is
combined with the attackpower field to calculate the damage.

dmgschool
---------

A damage school for melee combat. The following table provides a list of
valid values.

+---------+-----------------+
| Value   | Description     |
+=========+=================+
| 0       | Normal damage   |
+---------+-----------------+
| 1       | Holy damage     |
+---------+-----------------+
| 2       | Fire damage     |
+---------+-----------------+
| 3       | Nature damage   |
+---------+-----------------+
| 4       | Frost damage    |
+---------+-----------------+
| 5       | Shadow damage   |
+---------+-----------------+
| 6       | Arcane damage   |
+---------+-----------------+

attackpower
-----------

The attack power for the creature's melee attacks. This field along with
``mindmg`` and ``maxdmg`` dictate how much the creature will hit for.
The formula for applying correct damages is as follows:

.. code-block:: sql

        UPDATE `creature_template` SET
            `mindmg` = <#1>,
            `maxdmg` = <#2>,
            `attackpower` = ROUND((`mindmg` + `maxdmg`) / 4 * 7),
            `mindmg` = ROUND(`mindmg` - `attackpower` / 7),
            `maxdmg` = ROUND(`maxdmg` - `attackpower` / 7)
          WHERE `entry` = ...

In the query above, substitute ``<#1>`` with the minimum damage you want
the creature to deal and ``<#2>`` with the maximum damage you want the
creature to deal.

*Notice*: you might want to double check the calculated values after the
query has run because a large difference between ``mindmg`` and
``maxdmg`` can cause ``mindmg`` to become a negative value.

dmg\_multiplier
---------------

Setting this value to a value smaller or larger than ``1`` will modify
the creature template's damage by this factor.

baseattacktime
--------------

A creature's melee attack time in milliseconds.

rangeattacktime
---------------

A creature's ranged attack time in milliseconds.

unit\_class
-----------

A creature's class. The following table describes the available classes.

+---------+-----------+-----------------------------------------+
| Value   | Name      | Description                             |
+=========+===========+=========================================+
| 1       | Warrior   | Has increased health and no mana        |
+---------+-----------+-----------------------------------------+
| 2       | Paladin   | Has increased health and low mana       |
+---------+-----------+-----------------------------------------+
| 4       | Rogue     | Has increased damage, but lower armor   |
+---------+-----------+-----------------------------------------+
| 8       | Mage      | Has low health, but increased mana      |
+---------+-----------+-----------------------------------------+

*Notice*: depending on the creature's class, you have to make sure that
the mana values are set properly. E.g. a Warrior or Rogue will not have
mana set.

unit\_flags
-----------

Unit flags are used to signal creature template states. The following
table contains a list of known values.

**TODO**: since this field is a 32bit sized byte mask, there is a lot to
figure out.

+-------------+----------------------+
| Value       | Description          |
+=============+======================+
| 0           | Default              |
+-------------+----------------------+
| 1           | Unknown              |
+-------------+----------------------+
| 2           | Not attackable       |
+-------------+----------------------+
| 4           | Movement disable     |
+-------------+----------------------+
| 8           | Attackable           |
+-------------+----------------------+
| 16          | Rename in progress   |
+-------------+----------------------+
| 32          | Resting              |
+-------------+----------------------+
| 64          | Unknown              |
+-------------+----------------------+
| 128         | Not attackable       |
+-------------+----------------------+
| 136         | Not PvP enabled      |
+-------------+----------------------+
| 256         | Unknown              |
+-------------+----------------------+
| 512         | Unknown              |
+-------------+----------------------+
| 1024        | Animation frozen     |
+-------------+----------------------+
| 2048        | Unknown              |
+-------------+----------------------+
| 4096        | PvP enabled          |
+-------------+----------------------+
| 8192        | Mounted              |
+-------------+----------------------+
| 16386       | Unknown              |
+-------------+----------------------+
| 32768       | Unknown              |
+-------------+----------------------+
| 65536       | Unknown              |
+-------------+----------------------+
| 131072      | Unknown              |
+-------------+----------------------+
| 262144      | Rotation disabled    |
+-------------+----------------------+
| 524288      | In combat            |
+-------------+----------------------+
| 1048576     | Unknown              |
+-------------+----------------------+
| 2097152     | Unknown              |
+-------------+----------------------+
| 4194304     | Unknown              |
+-------------+----------------------+
| 8388608     | Unknown              |
+-------------+----------------------+
| 16777216    | Unknown              |
+-------------+----------------------+
| 33554432    | Unknown              |
+-------------+----------------------+
| 67108864    | Unknown              |
+-------------+----------------------+
| 134217728   | Unknown              |
+-------------+----------------------+

dynamicflags
------------

Dynamic flags are used to control the visual appearance of a creature
template. The following table provides a list of valid values. Multiple
flags may be combined.

+---------+-----------------------------+-----------------------------------------+
| Value   | Description                 | Comments                                |
+=========+=============================+=========================================+
| 0       | None                        |                                         |
+---------+-----------------------------+-----------------------------------------+
| 1       | Lootable                    |                                         |
+---------+-----------------------------+-----------------------------------------+
| 2       | Track unit                  |                                         |
+---------+-----------------------------+-----------------------------------------+
| 4       | Other tagger                | Makes creature name tag appear grey     |
+---------+-----------------------------+-----------------------------------------+
| 8       | Rooted                      |                                         |
+---------+-----------------------------+-----------------------------------------+
| 16      | Specialinfo                 | Show basic creature stats in tooltip    |
+---------+-----------------------------+-----------------------------------------+
| 32      | Dead                        | Make creature appear dead without tag   |
+---------+-----------------------------+-----------------------------------------+
| 64      | Tapped by all threat list   |                                         |
+---------+-----------------------------+-----------------------------------------+

family
------

The creature's family is set for all creature's with a type of ``1``,
aka. beasts.

+---------+----------------+---------+------------------+
| Value   | Description    | Value   | Description      |
+=========+================+=========+==================+
| 1       | Wolf           | 16      | Voidwalker       |
+---------+----------------+---------+------------------+
| 2       | Cat            | 17      | Succubus         |
+---------+----------------+---------+------------------+
| 3       | Spider         | 19      | Doomguard        |
+---------+----------------+---------+------------------+
| 4       | Bear           | 20      | Scorpid          |
+---------+----------------+---------+------------------+
| 5       | Boar           | 21      | Turtle           |
+---------+----------------+---------+------------------+
| 6       | Crocolisk      | 23      | Imp              |
+---------+----------------+---------+------------------+
| 7       | Carrion Bird   | 24      | Bat              |
+---------+----------------+---------+------------------+
| 8       | Crab           | 25      | Hyena            |
+---------+----------------+---------+------------------+
| 9       | Gorilla        | 26      | Owl              |
+---------+----------------+---------+------------------+
| 11      | Raptor         | 27      | Wind Serpent     |
+---------+----------------+---------+------------------+
| 12      | Tallstrider    | 28      | Remote Control   |
+---------+----------------+---------+------------------+
| 15      | Felhunter      |         |                  |
+---------+----------------+---------+------------------+

*Notice*: It has to be evaluated if creatures of type ``3`` (Demons)
should have their family set, as there are creature families defined for
these. Also, remote control family would probably be having a type of
``9`` since these are mechanical.

trainer\_type
-------------

For creature templates set to be trainers, this details what kind of
trainer the creature is. The following table provides a list of valid
trainer types.

+---------+----------------+
| Value   | Type           |
+=========+================+
| 0       | Class          |
+---------+----------------+
| 1       | Mounts         |
+---------+----------------+
| 2       | Trade skills   |
+---------+----------------+
| 3       | Pets           |
+---------+----------------+

trainer\_spell
--------------

If set to a valid spell identifier from
`Spell.dbc <../dbc/Spell.dbc>`__, this will restrict access to a
profession trainer so that the player needs to already have access to
the spell to access the trainer.

trainer\_class
--------------

The value of this field will restrict access to class and/or pet
trainers, if set to a value corresponding with the class identifiers
from `ChrClasses.dbc <../dbc/ChrClasses.dbc>`__.

+---------+---------------+
| Value   | Description   |
+=========+===============+
| 1       | Warrior       |
+---------+---------------+
| 2       | Paladin       |
+---------+---------------+
| 3       | Hunter        |
+---------+---------------+
| 4       | Rogue         |
+---------+---------------+
| 5       | Priest        |
+---------+---------------+
| 7       | Shaman        |
+---------+---------------+
| 8       | Mage          |
+---------+---------------+
| 9       | Warlock       |
+---------+---------------+
| 11      | Druid         |
+---------+---------------+

*Notice*: pet trainers should always use the Hunter class identifier
``3``.

trainer\_race
-------------

This field allows to restrict a riding trainer to a specific race.
Players not from that race will require exalted reputation with the
trainers race before being able to buy from him. Values in this field
correspond with the content of `ChrRaces.dbc <../dbc/ChrRaces.dbc>`__.

minrangedmg
-----------

Minimum damage the creature deals in ranged combat. This field is
combined with the ranged attackpower field to calculate the damage.

maxrangedmg
-----------

Maximum damage the creature deals in ranged combat. This field is
combined with the ranged attackpower field to calculate the damage.

rangedattackpower
-----------------

The attack power for the creature's ranged attacks.

type
----

The type of the creature. The following table provides a list of valid
values. The values are taken from
`CreatureType.dbc <../dbc/CreatureType.dbc>`__.

+---------+-----------------+
| Value   | Name            |
+=========+=================+
| 1       | Beast           |
+---------+-----------------+
| 2       | Dragonkin       |
+---------+-----------------+
| 3       | Demon           |
+---------+-----------------+
| 4       | Elemental       |
+---------+-----------------+
| 5       | Giant           |
+---------+-----------------+
| 6       | Undead          |
+---------+-----------------+
| 7       | Humanoid        |
+---------+-----------------+
| 8       | Critter         |
+---------+-----------------+
| 9       | Mechanical      |
+---------+-----------------+
| 10      | Not specified   |
+---------+-----------------+
| 11      | Totem           |
+---------+-----------------+

type\_flags
-----------

Type flags *seem* to control what actions a player can perform towards a
creature template.

lootid
------

The field adds loot to a creature template and references the
`creature\_loot\_template <creature_loot_template>`__ tables unique ID
for which the entry is valid.

pickpocketloot
--------------

The field adds pickpocketing loot to a creature template and references
the `pickpocketing\_loot\_template <pickpocketing_loot_template>`__
tables unique ID for which the entry is valid.

skinloot
--------

The field adds skinning loot to a creature template and references the
`skinning\_loot\_template <skinning_loot_template>`__ tables unique ID
for which the entry is valid.

resistance1
-----------

Holy resistance.

resistance2
-----------

Fire resistance.

resistance3
-----------

Nature resistance.

resistance4
-----------

Frost resistance.

resistance5
-----------

Shadow resistance.

resistance6
-----------

Arcane resistance.

PetSpellDataId
--------------

ID that displays what spells the pet has in the client.

mingold
-------

Minimum money the creature drops when killed, in copper.

maxgold
-------

Maximum money the creature drops when killed, in copper.

AIName
------

This string determines which built-in AI script will be used for the
creature template. By default and empty string will lead to the creature
doing nothing. The following table lists all valid entries.

+---------------+------------------------------------------------+
| Value         | Description                                    |
+===============+================================================+
| NullAI        | Do nothing. Same as empty string.              |
+---------------+------------------------------------------------+
| AggressorAI   | Creature attacks when entering aggro radius.   |
+---------------+------------------------------------------------+
| ReactorAI     | Creature attacks only if aggroed by spell.     |
+---------------+------------------------------------------------+
| GuardAI       | Creature is a zone guard.                      |
+---------------+------------------------------------------------+
| PetAI         | Creature is a pet.                             |
+---------------+------------------------------------------------+
| TotemAI       | Creature casts spell from spell1.              |
+---------------+------------------------------------------------+
| EventAI       | Creature uses event based AI.                  |
+---------------+------------------------------------------------+

MovementType
------------

The movement type defines what a creature spawn will behave like after
spawning.

+---------+-----------------------------------------------+
| Value   | Behaviour                                     |
+=========+===============================================+
| 0       | Idle on spawn point                           |
+---------+-----------------------------------------------+
| 1       | Random movement within ``spawndist`` radius   |
+---------+-----------------------------------------------+
| 2       | Waypoint movement                             |
+---------+-----------------------------------------------+

InhabitType
-----------

The inhabit type defines where a creature can move and attack and thus
also influences when a creature will rest.

+---------+-----------------------------+
| Value   | Behaviour                   |
+=========+=============================+
| 1       | Ground movement only        |
+---------+-----------------------------+
| 2       | Water movement only         |
+---------+-----------------------------+
| 3       | Ground and water movement   |
+---------+-----------------------------+
| 4       | Air movement                |
+---------+-----------------------------+

Civilian
--------

Marking a creature template as civilian will prevent it from aggroing
and may influence the honor points gained negatively.

+---------+---------------+
| Value   | Description   |
+=========+===============+
| 0       | No civilian   |
+---------+---------------+
| 1       | Civilian      |
+---------+---------------+

RacialLeader
------------

Determines if a creature template is a racial leader. Racial leaders
will grant increased honor points upon death.

+---------+-------------------+
| Value   | Description       |
+=========+===================+
| 0       | Normal creature   |
+---------+-------------------+
| 1       | Racial leader     |
+---------+-------------------+

RegenHealth
-----------

Controls if a creature template should regenerate it's health or not.

+---------+-------------------+
| Value   | Description       |
+=========+===================+
| 0       | No regeneration   |
+---------+-------------------+
| 1       | Regenerate        |
+---------+-------------------+

equipment\_id
-------------

The field adds equipment to a creature template and references the
`creature\_equip\_template <creature_equip_template>`__ tables unique ID
for which the entry is valid.

trainer\_id
-----------

This field adds a training spells to a creature template and references
the `npc\_trainer\_template <npc_trainer_template>`__ tables unique ID
for which the entry is valid.

vendor\_id
----------

This field adds a vendor items to a creature template and references the
`npc\_vendor\_template <npc_vendor_template>`__ tables unique ID for
which the entry is valid.

mechanic\_immune\_mask
----------------------

This mask can be used to make creatures immune to spell mechanics.
Multiple immunities can be combined.

+---------+------------+-------------+-------------------+
| Value   | Type       | Value       | Type              |
+=========+============+=============+===================+
| 0       | NONE       | 32768       | BANDAGE           |
+---------+------------+-------------+-------------------+
| 1       | CHARM      | 65536       | POLYMORPH         |
+---------+------------+-------------+-------------------+
| 2       | CONFUSED   | 131072      | BANISH            |
+---------+------------+-------------+-------------------+
| 4       | DISARM     | 262144      | SHIELD            |
+---------+------------+-------------+-------------------+
| 8       | DISTRACT   | 524288      | SHACKLE           |
+---------+------------+-------------+-------------------+
| 16      | FEAR       | 1048576     | MOUNT             |
+---------+------------+-------------+-------------------+
| 32      | FUMBLE     | 2097152     | PERSUADE          |
+---------+------------+-------------+-------------------+
| 64      | ROOT       | 4194304     | TURN              |
+---------+------------+-------------+-------------------+
| 128     | PACIFY     | 8388608     | HORROR            |
+---------+------------+-------------+-------------------+
| 256     | SILENCE    | 16777216    | INVULNERABILITY   |
+---------+------------+-------------+-------------------+
| 512     | SLEEP      | 33554432    | INTERRUPT         |
+---------+------------+-------------+-------------------+
| 1024    | SNARE      | 67108864    | DAZE              |
+---------+------------+-------------+-------------------+
| 2048    | STUN       | 134217728   | DISCOVERY         |
+---------+------------+-------------+-------------------+
| 4096    | FREEZE     | 268435456   | IMMUNE\_SHIELD    |
+---------+------------+-------------+-------------------+
| 8192    | KNOCKOUT   | 536870912   | SAPPED            |
+---------+------------+-------------+-------------------+
| 16384   | BLEED      |             |                   |
+---------+------------+-------------+-------------------+

*Notice*: in theory this should somehow relate to
`SpellMechanic.dbc <../dbc/SpellMechanic.dbc>`__ and the immunities list
there, but it does not match. **TODO**

flags\_extra
------------

The extra flags allow to modify special behaviour for a
creature\_template. The following table contains a list of combinable
flags.

+---------+----------------------+-----------------------------------------------+
| Value   | Type                 | Description                                   |
+=========+======================+===============================================+
| 0       | NONE                 | Default: do nothing.                          |
+---------+----------------------+-----------------------------------------------+
| 1       | INSTANCE\_BIND       | Bounds killer’s party to the instance         |
+---------+----------------------+-----------------------------------------------+
| 2       | CIVILIAN             | Makes creature ignore aggro                   |
+---------+----------------------+-----------------------------------------------+
| 4       | NO\_PARRY            | Prohibits from parrying                       |
+---------+----------------------+-----------------------------------------------+
| 8       | NO\_PARRY\_HASTEN    | Parries do not speed up its next attack       |
+---------+----------------------+-----------------------------------------------+
| 16      | NO\_BLOCK            | Prohibits from blocking                       |
+---------+----------------------+-----------------------------------------------+
| 32      | NO\_CRUSH            | Prohibits from dealing crushing blows         |
+---------+----------------------+-----------------------------------------------+
| 64      | NO\_XP\_AT\_KILL     | Creature rewards no XP at kill                |
+---------+----------------------+-----------------------------------------------+
| 128     | INVISIBLE            | Creature invisible for player, e.g triggers   |
+---------+----------------------+-----------------------------------------------+
| 256     | NOT\_TAUNTABLE       | Creature is immune to taunts                  |
+---------+----------------------+-----------------------------------------------+
| 512     | AGGRO\_ZONE          | Sets itself in combat with zone on aggro      |
+---------+----------------------+-----------------------------------------------+
| 1024    | GUARD                | Is zone guard and death will be announced     |
+---------+----------------------+-----------------------------------------------+
| 2048    | NO\_TALKTO\_CREDIT   | Does not give quest credit (temporary)        |
+---------+----------------------+-----------------------------------------------+

ScriptName
----------

To assign a script from the script library to the creature\_template,
set this string to the script's exported name.
