.. _db-world-npc-text:

=================
"npc\_text" table
=================

The ``npc_text`` table holds the texts that are used for gossip.

Table structure
---------------

+-----------------+-------------------------+--------+-------+-----------+---------+
| Field           | Type                    | Null   | Key   | Default   | Extra   |
+=================+=========================+========+=======+===========+=========+
| ID              | mediumint(8) unsigned   | NO     | PRI   | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| text0\_0        | longtext                | YES    |       | NULL      |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| text0\_1        | longtext                | YES    |       | NULL      |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| lang0           | tinyint(3) unsigned     | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| prob0           | float                   | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| em0\_0\_delay   | smallint(5) unsigned    | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| em0\_0          | smallint(5) unsigned    | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| em0\_1\_delay   | smallint(5) unsigned    | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| em0\_1          | smallint(5) unsigned    | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| em0\_2\_delay   | smallint(5) unsigned    | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| em0\_2          | smallint(5) unsigned    | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| text1\_0        | longtext                | YES    |       | NULL      |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| text1\_1        | longtext                | YES    |       | NULL      |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| lang1           | tinyint(3) unsigned     | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| prob1           | float                   | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| em1\_0\_delay   | smallint(5) unsigned    | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| em1\_0          | smallint(5) unsigned    | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| em1\_1\_delay   | smallint(5) unsigned    | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| em1\_1          | smallint(5) unsigned    | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| em1\_2\_delay   | smallint(5) unsigned    | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| em1\_2          | smallint(5) unsigned    | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| text2\_0        | longtext                | YES    |       | NULL      |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| text2\_1        | longtext                | YES    |       | NULL      |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| lang2           | tinyint(3) unsigned     | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| prob2           | float                   | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| em2\_0\_delay   | smallint(5) unsigned    | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| em2\_0          | smallint(5) unsigned    | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| em2\_1\_delay   | smallint(5) unsigned    | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| em2\_1          | smallint(5) unsigned    | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| em2\_2\_delay   | smallint(5) unsigned    | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| em2\_2          | smallint(5) unsigned    | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| text3\_0        | longtext                | YES    |       | NULL      |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| text3\_1        | longtext                | YES    |       | NULL      |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| lang3           | tinyint(3) unsigned     | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| prob3           | float                   | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| em3\_0\_delay   | smallint(5) unsigned    | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| em3\_0          | smallint(5) unsigned    | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| em3\_1\_delay   | smallint(5) unsigned    | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| em3\_1          | smallint(5) unsigned    | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| em3\_2\_delay   | smallint(5) unsigned    | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| em3\_2          | smallint(5) unsigned    | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| text4\_0        | longtext                | YES    |       | NULL      |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| text4\_1        | longtext                | YES    |       | NULL      |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| lang4           | tinyint(3) unsigned     | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| prob4           | float                   | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| em4\_0\_delay   | smallint(5) unsigned    | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| em4\_0          | smallint(5) unsigned    | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| em4\_1\_delay   | smallint(5) unsigned    | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| em4\_1          | smallint(5) unsigned    | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| em4\_2\_delay   | smallint(5) unsigned    | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| em4\_2          | smallint(5) unsigned    | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| text5\_0        | longtext                | YES    |       | NULL      |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| text5\_1        | longtext                | YES    |       | NULL      |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| lang5           | tinyint(3) unsigned     | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| prob5           | float                   | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| em5\_0\_delay   | smallint(5) unsigned    | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| em5\_0          | smallint(5) unsigned    | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| em5\_1\_delay   | smallint(5) unsigned    | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| em5\_1          | smallint(5) unsigned    | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| em5\_2\_delay   | smallint(5) unsigned    | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| em5\_2          | smallint(5) unsigned    | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| text6\_0        | longtext                | YES    |       | NULL      |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| text6\_1        | longtext                | YES    |       | NULL      |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| lang6           | tinyint(3) unsigned     | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| prob6           | float                   | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| em6\_0\_delay   | smallint(5) unsigned    | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| em6\_0          | smallint(5) unsigned    | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| em6\_1\_delay   | smallint(5) unsigned    | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| em6\_1          | smallint(5) unsigned    | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| em6\_2\_delay   | smallint(5) unsigned    | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| em6\_2          | smallint(5) unsigned    | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| text7\_0        | longtext                | YES    |       | NULL      |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| text7\_1        | longtext                | YES    |       | NULL      |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| lang7           | tinyint(3) unsigned     | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| prob7           | float                   | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| em7\_0\_delay   | smallint(5) unsigned    | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| em7\_0          | smallint(5) unsigned    | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| em7\_1\_delay   | smallint(5) unsigned    | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| em7\_1          | smallint(5) unsigned    | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| em7\_2\_delay   | smallint(5) unsigned    | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+
| em7\_2          | smallint(5) unsigned    | NO     |       | 0         |         |
+-----------------+-------------------------+--------+-------+-----------+---------+

Fields
------

ID
--

The unique identifier of the text entry. Please note that the identifier
is acquired from the game client by parsing the local *WDB* cache files.

It is unknown if text identifiers required a specific identifier to
work.

text0\_0
--------

This is the locale text that is displayed if the creature is male.

text0\_1
--------

