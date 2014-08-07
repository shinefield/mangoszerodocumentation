.. _file-formats-dbc-servermessages:

==================
ServerMessages.dbc
==================

The *server messages* table contains definitions for chat messages sent
by the game server.

Table structure
---------------

+------+--------+----------------------+-----------+----------------------------+
| ID   | Name   | Type                 | Default   | Description                |
+======+========+======================+===========+============================+
| 1    | ID     | Integer              | -         | Unique ID                  |
+------+--------+----------------------+-----------+----------------------------+
| 2    | text   | String (localized)   | -         | The server message text.   |
+------+--------+----------------------+-----------+----------------------------+
