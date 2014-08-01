.. _file-formats-dbc-uisoundlookups:

==================
UISoundLookups.dbc
==================

The *UI sound lookups* table contains definitions for sounds used in
various sections of the user interface.

Table structure
---------------

+------+----------------+--------------------+-----------+-----------------------------------------------------------------------------------+
| ID   | Name           | Type               | Default   | Description                                                                       |
+======+================+====================+===========+===================================================================================+
| 1    | ID             | Integer (signed)   | -         | Unique ID                                                                         |
+------+----------------+--------------------+-----------+-----------------------------------------------------------------------------------+
| 2    | soundEntryID   | Integer (signed)   | 0         | The sound to be played.                                                           |
+------+----------------+--------------------+-----------+-----------------------------------------------------------------------------------+
| 3    | internalName   | String             | -         | Most likely the hard-coded name used in the clients' interface and LUA scripts.   |
+------+----------------+--------------------+-----------+-----------------------------------------------------------------------------------+

Relations
---------

-  ``soundEntryID`` references the primary key of ``SoundEntries.dbc``.
