.. _file-formats-dbc-chatchannels:

================
ChatChannels.dbc
================

The *chat channels* table contains definitions for in-game chat channels
and their availability.

Table structure
---------------

+------+----------------+----------------------+-----------+------------------------------------------------------------------+
| ID   | Name           | Type                 | Default   | Description                                                      |
+======+================+======================+===========+==================================================================+
| 1    | ID             | Integer (signed)     | -         | Unique ID                                                        |
+------+----------------+----------------------+-----------+------------------------------------------------------------------+
| 2    | flags          | Integer              | 0         | See below.                                                       |
+------+----------------+----------------------+-----------+------------------------------------------------------------------+
| 3    | factionGroup   | Integer (signed)     | 0         | References which faction has access to the channel.              |
+------+----------------+----------------------+-----------+------------------------------------------------------------------+
| 4    | name           | String (localized)   | -         | The name of the chat channel as display in the user interface.   |
+------+----------------+----------------------+-----------+------------------------------------------------------------------+
| 5    | shortcut       | String (localized)   | -         | The short-cut name as used on user interface scripting.          |
+------+----------------+----------------------+-----------+------------------------------------------------------------------+

Fields
------

flags
~~~~~

``flags`` indicate in which state a channel is set initially for a
character.

-  ``0``: *FLAG\_NONE* indicates a channel which is available but not
   joined by characters,
-  ``1``: *FLAG\_INITIAL* indicates a channel which is automatically
   joined by characters,
-  ``2``: *FLAG\_ZONE\_DEP* indicates a channel which is zone specific,
-  ``4``: *FLAG\_GLOBAL* indicates a channel which is available
   everywhere,
-  ``8``: *FLAG\_TRADE* indicates a channel which is a trade channel
   (duh!),
-  ``16``: *FLAG\_CITY\_ONLY* indicates a channel which is available in
   cities only,
-  ``32``: *FLAG\_CITY\_ONLY2* indicates a channel which is available in
   cities only,
-  ``65536``: *FLAG\_DEFENSE* indicates a channel which is a PvP
   channel,
-  ``262144``: *FLAG\_UISELECTED* indicates a channel which is optional
   and selected in user interface.

Relations
---------

-  ``factionGroup`` references the key *maskID* of ``FactionGroup.dbc``.
