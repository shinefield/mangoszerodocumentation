.. _db-world-quest-template:

=======================
"quest\_template" table
=======================

The ``quest_template`` table holds information on every quest that
exists in the game.

Table structure
---------------

+--------------------------+-------------------------+--------+-------+-----------+---------+
| Field                    | Type                    | Null   | Key   | Default   | Extra   |
+==========================+=========================+========+=======+===========+=========+
| entry                    | mediumint(8) unsigned   | NO     | PRI   | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| Method                   | tinyint(3) unsigned     | NO     |       | 2         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| ZoneOrSort               | smallint(6)             | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| MinLevel                 | tinyint(3) unsigned     | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| QuestLevel               | tinyint(3) unsigned     | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| Type                     | smallint(5) unsigned    | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| RequiredClasses          | smallint(5) unsigned    | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| RequiredRaces            | smallint(5) unsigned    | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| RequiredSkill            | smallint(5) unsigned    | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| RequiredSkillValue       | smallint(5) unsigned    | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| RepObjectiveFaction      | smallint(5) unsigned    | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| RepObjectiveValue        | mediumint(9)            | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| RequiredMinRepFaction    | smallint(5) unsigned    | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| RequiredMinRepValue      | mediumint(9)            | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| RequiredMaxRepFaction    | smallint(5) unsigned    | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| RequiredMaxRepValue      | mediumint(9)            | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| SuggestedPlayers         | tinyint(3) unsigned     | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| LimitTime                | int(10) unsigned        | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| QuestFlags               | smallint(5) unsigned    | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| SpecialFlags             | tinyint(3) unsigned     | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| PrevQuestId              | mediumint(9)            | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| NextQuestId              | mediumint(9)            | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| ExclusiveGroup           | mediumint(9)            | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| NextQuestInChain         | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| SrcItemId                | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| SrcItemCount             | tinyint(3) unsigned     | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| SrcSpell                 | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| Title                    | text                    | YES    |       | NULL      |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| Details                  | text                    | YES    |       | NULL      |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| Objectives               | text                    | YES    |       | NULL      |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| OfferRewardText          | text                    | YES    |       | NULL      |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| RequestItemsText         | text                    | YES    |       | NULL      |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| EndText                  | text                    | YES    |       | NULL      |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| ObjectiveText1           | text                    | YES    |       | NULL      |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| ObjectiveText2           | text                    | YES    |       | NULL      |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| ObjectiveText3           | text                    | YES    |       | NULL      |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| ObjectiveText4           | text                    | YES    |       | NULL      |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| ReqItemId1               | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| ReqItemId2               | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| ReqItemId3               | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| ReqItemId4               | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| ReqItemCount1            | smallint(5) unsigned    | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| ReqItemCount2            | smallint(5) unsigned    | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| ReqItemCount3            | smallint(5) unsigned    | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| ReqItemCount4            | smallint(5) unsigned    | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| ReqSourceId1             | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| ReqSourceId2             | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| ReqSourceId3             | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| ReqSourceId4             | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| ReqSourceCount1          | smallint(5) unsigned    | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| ReqSourceCount2          | smallint(5) unsigned    | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| ReqSourceCount3          | smallint(5) unsigned    | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| ReqSourceCount4          | smallint(5) unsigned    | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| ReqCreatureOrGOId1       | mediumint(9)            | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| ReqCreatureOrGOId2       | mediumint(9)            | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| ReqCreatureOrGOId3       | mediumint(9)            | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| ReqCreatureOrGOId4       | mediumint(9)            | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| ReqCreatureOrGOCount1    | smallint(5) unsigned    | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| ReqCreatureOrGOCount2    | smallint(5) unsigned    | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| ReqCreatureOrGOCount3    | smallint(5) unsigned    | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| ReqCreatureOrGOCount4    | smallint(5) unsigned    | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| ReqSpellCast1            | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| ReqSpellCast2            | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| ReqSpellCast3            | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| ReqSpellCast4            | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| RewChoiceItemId1         | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| RewChoiceItemId2         | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| RewChoiceItemId3         | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| RewChoiceItemId4         | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| RewChoiceItemId5         | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| RewChoiceItemId6         | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| RewChoiceItemCount1      | smallint(5) unsigned    | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| RewChoiceItemCount2      | smallint(5) unsigned    | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| RewChoiceItemCount3      | smallint(5) unsigned    | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| RewChoiceItemCount4      | smallint(5) unsigned    | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| RewChoiceItemCount5      | smallint(5) unsigned    | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| RewChoiceItemCount6      | smallint(5) unsigned    | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| RewItemId1               | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| RewItemId2               | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| RewItemId3               | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| RewItemId4               | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| RewItemCount1            | smallint(5) unsigned    | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| RewItemCount2            | smallint(5) unsigned    | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| RewItemCount3            | smallint(5) unsigned    | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| RewItemCount4            | smallint(5) unsigned    | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| RewRepFaction1           | smallint(5) unsigned    | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| RewRepFaction2           | smallint(5) unsigned    | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| RewRepFaction3           | smallint(5) unsigned    | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| RewRepFaction4           | smallint(5) unsigned    | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| RewRepFaction5           | smallint(5) unsigned    | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| RewRepValue1             | mediumint(9)            | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| RewRepValue2             | mediumint(9)            | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| RewRepValue3             | mediumint(9)            | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| RewRepValue4             | mediumint(9)            | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| RewRepValue5             | mediumint(9)            | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| RewOrReqMoney            | int(11)                 | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| RewMoneyMaxLevel         | int(10) unsigned        | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| RewSpell                 | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| RewSpellCast             | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| RewMailTemplateId        | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| RewMailDelaySecs         | int(11) unsigned        | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| PointMapId               | smallint(5) unsigned    | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| PointX                   | float                   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| PointY                   | float                   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| PointOpt                 | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| DetailsEmote1            | smallint(5) unsigned    | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| DetailsEmote2            | smallint(5) unsigned    | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| DetailsEmote3            | smallint(5) unsigned    | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| DetailsEmote4            | smallint(5) unsigned    | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| DetailsEmoteDelay1       | int(11) unsigned        | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| DetailsEmoteDelay2       | int(11) unsigned        | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| DetailsEmoteDelay3       | int(11) unsigned        | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| DetailsEmoteDelay4       | int(11) unsigned        | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| IncompleteEmote          | smallint(5) unsigned    | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| CompleteEmote            | smallint(5) unsigned    | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| OfferRewardEmote1        | smallint(5) unsigned    | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| OfferRewardEmote2        | smallint(5) unsigned    | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| OfferRewardEmote3        | smallint(5) unsigned    | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| OfferRewardEmote4        | smallint(5) unsigned    | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| OfferRewardEmoteDelay1   | int(11) unsigned        | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| OfferRewardEmoteDelay2   | int(11) unsigned        | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| OfferRewardEmoteDelay3   | int(11) unsigned        | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| OfferRewardEmoteDelay4   | int(11) unsigned        | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| StartScript              | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+
| CompleteScript           | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------------------+-------------------------+--------+-------+-----------+---------+

