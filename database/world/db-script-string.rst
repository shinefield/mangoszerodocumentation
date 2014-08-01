.. _db-world-db-script-string:

==========================
"db\_script\_string" table
==========================

The ``db_script_string`` table holds all texts used by creature scripts
defined for templates.

The texts are used for creature say/yell/emote actions and may be
combined with emotes.

Table structure
---------------

+--------------------+-------------------------+--------+-------+-----------+---------+
| Field              | Type                    | Null   | Key   | Default   | Extra   |
+====================+=========================+========+=======+===========+=========+
| entry              | int(11) unsigned        | NO     | PRI   | 0         |         |
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

The unique identifier of the script string entry.

.. note::

    entries in this table have to use an ID range from ``2000000000`` to ``2000010000``.

content\_default
----------------

The English translation.

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
defined in `SoundEntries.dbc <../dbc/SoundEntries.dbc>`__.

The type of message to display. The following table lists all valid
types.

+---------+------------------+
| Value   | Description      |
+=========+==================+
| 0       | Say              |
+---------+------------------+
| 1       | Yell             |
+---------+------------------+
| 2       | Text emote       |
+---------+------------------+
| 3       | Boss emote       |
+---------+------------------+
| 4       | Whisper          |
+---------+------------------+
| 5       | Boss whisper     |
+---------+------------------+
| 6       | Zone-wide yell   |
+---------+------------------+

language
--------

A language identifier. The value has to match with a language identifier
defined in `Languages.dbc <../dbc/Languages.dbc>`__.

emote
-----

An emote identifier. The value has to match with a emote identifier
defined in `Emotes.dbc <../dbc/Emotes.dbc>`__.

comment
-------

This documents the script text. Currently no rules have been defined for
the format of the comment. It *should* help identifying who and why does
perform the emote.
