.. _file-formats-dbc-spammessages:

================
SpamMessages.dbc
================

The *spam messages* table contains definitions for regular expressions
used to decide if a chat message is spam.

Table structure
---------------

+------+--------+--------------------+-----------+---------------------------+
| ID   | Name   | Type               | Default   | Description               |
+======+========+====================+===========+===========================+
| 1    | ID     | Integer            | -         | Unique ID                 |
+------+--------+--------------------+-----------+---------------------------+
| 2    | text   | String             | -         | The regular expression.   |
+------+--------+--------------------+-----------+---------------------------+