Fields
------

entry
-----

The unique identifier of the quest template entry.

Method
------

This flag decides how a quest will handled by the client. The following
table lists allowed values.

+---------+-----------------------------------------------------------------+
| Value   | Description                                                     |
+=========+=================================================================+
| 0       | Quest will auto-complete. Objectives/details will be skipped.   |
+---------+-----------------------------------------------------------------+
| 1       | Quest is disabled.                                              |
+---------+-----------------------------------------------------------------+
| 2       | Quest is enabled.                                               |
+---------+-----------------------------------------------------------------+

ZoneOrSort
----------

Defines the category under which a quest will be listed in the in-game
quest log. Depending on the sign of the value different category sources
will be used.

-  If the value is > ``0``, the value references an entry from
   `AreaTable.dbc <../dbc/AreaTable.dbc>`__.
-  If the value is < ``0``, the value references an entry from
   `QuestSort.dbc <../dbc/QuestSort.dbc>`__. This is usually the case
   for class or skill related quests.

MinLevel
--------

The lowest level allowed to accept the quest.

QuestLevel
----------

The quest's level. Depending on the quest's level, the experience
rewarded for the quest will be awarded.

-  If a character's level is <= ``QuestLevel``\ +5, full experience will
   be given.
-  If ``QuestLevel`` is set to ``-1``, the character's level will be
   used as ``QuestLevel``.

Type
----

Classifies a quest's difficulty. This references an entry from
`QuestInfo.dbc <../dbc/QuestInfo.dbc>`__. The following table lists
allowed values.

