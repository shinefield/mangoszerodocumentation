.. _db-world-dbscripts-on-event:

============================
"dbscripts\_on\_event" table
============================

The ``dbscripts_on_event`` table holds holds scripts which are executed
upon event activation or when a spell with a SPELL\_EFFECT\_SEND\_EVENT
is triggered.

Table structure
---------------

+------------------+-------------------------+--------+-------+-----------+---------+
| Field            | Type                    | Null   | Key   | Default   | Extra   |
+==================+=========================+========+=======+===========+=========+
| id               | mediumint(8) unsigned   | NO     |       | 0         |         |
+------------------+-------------------------+--------+-------+-----------+---------+
| delay            | int(10) unsigned        | NO     |       | 0         |         |
+------------------+-------------------------+--------+-------+-----------+---------+
| command          | mediumint(8) unsigned   | NO     |       | 0         |         |
+------------------+-------------------------+--------+-------+-----------+---------+
| datalong         | mediumint(8) unsigned   | NO     |       | 0         |         |
+------------------+-------------------------+--------+-------+-----------+---------+
| datalong2        | int(10) unsigned        | NO     |       | 0         |         |
+------------------+-------------------------+--------+-------+-----------+---------+
| buddy\_entry     | mediumint(8) unsigned   | NO     |       | 0         |         |
+------------------+-------------------------+--------+-------+-----------+---------+
| search\_radius   | mediumint(8) unsigned   | NO     |       | 0         |         |
+------------------+-------------------------+--------+-------+-----------+---------+
| data\_flags      | tinyint(3) unsigned     | NO     |       | 0         |         |
+------------------+-------------------------+--------+-------+-----------+---------+
| dataint          | int(11)                 | NO     |       | 0         |         |
+------------------+-------------------------+--------+-------+-----------+---------+
| dataint2         | int(11)                 | NO     |       | 0         |         |
+------------------+-------------------------+--------+-------+-----------+---------+
| dataint3         | int(11)                 | NO     |       | 0         |         |
+------------------+-------------------------+--------+-------+-----------+---------+
| dataint4         | int(11)                 | NO     |       | 0         |         |
+------------------+-------------------------+--------+-------+-----------+---------+
| x                | float                   | NO     |       | 0         |         |
+------------------+-------------------------+--------+-------+-----------+---------+
| y                | float                   | NO     |       | 0         |         |
+------------------+-------------------------+--------+-------+-----------+---------+
| z                | float                   | NO     |       | 0         |         |
+------------------+-------------------------+--------+-------+-----------+---------+
| o                | float                   | NO     |       | 0         |         |
+------------------+-------------------------+--------+-------+-----------+---------+
| comments         | varchar(255)            | NO     |       | NULL      |         |
+------------------+-------------------------+--------+-------+-----------+---------+

Fields
------

id
--

This references the parameter for a spell with a
SPELL\_EFFECT\_SEND\_EVENT effect set.

delay
-----

The delay in seconds to apply before starting the script command.
Setting the value to ``0`` will instantly execute the command.

*Notice*: delay is accumulated over all events with identical ``id``
values.

command
-------

The action to execute once the ``delay`` defined has been reached. The
following list shows all available actions.

