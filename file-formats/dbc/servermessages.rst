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
| 1    | ID     | Integer (signed)     | -         | Unique ID                  |
+------+--------+----------------------+-----------+----------------------------+
| 2    | text   | String (localized)   | -         | The server message text.   |
+------+--------+----------------------+-----------+----------------------------+

Data
----

The following is a list of available quest types.

+------+-------------------------------+
| ID   | Message                       |
+======+===============================+
| 1    | [SERVER] Shutdown in %s       |
+------+-------------------------------+
| 2    | [SERVER] Restart in %s        |
+------+-------------------------------+
| 3    | %s                            |
+------+-------------------------------+
| 4    | [SERVER] Shutdown cancelled   |
+------+-------------------------------+
| 5    | [SERVER] Restart cancelled    |
+------+-------------------------------+