+---------+---------------+
| Value   | Description   |
+=========+===============+
| 0       | Normal        |
+---------+---------------+
| 1       | Elite         |
+---------+---------------+
| 21      | Life          |
+---------+---------------+
| 41      | PvP           |
+---------+---------------+
| 62      | Raid          |
+---------+---------------+
| 81      | Dungeon       |
+---------+---------------+
| 82      | World Event   |
+---------+---------------+
| 83      | Legendary     |
+---------+---------------+

RequiredClasses
---------------

A bit-mask corresponding to class that should get the quest. The value
has to match with classes defined in
`ChrClasses.dbc <../dbc/ChrClasses.dbc>`__.

RequiredRaces
-------------

A bit-mask corresponding to races that should get the spell. The value
has to match with races defined in
`ChrRaces.dbc <../dbc/ChrRaces.dbc>`__.

RequiredSkill
-------------

If the quest requires a skill, set this to a valid identifier
referencing an entry from `SkillLine.dbc <../dbc/SkillLine.dbc>`__.

RequiredSkillValue
------------------

If a ``RequiredSkill`` is set, set this to the skill points required to
aquire the quest.

RepObjectiveFaction
-------------------

If an objective of the quest is to reach a specific reputation with a
faction, this value is set to a faction identifier, referencing an entry
from the `Faction.dbc <../dbc/Faction.dbc>`__ table.

RepObjectiveValue
-----------------

If ``RepObjectiveFaction`` is defined, this value specifies the
reputation value required to achieve.

RequiredMinRepFaction
---------------------

If a quest is obtainable if the character has a specific *minimum*
reputation with a faction, this value is set to a faction identifier,
referencing an entry from the `Faction.dbc <../dbc/Faction.dbc>`__
table.

RequiredMinRepValue
-------------------

If ``RequiredMinRepFaction`` is defined, this value specifies the
reputation value required to obtain the quest.

RequiredMaxRepFaction
---------------------

If a quest is obtainable if the character has a specific *maximum*
reputation with a faction, this value is set to a faction identifier,
referencing an entry from the `Faction.dbc <../dbc/Faction.dbc>`__
table.

RequiredMaxRepValue
-------------------

If ``RequiredManRepFaction`` is defined, this value specifies the
highest reputation value allowed for obtaining the quest.

SuggestedPlayers
----------------

If a quest would require more characters to cooperate for completing the
quest - when the characters are in a valid level range - this value may
be set to the amount of characters recommended to group up for
completing the quest.

LimitTime
---------

Setting this to a value in seconds will put a time limit on a quest,
ticking from the moment a quest was accepted.

QuestFlags
----------

The quest flags give additional details on the quest type. Flags set
here will determine mostly grouping behaviour. Multiple flags may be
combined.

The following table list known flags.

+---------+---------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Value   | Name                            | Description                                                                                                                                                            |
+=========+=================================+========================================================================================================================================================================+
| 0       | QUEST\_FLAGS\_NONE              | Nothing special going on.                                                                                                                                              |
+---------+---------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 1       | QUEST\_FLAGS\_STAY\_ALIVE       | If the character dies, the quest will fail                                                                                                                             |
+---------+---------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 2       | QUEST\_FLAGS\_PARTY\_ACCEPT     | If the character is grouped, all players that can accept this quest will receive confirmation box to accept quest                                                      |
+---------+---------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 4       | QUEST\_FLAGS\_EXPLORATION       | Quest requires the character to explore a zone                                                                                                                         |
+---------+---------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 8       | QUEST\_FLAGS\_SHARABLE          | Quest may be shared with other characters                                                                                                                              |
+---------+---------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 16      | QUEST\_FLAGS\_UNUSED1           | Not used by any quest.                                                                                                                                                 |
+---------+---------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 32      | QUEST\_FLAGS\_EPIC              | Epic class quests?                                                                                                                                                     |
+---------+---------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 64      | QUEST\_FLAGS\_RAID              | Raid quests.                                                                                                                                                           |
+---------+---------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 128     | QUEST\_FLAGS\_UNUSED2           | Not used by any quest.                                                                                                                                                 |
+---------+---------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 256     | QUEST\_FLAGS\_UNK2              | Not used currently: *DELIVER*\ MORE Quest needs more than normal *q-item* drops from mobs                                                                              |
+---------+---------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 512     | QUEST\_FLAGS\_HIDDEN\_REWARDS   | Items and money rewarded only sent in SMSG\_QUESTGIVER\_OFFER\_REWARD (not in SMSG\_QUESTGIVER\_QUEST\_DETAILS or in client quest log(SMSG\_QUEST\_QUERY\_RESPONSE))   |
+---------+---------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 1024    | QUEST\_FLAGS\_AUTO\_REWARDED    | These quests are automatically rewarded on quest complete and they will never appear in quest log client side.                                                         |
+---------+---------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

