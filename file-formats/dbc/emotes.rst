.. _file-formats-dbc-emotes:

==========
Emotes.dbc
==========

The *emotes* table contains definitions for available /emote commands.

Table structure
---------------

+------+----------------------+--------------------+-----------+---------------------------------------------------------------+
| ID   | Name                 | Type               | Default   | Description                                                   |
+======+======================+====================+===========+===============================================================+
| 1    | ID                   | Integer            | -         | Unique ID                                                     |
+------+----------------------+--------------------+-----------+---------------------------------------------------------------+
| 2    | emoteSlashCommand    | String             | -         | The emote command name, as referenced in-game, e.g. in Lua.   |
+------+----------------------+--------------------+-----------+---------------------------------------------------------------+
| 3    | animationData        | Integer            | 0         | The animation to play when executing the emote.               |
+------+----------------------+--------------------+-----------+---------------------------------------------------------------+
| 4    | emoteFlags           | Integer (signed)   | 0         | See below.                                                    |
+------+----------------------+--------------------+-----------+---------------------------------------------------------------+
| 5    | emoteSpecProc        | Integer (signed)   | 0         | See below.                                                    |
+------+----------------------+--------------------+-----------+---------------------------------------------------------------+
| 6    | emoteSpecProcParam   | Integer (signed)   | 0         | Last frame of the emote animation.                            |
+------+----------------------+--------------------+-----------+---------------------------------------------------------------+
| 7    | eventSoundEntry      | Integer            | 0         | The sound to be played while executing the emote.             |
+------+----------------------+--------------------+-----------+---------------------------------------------------------------+

Fields
------

emoteFlags
~~~~~~~~~~

-  ``0000 0000 0000 1000`` / 8: Talk,
-  ``0000 0000 0001 0000`` / 16: Question,
-  ``0000 0000 0010 0000`` / 32: Exclamation,
-  ``0000 0000 0100 0000`` / 64: Shout,
-  ``0000 0001 0000 0000`` / 256: Laugh.

emoteSpecProc
~~~~~~~~~~~~~

-  ``0``: perform emote once,
-  ``1``: loop emote,
-  ``2``: loop emote with sound.

Relations
---------

-  ``animationData`` references the primary key of ``AnimationData.dbc``.
-  ``eventSoundEntry`` references the primary key of ``SoundEntries.dbc``.
