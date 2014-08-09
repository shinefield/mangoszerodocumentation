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
| Entry                    | mediumint(8) unsigned   | NO     | PRI   | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| Name                     | char(100)               | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| SubName                  | char(100)               | YES    |       | NULL      |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| MinLevel                 | tinyint(3) unsigned     | NO     |       | 1         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| MaxLevel                 | tinyint(3) unsigned     | NO     |       | 1         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| ModelId1                 | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| ModelId2                 | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| FactionAlliance          | smallint(5) unsigned    | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| FactionHorde             | smallint(5) unsigned    | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| Scale                    | float                   | NO     |       | 1         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| Family                   | tinyint(4)              | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| CreatureType             | tinyint(3) unsigned     | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| InhabitType              | tinyint(3) unsigned     | NO     |       | 3         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| RegenerateStats          | tinyint(3) unsigned     | NO     |       | 3         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| RacialLeader             | tinyint(3) unsigned     | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| NpcFlags                 | int(10) unsigned        | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| UnitFlags                | int(10) unsigned        | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| DynamicFlags             | int(10) unsigned        | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| ExtraFlags               | int(10) unsigned        | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| CreatureTypeFlags        | int(10) unsigned        | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| SpeedWalk                | float                   | NO     |       | 1         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| SpeedRun                 | float                   | NO     |       | 1.14286   |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| UnitClass                | tinyint(3) unsigned     | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| Rank                     | tinyint(3) unsigned     | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| HealthMultiplier         | float                   | NO     |       | 1         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| PowerMultiplier          | float                   | NO     |       | 1         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| DamageMultiplier         | float                   | NO     |       | 1         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| DamageVariance           | float                   | NO     |       | 1         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| ArmorMultiplier          | float                   | NO     |       | 1         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| ExperienceMultiplier     | float                   | NO     |       | 1         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| MinLevelHealth           | int(10) unsigned        | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| MaxLevelHealth           | int(10) unsigned        | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| MinLevelMana             | int(10) unsigned        | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| MaxLevelMana             | int(10) unsigned        | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| MinMeleeDmg              | float                   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| MaxMeleeDmg              | float                   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| MinRangedDmg             | float                   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| MaxRangedDmg             | float                   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| Armor                    | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| MeleeAttackPower         | int(10) unsigned        | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| RangedAttackPower        | smallint(5) unsigned    | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| MeleeBaseAttackTime      | int(10) unsigned        | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| RangedBaseAttackTime     | int(10) unsigned        | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| DamageSchool             | tinyint(4)              | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| MinLootGold              | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| MaxLootGold              | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| LootId                   | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| PickpocketLootId         | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| SkinningLootId           | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| KillCredit1              | int(11) unsigned        | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| KillCredit2              | int(11) unsigned        | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| MechanicImmuneMask       | int(10) unsigned        | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| ResistanceHoly           | smallint(5)             | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| ResistanceFire           | smallint(5)             | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| ResistanceNature         | smallint(5)             | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| ResistanceFrost          | smallint(5)             | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| ResistanceShadow         | smallint(5)             | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| ResistanceArcane         | smallint(5)             | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| PetSpellDataId           | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| MovementType             | tinyint(3) unsigned     | YES    |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| TrainerType              | tinyint(4)              | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| TrainerSpell             | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| TrainerClass             | tinyint(3) unsigned     | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| TrainerRace              | tinyint(3) unsigned     | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| TrainerTemplateId        | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| VendorTemplateId         | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| GossipMenuId             | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| EquipmentTemplateId      | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| Civilian                 | tinyint(3) unsigned     | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| AIName                   | char(64)                | YES    |       | NULL      |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| ScriptName               | char(64)                | YES    |       | NULL      |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+

Fields
------

Entry
-----

The unique identifier of the creature template entry.

Name
----

The creature's name that will be displayed.

SubName
-------

An optional tag, which will be shown below the creature's name.

MinLevel
--------

The minimum level of the creature if the creature has a level range.

MaxLevel
--------

The maximum level of the creature if the creature has a level range.
When added to world, a level in chosen in the specified level range.

ModelId1
--------