+---------+------------------------------------------------+----------------------------------------------------------------+
| Value   | Command                                        | Description                                                    |
+=========+================================================+================================================================+
| 0       | SCRIPT\_COMMAND\_TALK                          | Creature will send a text emote (say, yell, whisper)           |
+---------+------------------------------------------------+----------------------------------------------------------------+
| 1       | SCRIPT\_COMMAND\_EMOTE                         | Creature/character will play an emote                          |
+---------+------------------------------------------------+----------------------------------------------------------------+
| 2       | SCRIPT\_COMMAND\_FIELD\_SET                    | Modifies a character variable                                  |
+---------+------------------------------------------------+----------------------------------------------------------------+
| 3       | SCRIPT\_COMMAND\_MOVE\_TO                      | Moves a creature to a new location                             |
+---------+------------------------------------------------+----------------------------------------------------------------+
| 4       | SCRIPT\_COMMAND\_FLAG\_SET                     | Turns on bits on character variable                            |
+---------+------------------------------------------------+----------------------------------------------------------------+
| 5       | SCRIPT\_COMMAND\_FLAG\_REMOVE                  | Turns off bits on character variable                           |
+---------+------------------------------------------------+----------------------------------------------------------------+
| 6       | SCRIPT\_COMMAND\_TELEPORT\_TO                  | Teleports a character to a new location                        |
+---------+------------------------------------------------+----------------------------------------------------------------+
| 7       | SCRIPT\_COMMAND\_QUEST\_EXPLORED               | Marks a quest exploration requirement as done                  |
+---------+------------------------------------------------+----------------------------------------------------------------+
| 8       | SCRIPT\_COMMAND\_KILL\_CREDIT                  | Marks a quest kill requirement as done                         |
+---------+------------------------------------------------+----------------------------------------------------------------+
| 9       | SCRIPT\_COMMAND\_RESPAWN\_GAMEOBJECT           | Respawns a despawned game object                               |
+---------+------------------------------------------------+----------------------------------------------------------------+
| 10      | SCRIPT\_COMMAND\_TEMP\_SUMMON\_CREATURE        | Summons one/multiple temporary creature(s)                     |
+---------+------------------------------------------------+----------------------------------------------------------------+
| 11      | SCRIPT\_COMMAND\_OPEN\_DOOR                    | Opens a game object of type 0 (aka. a door)                    |
+---------+------------------------------------------------+----------------------------------------------------------------+
| 12      | SCRIPT\_COMMAND\_CLOSE\_DOOR                   | Closes a game object of type 0 (aka. a door)                   |
+---------+------------------------------------------------+----------------------------------------------------------------+
| 13      | SCRIPT\_COMMAND\_ACTIVATE\_OBJECT              | Uses a game object                                             |
+---------+------------------------------------------------+----------------------------------------------------------------+
| 14      | SCRIPT\_COMMAND\_REMOVE\_AURA                  | Removes an aura using a spell                                  |
+---------+------------------------------------------------+----------------------------------------------------------------+
| 15      | SCRIPT\_COMMAND\_CAST\_SPELL                   | Cast a spell                                                   |
+---------+------------------------------------------------+----------------------------------------------------------------+
| 16      | SCRIPT\_COMMAND\_PLAY\_SOUND                   | Play a sound entry                                             |
+---------+------------------------------------------------+----------------------------------------------------------------+
| 17      | SCRIPT\_COMMAND\_CREATE\_ITEM                  | Create an item                                                 |
+---------+------------------------------------------------+----------------------------------------------------------------+
| 18      | SCRIPT\_COMMAND\_DESPAWN\_SELF                 | Despawns a creature using an optional delay                    |
+---------+------------------------------------------------+----------------------------------------------------------------+
| 19      | SCRIPT\_COMMAND\_PLAY\_MOVIE                   | Play a move for the targeted character                         |
+---------+------------------------------------------------+----------------------------------------------------------------+
| 20      | SCRIPT\_COMMAND\_MOVEMENT                      | Change the movement type of a creature                         |
+---------+------------------------------------------------+----------------------------------------------------------------+
| 21      | SCRIPT\_COMMAND\_SET\_ACTIVEOBJECT             | Set a creature as active object                                |
+---------+------------------------------------------------+----------------------------------------------------------------+
| 22      | SCRIPT\_COMMAND\_SET\_FACTION                  | Change the faction of a creature                               |
+---------+------------------------------------------------+----------------------------------------------------------------+
| 23      | SCRIPT\_COMMAND\_MORPH\_TO\_ENTRY\_OR\_MODEL   | Changes a creature model displayed                             |
+---------+------------------------------------------------+----------------------------------------------------------------+
| 24      | SCRIPT\_COMMAND\_MOUNT\_TO\_ENTRY\_OR\_MODEL   | Mounts a creature with the given model                         |
+---------+------------------------------------------------+----------------------------------------------------------------+
| 25      | SCRIPT\_COMMAND\_SET\_RUN                      | Let a creature walk or run                                     |
+---------+------------------------------------------------+----------------------------------------------------------------+
| 26      | SCRIPT\_COMMAND\_ATTACK\_START                 | Makes a creature attack within a given radius                  |
+---------+------------------------------------------------+----------------------------------------------------------------+
| 27      | SCRIPT\_COMMAND\_GO\_LOCK\_STATE               | Changes the lock/interaction state of a game object            |
+---------+------------------------------------------------+----------------------------------------------------------------+
| 28      | SCRIPT\_COMMAND\_STAND\_STATE                  | Changes the stand state of a creature                          |
+---------+------------------------------------------------+----------------------------------------------------------------+
| 29      | SCRIPT\_COMMAND\_MODIFY\_NPC\_FLAGS            | Change the ``npcflag`` settings of a creature                  |
+---------+------------------------------------------------+----------------------------------------------------------------+
| 30      | SCRIPT\_COMMAND\_SEND\_TAXI\_PATH              | Puts a character on a given taxi path                          |
+---------+------------------------------------------------+----------------------------------------------------------------+
| 31      | SCRIPT\_COMMAND\_TERMINATE\_SCRIPT             | Stops script execution on a creature if it meets a condition   |
+---------+------------------------------------------------+----------------------------------------------------------------+
| 32      | SCRIPT\_COMMAND\_PAUSE\_WAYPOINTS              | Pause or continue waypoint movement of a creature              |
+---------+------------------------------------------------+----------------------------------------------------------------+
| 33      | SCRIPT\_COMMAND\_RESERVED\_1                   | Reserved for later usage                                       |
+---------+------------------------------------------------+----------------------------------------------------------------+
| 34      | SCRIPT\_COMMAND\_TERMINATE\_COND               | Stops script execution if a condition is met                   |
+---------+------------------------------------------------+----------------------------------------------------------------+
| 35      | SCRIPT\_COMMAND\_TURN\_TO                      | Change a creature orientation towards a target                 |
+---------+------------------------------------------------+----------------------------------------------------------------+

