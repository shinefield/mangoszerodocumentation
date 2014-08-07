.. _file-formats-dbc-emotestextdata:

==================
EmotesTextData.dbc
==================

The *emotes text data* table contains definitions for actual text emotes
to display in-game when slash commands are executed.

Table structure
---------------

+------+--------+----------------------+-----------+------------------------+
| ID   | Name   | Type                 | Default   | Description            |
+======+========+======================+===========+========================+
| 1    | ID     | Integer              | -         | Unique ID              |
+------+--------+----------------------+-----------+------------------------+
| 2    | text   | String (localized)   | -         | The emote chat text.   |
+------+--------+----------------------+-----------+------------------------+
