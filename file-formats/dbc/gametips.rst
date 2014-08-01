.. _file-formats-dbc-gametips:

============
GameTips.dbc
============

The *game tips* table contains definitions for game tips displayed on
the world loading screen to players.

Table structure
---------------

+------+--------+----------------------+-----------+-----------------------------+
| ID   | Name   | Type                 | Default   | Description                 |
+======+========+======================+===========+=============================+
| 1    | ID     | Integer (signed)     | -         | Unique ID                   |
+------+--------+----------------------+-----------+-----------------------------+
| 2    | text   | String (localized)   | -         | The text of the game tip.   |
+------+--------+----------------------+-----------+-----------------------------+

Notes
-----

The text for a game tip needs to be parsed with a regular expression to
extract colour, title and actual tip from the text.