*Notice*: not all quest flags are currently supported by the core.

SpecialFlags
------------

If quests need any special behaviour, these flags can be used to allow
for it. Multiple special flags may be combined.

Currently the following special cases are available.

+---------+--------------------------------------------------------------------------+
| Value   | Description                                                              |
+=========+==========================================================================+
| 0       | Nothing special going on.                                                |
+---------+--------------------------------------------------------------------------+
| 1       | The quest is repeatable.                                                 |
+---------+--------------------------------------------------------------------------+
| 2       | Quest requires exploration or an event, handled by the script library.   |
+---------+--------------------------------------------------------------------------+

PrevQuestId
-----------

This points to a `quest\_template <quest_template>`__ being a previous
requirement. Depending on the signedness of the value, different
requirements are set.

-  If the value is > ``0``, the given quest needs to be *completed*
   prior to getting this quest.
-  If the value is < ``0``, the given quest has to be active in the
   quest log to get this quest.

NextQuestId
-----------

This points to a `quest\_template <quest_template>`__ being a follow-up.
Depending on the signedness of the value, different requirements are
set.

-  If the value is > ``0``, this contains the quest identifier of the
   next quest, if setting the previous quest identifier on it is not
   sufficient.
-  If the value is < ``0``, this contains a quest identifier for quests
   where multiple follow-ups are possible. Previous quest identifier can
   be set to this quest identifier, too.

ExclusiveGroup
--------------

Allows to group multiple quests into a group, where only one quest can
be completed from, or all quests need to be completed.

-  If the value is > ``0``, all quests having this value set, will be
   put into a group of which only one quest may be completed to get this
   quest.
-  If the value is < ``0``, all quests having this value set, will be
   put into a group of which all quests have to be completed to get this
   quest.

NextQuestInChain
----------------

If ending a quest should immediately start a new quest set this to a
quest identifier referencing the `quest\_template <quest_template>`__
table.

SrcItemId
---------

If starting a quest should give items to the character, set this field
to an item identifier referencing the `item\_template <item_template>`__
table.

SrcItemCount
------------

If ``SrcItemId`` is set, this can be set to the amount of item copies to
give to the character.

SrcSpell
--------

If a spell should be casted on a character upon starting the quest, set
this to a spell identifier referencing the
`Spell.dbc <../dbc/Spell.dbc>`__ table.

Title
-----

The title of the quest.

Details
-------

The quest text, supporting a few variables to insert character related
data into the quest's text.

+---------+-------------------------------------------------------------------------------------------------------------------------------+
| Value   | Description                                                                                                                   |
+=========+===============================================================================================================================+
| $B      | Line break                                                                                                                    |
+---------+-------------------------------------------------------------------------------------------------------------------------------+
| $N      | Character name                                                                                                                |
+---------+-------------------------------------------------------------------------------------------------------------------------------+
| $R      | Character race                                                                                                                |
+---------+-------------------------------------------------------------------------------------------------------------------------------+
| $C      | Character class                                                                                                               |
+---------+-------------------------------------------------------------------------------------------------------------------------------+
| $G m:f  | Inserts string based on character gender. Example: ``Such a generous $G man:woman.`` The order male:female needs to be kept.  |
+---------+-------------------------------------------------------------------------------------------------------------------------------+

Objectives
----------

The quest's objective in text form. If the quest should auto-complete,
leave this empty.

OfferRewardText
---------------

The text sent to a character when talking to the quest giver, and having
completed the quest. Variables are supported.