A display model identifier for the creature\_template. This references
the `creature\_model\_info <creature_model_info>`__ tables unique ID for
which this entry is valid.

ModelId2
--------

A display model identifier for the creature\_template. This references
the `creature\_model\_info <creature_model_info>`__ tables unique ID for
which this entry is valid.

FactionAlliance
---------------

A faction for creatures on the Alliance side. The value has to match
with a faction template identifier defined in
`FactionTemplate.dbc <../dbc/FactionTemplate.dbc>`__.

.. note::

    This field also controls the creature family assistance
    mechanic. Only creatures with the same faction will assist each other.

FactionHorde
------------

A faction for creatures on the Horde side. The value has to match with a
faction template identifier defined in
`FactionTemplate.dbc <../dbc/FactionTemplate.dbc>`__.

.. note::

    This field also controls the creature family assistance
    mechanic. Only creatures with the same faction will assist each other.

Scale
-----

If non-zero, this field defines how the size of the model appears in
game. If zero, it will use default model size taken from
`CreatureDisplayInfo.dbc <../dbc/CreatureDisplayInfo.dbc>`__.

Family
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

.. note::

    It has to be evaluated if creatures of type ``3`` (Demons)
    should have their family set, as there are creature families defined for
    these. Also, remote control family would probably be having a type of
    ``9`` since these are mechanical.

CreatureType
------------

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

RegenerateStats
----------------

Controls if a creature template should regenerate it's health or not.

+---------+-------------------+
| Value   | Description       |
+=========+===================+
| 0       | No regeneration   |
+---------+-------------------+
| 1       | Regenerate health |
+---------+-------------------+
| 2       | Regenerate power  |
+---------+-------------------+

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

NpcFlags
--------

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

UnitFlags
---------

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

DynamicFlags
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

ExtraFlags
----------

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

CreatureTypeFlags
-----------------

Type flags *seem* to control what actions a player can perform towards a
creature template.

SpeedWalk
---------

Controls how fast the creature can move in walking mode.

SpeedRun
--------

Controls how fast the creature can move in running mode.

UnitClass
---------

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

.. note::

    Depending on the creature's class, you have to make sure that
    the mana values are set properly. E.g. a Warrior or Rogue will not have
    mana set.

Rank
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

HealthMultiplier
----------------

Setting this value to a value smaller or larger than ``1`` will modify
the creature template's health by this factor.

PowerMultiplier
--------------

Setting this value to a value smaller or larger than ``1`` will modify
the creature template's power by this factor.

DamageMultiplier
----------------

Setting this value to a value smaller or larger than ``1`` will modify
the creature template's damage by this factor.

DamageVariance
--------------

**TODO**

ArmorMultiplier
---------------

Setting this value to a value smaller or larger than ``1`` will modify
the creature template's armor by this factor.

ExperienceMultiplier
--------------------

Setting this value to a value smaller or larger than ``1`` will modify
experience gained from the creature template by this factor.

MinLevelHealth
--------------

The minimum health of the creature if the creature has variable health.

MaxLevelHealth
--------------

The maximum health of the creature if the creature has a variable
health. When added to world, the health value is chosen in proportion to
the level chosen.

MinLevelMana
------------

The miminum mana of the creature if the creature has variable mana.

MaxLevelMana
------------

The maximum mana of the creature if the creature has variable mana. When
added to world, the mana value is chosen in proportion to the level
chosen.

MinMeleeDmg
-----------

Minimum damage the creature deals in melee combat. This field is
combined with the attackpower field to calculate the damage.

MaxMeleeDmg
-----------

Maximum damage the creature deals in melee combat. This field is
combined with the attackpower field to calculate the damage.

MinRangedDmg
------------

Minimum damage the creature deals in ranged combat. This field is
combined with the ranged attackpower field to calculate the damage.

MaxRangedDmg
------------

Maximum damage the creature deals in ranged combat. This field is
combined with the ranged attackpower field to calculate the damage.

Armor
-----

The armor value of the creature. It controls how much damage reduction
the creature gets from physical attacks.

MeleeAttackPower
----------------

