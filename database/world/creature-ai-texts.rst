.. _db-world-creature-ai-texts:

===========================
"creature\_ai\_texts" table
===========================

The ``creature_ai_texts`` table holds all texts used by creature scripts
defined in ``creature_ai_scripts``.

The texts are used for creature say/yell/emote actions and may be
combined with emotes.

Table structure
---------------

+--------------------+-------------------------+--------+-------+-----------+---------+
| Field              | Type                    | Null   | Key   | Default   | Extra   |
+====================+=========================+========+=======+===========+=========+
| entry              | mediumint(8)            | NO     | PRI   | NULL      |         |
+--------------------+-------------------------+--------+-------+-----------+---------+
| content\_default   | text                    | NO     |       | NULL      |         |
+--------------------+-------------------------+--------+-------+-----------+---------+
| content\_loc1      | text                    | YES    |       | NULL      |         |
+--------------------+-------------------------+--------+-------+-----------+---------+
| content\_loc2      | text                    | YES    |       | NULL      |         |
+--------------------+-------------------------+--------+-------+-----------+---------+
| content\_loc3      | text                    | YES    |       | NULL      |         |
+--------------------+-------------------------+--------+-------+-----------+---------+
| content\_loc4      | text                    | YES    |       | NULL      |         |
+--------------------+-------------------------+--------+-------+-----------+---------+
| content\_loc5      | text                    | YES    |       | NULL      |         |
+--------------------+-------------------------+--------+-------+-----------+---------+
| content\_loc6      | text                    | YES    |       | NULL      |         |
+--------------------+-------------------------+--------+-------+-----------+---------+
| content\_loc7      | text                    | YES    |       | NULL      |         |
+--------------------+-------------------------+--------+-------+-----------+---------+
| content\_loc8      | text                    | YES    |       | NULL      |         |
+--------------------+-------------------------+--------+-------+-----------+---------+
| sound              | mediumint(8) unsigned   | NO     |       | 0         |         |
+--------------------+-------------------------+--------+-------+-----------+---------+
| type               | tinyint(3) unsigned     | NO     |       | 0         |         |
+--------------------+-------------------------+--------+-------+-----------+---------+
| language           | tinyint(3) unsigned     | NO     |       | 0         |         |
+--------------------+-------------------------+--------+-------+-----------+---------+
| emote              | smallint(5) unsigned    | NO     |       | 0         |         |
+--------------------+-------------------------+--------+-------+-----------+---------+
| comment            | text                    | YES    |       | NULL      |         |
+--------------------+-------------------------+--------+-------+-----------+---------+

Fields
------

entry
-----

This references a script using an action of the type ``ACTION_T_TEXT``
in the :doc:`creature-ai-scripts` tables entry.

.. note::

    IDs use the *negative* versions of the referenced action's ID.

content\_default
----------------

Contains the text presented in the default language English. Strings may
contain special variables which are replaced with creature or character
data. The following table lists available variables.

+--------------------------------------+-------------------+
| Value                                | Description       |
+======================================+===================+
| %s                                   | Creature name     |
+--------------------------------------+-------------------+
| $n                                   | Character name    |
+--------------------------------------+-------------------+
| $r                                   | Character race    |
+--------------------------------------+-------------------+
| $c                                   | Character class   |
+--------------------------------------+-------------------+

content\_loc1
-------------

*Korean* localization of ``content_default``.

content\_loc2
-------------

*French* localization of ``content_default``.

content\_loc3
-------------

*German* localization of ``content_default``.

content\_loc4
-------------

*Chinese* localization of ``content_default``.

content\_loc5
-------------

*Taiwanese* localization of ``content_default``.

content\_loc6
-------------

*Spanish Spain* localization of ``content_default``.

content\_loc7
-------------

*Spanish Latin America* localization of ``content_default``.

content\_loc8
-------------

*Russian* localization of ``content_default``.

sound
-----

A sound identifier. The value has to match with a sound identifier
defined in :doc:`../../file-formats/dbc/soundentries`.

type
----

The type of message to display. The following table lists all valid
types.

+---------+----------------+
| Value   | Description    |
+=========+================+
| 0       | Say            |
+---------+----------------+
| 1       | Yell           |
+---------+----------------+
| 2       | Text emote     |
+---------+----------------+
| 3       | Boss emote     |
+---------+----------------+
| 4       | Whisper        |
+---------+----------------+
| 5       | Boss whisper   |
+---------+----------------+

language
--------

A language identifier. The value has to match with a language identifier
defined in :doc:`../../file-formats/dbc/languages`.

emote
-----

An emote identifier. The value has to match with a emote identifier
defined in :doc:`../../file-formats/dbc/emotes`.

comment
-------

This documents the creature text. Currently no rules have been defined
for the format of the comment. It *should* help identifying who and why
does perform the emote.