+---------+-------------------------------------------------------------------------------------------------------------------------------+
| Value   | Description                                                                                                                   |
+=========+===============================================================================================================================+
| $B      | Line break                                                                                                                    |
+---------+-------------------------------------------------------------------------------------------------------------------------------+
| $N      | Character name                                                                                                                |
+---------+-------------------------------------------------------------------------------------------------------------------------------+
| $R      | Character race                                                                                                                |
+---------+-------------------------------------------------------------------------------------------------------------------------------+
| $C      | Character class                                                                                                               |
+---------+-------------------------------------------------------------------------------------------------------------------------------+
| $G m:f  | Inserts string based on character gender. Example: ``Such a generous $G man:woman.`` The order male:female needs to be kept.  |
+---------+-------------------------------------------------------------------------------------------------------------------------------+

RequestItemsText
----------------

The text sent to a character when talking to a quest giver, and not
missing to fulfill the quest's requirements. Variables are supported.

+---------+-------------------------------------------------------------------------------------------------------------------------------+
| Value   | Description                                                                                                                   |
+=========+===============================================================================================================================+
| $B      | Line break                                                                                                                    |
+---------+-------------------------------------------------------------------------------------------------------------------------------+
| $N      | Character name                                                                                                                |
+---------+-------------------------------------------------------------------------------------------------------------------------------+
| $R      | Character race                                                                                                                |
+---------+-------------------------------------------------------------------------------------------------------------------------------+
| $C      | Character class                                                                                                               |
+---------+-------------------------------------------------------------------------------------------------------------------------------+
| $G m:f  | Inserts string based on character gender. Example: ``Such a generous $G man:woman.`` The order male:female needs to be kept.  |
+---------+-------------------------------------------------------------------------------------------------------------------------------+

EndText
-------

If the quest's ``SpecialFlag`` requires and action validated by the
script library this text will be sent to the character.

ObjectiveText1
--------------

Set to a text string, to show up as requirement in the quest log entry.

ObjectiveText2
--------------

Set to a text string, to show up as requirement in the quest log entry.

ObjectiveText3
--------------

Set to a text string, to show up as requirement in the quest log entry.

ObjectiveText4
--------------

Set to a text string, to show up as requirement in the quest log entry.

ReqItemId1
----------

If set to an item identifier, this references an entry in the
`item\_template <item_template>`__ table which is required to complete
the quest.

ReqItemId2
----------

If set to an item identifier, this references an entry in the
`item\_template <item_template>`__ table which is required to complete
the quest.

ReqItemId3
----------

If set to an item identifier, this references an entry in the
`item\_template <item_template>`__ table which is required to complete
the quest.

ReqItemId4
----------

If set to an item identifier, this references an entry in the
`item\_template <item_template>`__ table which is required to complete
the quest.

ReqItemCount1
-------------

If ``ReqItemId1`` is set, this defines the amount of items needed to
complete the quest.

ReqItemCount2
-------------

If ``ReqItemId2`` is set, this defines the amount of items needed to
complete the quest.

ReqItemCount3
-------------

If ``ReqItemId3`` is set, this defines the amount of items needed to
complete the quest.

ReqItemCount4
-------------

If ``ReqItemId4`` is set, this defines the amount of items needed to
complete the quest.

ReqSourceId1
------------

If the quest requires items created by using another item, set this to
an item identifier, referencing the creating items entry in the
`item\_template <item_template>`__ table.

*Notice*: this is required to decide if these items should be included
in loot or not.

ReqSourceId2
------------

If the quest requires items created by using another item, set this to
an item identifier, referencing the creating items entry in the
`item\_template <item_template>`__ table.

*Notice*: this is required to decide if these items should be included
in loot or not.

ReqSourceId3
------------

If the quest requires items created by using another item, set this to
an item identifier, referencing the creating items entry in the
`item\_template <item_template>`__ table.

*Notice*: this is required to decide if these items should be included
in loot or not.

ReqSourceId4
------------

If the quest requires items created by using another item, set this to
an item identifier, referencing the creating items entry in the
`item\_template <item_template>`__ table.

*Notice*: this is required to decide if these items should be included
in loot or not.

ReqSourceCount1
---------------

If ``ReqSourceId1`` is set, set this to the amount of required items.

ReqSourceCount2
---------------

If ``ReqSourceId2`` is set, set this to the amount of required items.

ReqSourceCount3
---------------

If ``ReqSourceId3`` is set, set this to the amount of required items.

ReqSourceCount4
---------------

If ``ReqSourceId4`` is set, set this to the amount of required items.

