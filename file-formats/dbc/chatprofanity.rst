.. _file-formats-dbc-chatprofanity:

=================
ChatProfanity.dbc
=================

The *chat profanity* table contains definitions for words/strings which
are banned from in-game chat channels.

Table structure
---------------

+------+--------+--------------------+-----------+------------------------------------------------+
| ID   | Name   | Type               | Default   | Description                                    |
+======+========+====================+===========+================================================+
| 1    | ID     | Integer (signed)   | -         | Unique ID                                      |
+------+--------+--------------------+-----------+------------------------------------------------+
| 2    | text   | String             | -         | A word/string not allowed in a chat message.   |
+------+--------+--------------------+-----------+------------------------------------------------+