datalong
--------

A multi-purpose field storing raw data as unsigned integer value.

datalong2
---------

A multi-purpose field storing raw data as unsigned integer value.

buddy\_entry
------------

If the command used has a buddy entry, this references either an entry
in the `gameobject\_template <gameobject_template>`__ or
`creature\_template <creature_template>`__ table.

search\_radius
--------------

The range in which the buddy's entry will be search for.

*Notice*: if ``data_flags`` has ``SCRIPT_FLAG_BUDDY_BY_GUID`` set, this
references an entry in the `gameobject <gameobject>`__ or
`creature <creature>`__ table.

data\_flags
-----------

Holds a flag or a combination for flags for the script command. The
following table contains all valid flags

+---------+---------------------------------------+
| Value   | Name                                  |
+=========+=======================================+
| 1       | SCRIPT\_FLAG\_BUDDY\_AS\_TARGET       |
+---------+---------------------------------------+
| 2       | SCRIPT\_FLAG\_REVERSE\_DIRECTION      |
+---------+---------------------------------------+
| 4       | SCRIPT\_FLAG\_SOURCE\_TARGETS\_SELF   |
+---------+---------------------------------------+
| 8       | SCRIPT\_FLAG\_COMMAND\_ADDITIONAL     |
+---------+---------------------------------------+
| 16      | SCRIPT\_FLAG\_BUDDY\_BY\_GUID         |
+---------+---------------------------------------+
| 32      | SCRIPT\_FLAG\_BUDDY\_IS\_PET          |
+---------+---------------------------------------+

dataint
-------

A multi-purpose data field storing signed integer values.

*Notice*: currently these fields are only used as text identifiers for
the ``SCRIPT_COMMAND_TALK`` and ``SCRIPT_COMMAND_TERMINATE_SCRIPT``
commands.

dataint2
--------

A multi-purpose data field storing signed integer values.

*Notice*: currently these fields are only used as text identifiers for
the ``SCRIPT_COMMAND_TALK`` and ``SCRIPT_COMMAND_TERMINATE_SCRIPT``
commands.

dataint3
--------

A multi-purpose data field storing signed integer values.

*Notice*: currently these fields are only used as text identifiers for
the ``SCRIPT_COMMAND_TALK`` and ``SCRIPT_COMMAND_TERMINATE_SCRIPT``
commands.

dataint4
--------

A multi-purpose data field storing signed integer values.

*Notice*: currently these fields are only used as text identifiers for
the ``SCRIPT_COMMAND_TALK`` and ``SCRIPT_COMMAND_TERMINATE_SCRIPT``
commands.

x
-

A X position on the map which the command needs.

y
-

A Y position on the map which the command needs.

z
-

A Z position on the map which the command needs.

o
-

An orientation on the map which the command needs.

comments
--------

A comment describing the purpose of the script.