ReqCreatureOrGOId1
------------------

If the quest targets creatures or game objects, this references their
unique identifier.

-  If the value is > ``0``, this references an entry in the
   `creature\_template <creature_template>`__ table.
-  If the value is < ``0``, this references an entry in the
   `gameobject\_template <gameobject_template>`__ table.

ReqCreatureOrGOId2
------------------

If the quest targets creatures or game objects, this references their
unique identifier.

-  If the value is > ``0``, this references an entry in the
   `creature\_template <creature_template>`__ table.
-  If the value is < ``0``, this references an entry in the
   `gameobject\_template <gameobject_template>`__ table.

ReqCreatureOrGOId3
------------------

If the quest targets creatures or game objects, this references their
unique identifier.

-  If the value is > ``0``, this references an entry in the
   `creature\_template <creature_template>`__ table.
-  If the value is < ``0``, this references an entry in the
   `gameobject\_template <gameobject_template>`__ table.

ReqCreatureOrGOId4
------------------

If the quest targets creatures or game objects, this references their
unique identifier.

-  If the value is > ``0``, this references an entry in the
   `creature\_template <creature_template>`__ table.
-  If the value is < ``0``, this references an entry in the
   `gameobject\_template <gameobject_template>`__ table.

ReqCreatureOrGOCount1
---------------------

The amount of creatures or game objects required for the quest.

ReqCreatureOrGOCount2
---------------------

The amount of creatures or game objects required for the quest.

ReqCreatureOrGOCount3
---------------------

The amount of creatures or game objects required for the quest.

ReqCreatureOrGOCount4
---------------------

The amount of creatures or game objects required for the quest.

ReqSpellCast1
-------------

Set to an entry referencing an entry from
`Spell.dbc <../dbc/Spell.dbc>`__ table to require a spell to be cast.
Spells usually need a target identifier set in the
``ReqCreatureOrGOId1``.

If a spell has an effect to send and event or signal quest completion,
targets do not have to be set.

ReqSpellCast2
-------------

Set to an entry referencing an entry from
`Spell.dbc <../dbc/Spell.dbc>`__ table to require a spell to be cast.
Spells usually need a target identifier set in the
``ReqCreatureOrGOId2``.

If a spell has an effect to send and event or signal quest completion,
targets do not have to be set.

ReqSpellCast3
-------------

Set to an entry referencing an entry from
`Spell.dbc <../dbc/Spell.dbc>`__ table to require a spell to be cast.
Spells usually need a target identifier set in the
``ReqCreatureOrGOId3``.

If a spell has an effect to send and event or signal quest completion,
targets do not have to be set.

ReqSpellCast4
-------------

Set to an entry referencing an entry from
`Spell.dbc <../dbc/Spell.dbc>`__ table to require a spell to be cast.
Spells usually need a target identifier set in the
``ReqCreatureOrGOId4``.

If a spell has an effect to send and event or signal quest completion,
targets do not have to be set.

RewChoiceItemId1
----------------

If the quest allow to chose between multiple items as reward, this
contains an item identifier, referencing the creating items entry in the
`item\_template <item_template>`__ table.

RewChoiceItemId2
----------------

If the quest allow to chose between multiple items as reward, this
contains an item identifier, referencing the creating items entry in the
`item\_template <item_template>`__ table.

RewChoiceItemId3
----------------

If the quest allow to chose between multiple items as reward, this
contains an item identifier, referencing the creating items entry in the
`item\_template <item_template>`__ table.

RewChoiceItemId4
----------------

If the quest allow to chose between multiple items as reward, this
contains an item identifier, referencing the creating items entry in the
`item\_template <item_template>`__ table.

RewChoiceItemId5
----------------

If the quest allow to chose between multiple items as reward, this
contains an item identifier, referencing the creating items entry in the
`item\_template <item_template>`__ table.

RewChoiceItemId6
----------------

If the quest allow to chose between multiple items as reward, this
contains an item identifier, referencing the creating items entry in the
`item\_template <item_template>`__ table.

RewChoiceItemCount1
-------------------

If ``RewChoiceItemId1`` contains an item identifier, this defines the
number of charges available for the rewarded item.

RewChoiceItemCount2
-------------------

If ``RewChoiceItemId2`` contains an item identifier, this defines the
number of charges available for the rewarded item.