This is the locale text that is displayed if the creature is female.

lang0
-----

The language of the text in game.

prob0
-----

This is the probability that the creature will say this text.

em0\_0\_delay
-------------

Time to wait before the first emote is played.

em0\_0
------

Emote to play when text is displayed.

em0\_1\_delay
-------------

Time to wait after the first emote are played, before the second emote
gets played.

em0\_1
------

Second emote to play when text is displayed.

em0\_2\_delay
-------------

Time to wait after the second emote are played, before the third emote
gets played.

em0\_2
------

Third emote to play when text is displayed.

text1\_0
--------

This is the locale text that is displayed if the creature is male.

text1\_1
--------

This is the locale text that is displayed if the creature is female.

lang1
-----

The language of the text in game.

prob1
-----

This is the probability that the creature will say this text.

em1\_0\_delay
-------------

Time to wait before the first emote is played.

em1\_0
------

Emote to play when text is displayed.

em1\_1\_delay
-------------

Time to wait after the first emote are played, before the second emote
gets played.

em1\_1
------

Second emote to play when text is displayed.

em1\_2\_delay
-------------

Time to wait after the second emote are played, before the third emote
gets played.

em1\_2
------

Third emote to play when text is displayed.

text2\_0
--------

This is the locale text that is displayed if the creature is male.

text2\_1
--------

This is the locale text that is displayed if the creature is female.

lang2
-----

The language of the text in game.

prob2
-----

This is the probability that the creature will say this text.

em2\_0\_delay
-------------

Time to wait before the first emote is played.

em2\_0
------

Emote to play when text is displayed.

em2\_1\_delay
-------------

Time to wait after the first emote are played, before the second emote
gets played.

em2\_1
------

Second emote to play when text is displayed.

em2\_2\_delay
-------------

Time to wait after the second emote are played, before the third emote
gets played.

em2\_2
------

Third emote to play when text is displayed.

text3\_0
--------

This is the locale text that is displayed if the creature is male.

text3\_1
--------

This is the locale text that is displayed if the creature is female.

lang3
-----

The language of the text in game.

prob3
-----

This is the probability that the creature will say this text.

em3\_0\_delay
-------------

Time to wait before the first emote is played.

em3\_0
------

Emote to play when text is displayed.

em3\_1\_delay
-------------

Time to wait after the first emote are played, before the second emote
gets played.

em3\_1
------

Second emote to play when text is displayed.

em3\_2\_delay
-------------

Time to wait after the second emote are played, before the third emote
gets played.

em3\_2
------

Third emote to play when text is displayed.

text4\_0
--------

This is the locale text that is displayed if the creature is male.

text4\_1
--------

This is the locale text that is displayed if the creature is female.

lang4
-----

The language of the text in game.

prob4
-----

This is the probability that the creature will say this text.

em4\_0\_delay
-------------

Time to wait before the first emote is played.

em4\_0
------

Emote to play when text is displayed.

em4\_1\_delay
-------------

Time to wait after the first emote are played, before the second emote
gets played.

em4\_1
------

Second emote to play when text is displayed.

em4\_2\_delay
-------------

Time to wait after the second emote are played, before the third emote
gets played.

em4\_2
------

Third emote to play when text is displayed.

text5\_0
--------

This is the locale text that is displayed if the creature is male.

text5\_1
--------

This is the locale text that is displayed if the creature is female.

lang5
-----

The language of the text in game.

prob5
-----

This is the probability that the creature will say this text.

em5\_0\_delay
-------------

Time to wait before the first emote is played.

em5\_0
------

Emote to play when text is displayed.

em5\_1\_delay
-------------

Time to wait after the first emote are played, before the second emote
gets played.

em5\_1
------

Second emote to play when text is displayed.

em5\_2\_delay
-------------

Time to wait after the second emote are played, before the third emote
gets played.

em5\_2
------

Third emote to play when text is displayed.

text6\_0
--------

This is the locale text that is displayed if the creature is male.

text6\_1
--------

This is the locale text that is displayed if the creature is female.

lang6
-----

The language of the text in game.

prob6
-----

This is the probability that the creature will say this text.

em6\_0\_delay
-------------

Time to wait before the first emote is played.

em6\_0
------

Emote to play when text is displayed.

em6\_1\_delay
-------------

Time to wait after the first emote are played, before the second emote
gets played.

em6\_1
------

Second emote to play when text is displayed.

em6\_2\_delay
-------------

Time to wait after the second emote are played, before the third emote
gets played.

em6\_2
------

Third emote to play when text is displayed.

text7\_0
--------

This is the locale text that is displayed if the creature is male.

text7\_1
--------

This is the locale text that is displayed if the creature is female.

lang7
-----

The language of the text in game.

prob7
-----

This is the probability that the creature will say this text.

em7\_0\_delay
-------------

Time to wait before the first emote is played.

em7\_0
------

Emote to play when text is displayed.

em7\_1\_delay
-------------

Time to wait after the first emote are played, before the second emote
gets played.

em7\_1
------

Second emote to play when text is displayed.

em7\_2\_delay
-------------

Time to wait after the second emote are played, before the third emote
gets played.

em7\_2
------

Third emote to play when text is displayed.