The attack power for the creature's melee attacks. This field along with
``MinMeleeDmg`` and ``MaxMeleeDmg`` dictate how much the creature will hit for.
The formula for applying correct damages is as follows:

.. code-block:: sql

        UPDATE `creature_template` SET
            `MinMeleeDmg` = <#1>,
            `MaxMeleeDmg` = <#2>,
            `MeleeAttackPower` = ROUND((`MinMeleeDmg` + `MaxMeleeDmg`) / 4 * 7),
            `MinMeleeDmg` = ROUND(`MinMeleeDmg` - `MeleeAttackPower` / 7),
            `MaxMeleeDmg` = ROUND(`MaxMeleeDmg` - `MeleeAttackPower` / 7)
          WHERE `Entry` = ...

In the query above, substitute ``<#1>`` with the minimum damage you want
the creature to deal and ``<#2>`` with the maximum damage you want the
creature to deal.

.. note::

    You might want to double check the calculated values after the
    query has run because a large difference between ``MinMeleeDmg`` and
    ``MaxMeleeDmg`` can cause ``MinMeleeDmg`` to become a negative value.

RangedAttackPower
-----------------

The attack power for the creature's ranged attacks.

MeleeBaseAttackTime
-------------------

A creature's melee attack time in milliseconds.

RangedBaseAttackTime
--------------------

A creature's ranged attack time in milliseconds.

DamageSchool
------------

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

MinLootGold
-----------

Minimum money the creature drops when killed, in copper.

MaxLootGold
-----------

Maximum money the creature drops when killed, in copper.

LootId
------

The field adds loot to a creature template and references the
`creature\_loot\_template <creature_loot_template>`__ tables unique ID
for which the entry is valid.

PickpocketLootId
----------------

The field adds pickpocketing loot to a creature template and references
the `pickpocketing\_loot\_template <pickpocketing_loot_template>`__
tables unique ID for which the entry is valid.

SkinningLootId
--------------

The field adds skinning loot to a creature template and references the
`skinning\_loot\_template <skinning_loot_template>`__ tables unique ID
for which the entry is valid.

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

MechanicImmuneMask
------------------

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

.. note::

    In theory this should somehow relate to
    `SpellMechanic.dbc <../dbc/SpellMechanic.dbc>`__ and the immunities list
    there, but it does not match. **TODO**

ResistanceHoly
--------------

Holy resistance.

ResistanceFire
--------------

Fire resistance.

ResistanceNature
----------------

Nature resistance.

ResistanceFrost
---------------

Frost resistance.

ResistanceShadow
----------------

Shadow resistance.

ResistanceArcane
----------------

Arcane resistance.

PetSpellDataId
--------------

ID that displays what spells the pet has in the client.

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

TrainerType
-----------

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

TrainerSpell
------------

If set to a valid spell identifier from
`Spell.dbc <../dbc/Spell.dbc>`__, this will restrict access to a
profession trainer so that the player needs to already have access to
the spell to access the trainer.

TrainerClass
------------

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

.. note::

    Pet trainers should always use the Hunter class identifier ``3``.

TrainerRace
-----------

This field allows to restrict a riding trainer to a specific race.
Players not from that race will require exalted reputation with the
trainers race before being able to buy from him. Values in this field
correspond with the content of `ChrRaces.dbc <../dbc/ChrRaces.dbc>`__.

TrainerTemplateId
-----------------

This field adds a training spells to a creature template and references
the `npc\_trainer\_template <npc_trainer_template>`__ tables unique ID
for which the entry is valid.

VendorTemplateId
----------------

This field adds a vendor items to a creature template and references the
`npc\_vendor\_template <npc_vendor_template>`__ tables unique ID for
which the entry is valid.

GossipMenuId
------------

This references the `gossip\_menu <gossip_menu>`__ tables unique ID for
which the entry is valid, if the creature\_template should have a gossip
dialogue.

EquipmentTemplateId
-------------------

The field adds equipment to a creature template and references the
`creature\_equip\_template <creature_equip_template>`__ tables unique ID
for which the entry is valid.

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

ScriptName
----------

To assign a script from the script library to the creature\_template,
set this string to the script's exported name.
