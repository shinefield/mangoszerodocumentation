.. _db-script-custom-texts:

=====================
"custom\_texts" table
=====================

The ``custom_texts`` table holds custom text strings, sounds, and emotes
used in scripted events.

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
~~~~~

The unique identifier of the script text entry. Identifiers here have to
match with the identifier set in the string using the text.

.. note::

    identifiers use a fixed format of ``-1<map-identifier><three-digit-counter>``.

content\_default
~~~~~~~~~~~~~~~~

The default text to be displayed in English.

content\_loc1
~~~~~~~~~~~~~

*Korean* localization of ``content_default``.

content\_loc2
~~~~~~~~~~~~~

*French* localization of ``content_default``.

content\_loc3
~~~~~~~~~~~~~

*German* localization of ``content_default``.

content\_loc4
~~~~~~~~~~~~~

*Chinese* localization of ``content_default``.

content\_loc5
~~~~~~~~~~~~~

*Taiwanese* localization of ``content_default``.

content\_loc6
~~~~~~~~~~~~~

*Spanish Spain* localization of ``content_default``.

content\_loc7
~~~~~~~~~~~~~

*Spanish Latin America* localization of ``content_default``.

content\_loc8
~~~~~~~~~~~~~

*Russian* localization of ``content_default``.

sound
~~~~~

If a sound file should be played, this references an entry in the
:doc:`SoundEntries.dbc <../../file-formats/dbc/soundentries>` table.

type
~~~~

Selects one of various text emote types to be used for the script text.
The following tables shows available text emote types.

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
~~~~~~~~

A language identifier. The value has to match with a language identifier
defined in :doc:`Languages.dbc <../../file-formats/dbc/languages>`.

emote
~~~~~

An emote identifier. The value has to match with a emote identifier
defined in :doc:`Emotes.dbc <../../file-formats/dbc/emotes>`.

comment
~~~~~~~

This documents the script text. Currently no rules have been defined for
the format of the comment. It *should* help identifying who and why does
perform the emote.