RewChoiceItemCount3
-------------------

If ``RewChoiceItemId3`` contains an item identifier, this defines the
number of charges available for the rewarded item.

RewChoiceItemCount4
-------------------

If ``RewChoiceItemId4`` contains an item identifier, this defines the
number of charges available for the rewarded item.

RewChoiceItemCount5
-------------------

If ``RewChoiceItemId5`` contains an item identifier, this defines the
number of charges available for the rewarded item.

RewChoiceItemCount6
-------------------

If ``RewChoiceItemId6`` contains an item identifier, this defines the
number of charges available for the rewarded item.

RewItemId1
----------

If the quest rewards items without any choice, this contains an item
identifier, referencing the creating items entry in the
`item\_template <item_template>`__ table.

RewItemId2
----------

If the quest rewards items without any choice, this contains an item
identifier, referencing the creating items entry in the
`item\_template <item_template>`__ table.

RewItemId3
----------

If the quest rewards items without any choice, this contains an item
identifier, referencing the creating items entry in the
`item\_template <item_template>`__ table.

RewItemId4
----------

If the quest rewards items without any choice, this contains an item
identifier, referencing the creating items entry in the
`item\_template <item_template>`__ table.

RewItemCount1
-------------

If ``RewItemId1`` contains an item identifier, this defines the amount
if items to be rewarded.

RewItemCount2
-------------

If ``RewItemId2`` contains an item identifier, this defines the amount
if items to be rewarded.

RewItemCount3
-------------

If ``RewItemId3`` contains an item identifier, this defines the amount
if items to be rewarded.

RewItemCount4
-------------

If ``RewItemId4`` contains an item identifier, this defines the amount
if items to be rewarded.

RewRepFaction1
--------------

If the quest should reward reputation towards a faction, this references
a faction identifier from the `Faction.dbc <../dbc/Faction.dbc>`__
table.

*Notice*: this is intended to reward extra reputation. Normal reputation
is awarded automatically by the server.

RewRepFaction2
--------------

If the quest should reward reputation towards a faction, this references
a faction identifier from the `Faction.dbc <../dbc/Faction.dbc>`__
table.

*Notice*: this is intended to reward extra reputation. Normal reputation
is awarded automatically by the server.

RewRepFaction3
--------------

If the quest should reward reputation towards a faction, this references
a faction identifier from the `Faction.dbc <../dbc/Faction.dbc>`__
table.

*Notice*: this is intended to reward extra reputation. Normal reputation
is awarded automatically by the server.

RewRepFaction4
--------------

If the quest should reward reputation towards a faction, this references
a faction identifier from the `Faction.dbc <../dbc/Faction.dbc>`__
table.

*Notice*: this is intended to reward extra reputation. Normal reputation
is awarded automatically by the server.

RewRepFaction5
--------------

If the quest should reward reputation towards a faction, this references
a faction identifier from the `Faction.dbc <../dbc/Faction.dbc>`__
table.

*Notice*: this is intended to reward extra reputation. Normal reputation
is awarded automatically by the server.

RewRepValue1
------------

If ``RewRepFaction1`` references a faction, this defines the amount of
reputation gain or loss for the referenced faction.

RewRepValue2
------------

If ``RewRepFaction2`` references a faction, this defines the amount of
reputation gain or loss for the referenced faction.

RewRepValue3
------------

If ``RewRepFaction3`` references a faction, this defines the amount of
reputation gain or loss for the referenced faction.

RewRepValue4
------------

If ``RewRepFaction4`` references a faction, this defines the amount of
reputation gain or loss for the referenced faction.

RewRepValue5
------------

If ``RewRepFaction5`` references a faction, this defines the amount of
reputation gain or loss for the referenced faction.

RewOrReqMoney
-------------

This field can be used to either require money for starting the quest,
or award money for completing the quest.

-  If set to a value > ``0``, the quest will reward money upon
   completion
-  If set to a value < ``0``, the quest will require money to accept
   it.s

RewMoneyMaxLevel
----------------

The value of this field decides how much experience or money (at level
60) a quest will reward.

Experience is calculated as follows: ``RewMoneyMaxLevel`` / 0.6

RewSpell
--------

If a spell should be shown as being casted as quest reward, set this to
a spell identifier referencing the `Spell.dbc <../dbc/Spell.dbc>`__
table.

*Notice*: if ``RewSpellCast`` is set, this spell will only be shown, but
not casted.

RewSpellCast
------------

If a spell should be casted as quest reward different from the spell
shown as quest reward, set this to a spell identifier referencing the
`Spell.dbc <../dbc/Spell.dbc>`__ table.

RewMailTemplateId
-----------------

If upon completion a quest should send out mail, this can be set to
reference a mail template identifier in the
`MailTemplate.dbc <../dbc/MailTemplate.dbc>`__ table.

RewMailDelaySecs
----------------

The number of seconds to wait before sending the reward mail.

PointMapId
----------

References an entry in the `points\_of\_interest <points_of_interest>`__
table, if it should be shown while the quest is active.

PointX
------

If a point of interest should be shown while the quest is active, this
will contain the X coordinate.

PointY
------

If a point of interest should be shown while the quest is active, this
will contain the Y coordinate.

PointOpt
--------

**TODO**

DetailsEmote1
-------------

If an emote should be shown upon displaying quest details, this
references the emotes identifier in the
`Emotes.dbc <../dbc/Emotes.dbc>`__ table.

DetailsEmote2
-------------

If an emote should be shown upon displaying quest details, this
references the emotes identifier in the
`Emotes.dbc <../dbc/Emotes.dbc>`__ table.

DetailsEmote3
-------------

If an emote should be shown upon displaying quest details, this
references the emotes identifier in the
`Emotes.dbc <../dbc/Emotes.dbc>`__ table.

DetailsEmote4
-------------

If an emote should be shown upon displaying quest details, this
references the emotes identifier in the
`Emotes.dbc <../dbc/Emotes.dbc>`__ table.

DetailsEmoteDelay1
------------------

The number of seconds to delay the emote, if one is reference in the
``DetailsEmote1`` column.

DetailsEmoteDelay2
------------------

The number of seconds to delay the emote, if one is reference in the
``DetailsEmote2`` column.

DetailsEmoteDelay3
------------------

The number of seconds to delay the emote, if one is reference in the
``DetailsEmote3`` column.

DetailsEmoteDelay4
------------------

The number of seconds to delay the emote, if one is reference in the
``DetailsEmote4`` column.

IncompleteEmote
---------------

If an emote should be shown upon displaying the incomplete quest text,
this references the emotes identifier in the
`Emotes.dbc <../dbc/Emotes.dbc>`__ table.

CompleteEmote
-------------

If an emote should be shown upon displaying the quest completion text,
this references the emotes identifier in the
`Emotes.dbc <../dbc/Emotes.dbc>`__ table.

OfferRewardEmote1
-----------------

If an emote should be shown upon displaying rewarding the quest, this
references the emotes identifier in the
`Emotes.dbc <../dbc/Emotes.dbc>`__ table.

OfferRewardEmote2
-----------------

If an emote should be shown upon displaying rewarding the quest, this
references the emotes identifier in the
`Emotes.dbc <../dbc/Emotes.dbc>`__ table.

OfferRewardEmote3
-----------------

If an emote should be shown upon displaying rewarding the quest, this
references the emotes identifier in the
`Emotes.dbc <../dbc/Emotes.dbc>`__ table.

OfferRewardEmote4
-----------------

If an emote should be shown upon displaying rewarding the quest, this
references the emotes identifier in the
`Emotes.dbc <../dbc/Emotes.dbc>`__ table.

OfferRewardEmoteDelay1
----------------------

The number of seconds the delay the emote, if one is referenced in the
``OfferRewardEmote1`` column.

OfferRewardEmoteDelay2
----------------------

The number of seconds the delay the emote, if one is referenced in the
``OfferRewardEmote2`` column.

OfferRewardEmoteDelay3
----------------------

The number of seconds the delay the emote, if one is referenced in the
``OfferRewardEmote3`` column.

OfferRewardEmoteDelay4
----------------------

The number of seconds the delay the emote, if one is referenced in the
``OfferRewardEmote4`` column.

StartScript
-----------

If a script should be executed on quest start, this references an entry
in the `dbscripts\_on\_quest\_start <dbscripts_on_quest_start>`__ table.

CompleteScript
--------------

If a script should be executed on quest end, this references an entry in
the `dbscripts\_on\_quest\_end <dbscripts_on_quest_end>`__ table.
