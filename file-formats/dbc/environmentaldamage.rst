.. _file-formats-dbc-environmentaldamage:

=======================
EnvironmentalDamage.dbc
=======================

The *environmental damage* table contains definitions which connect
environmental damage to a spell visual.

Table structure
---------------

+------+--------------------+--------------------+-----------+---------------------------------------------------+
| ID   | Name               | Type               | Default   | Description                                       |
+======+====================+====================+===========+===================================================+
| 1    | ID                 | Integer (signed)   | -         | Unique ID                                         |
+------+--------------------+--------------------+-----------+---------------------------------------------------+
| 2    | enumID             | Integer            | 0         | References an ID as defined in the game client.   |
+------+--------------------+--------------------+-----------+---------------------------------------------------+
| 3    | spellVisualKitID   | Integer (signed)   | 0         | The spell visual to display.                      |
+------+--------------------+--------------------+-----------+---------------------------------------------------+

Relations
---------

-  ``spellVisualKitID`` references the primary key of
   ``SpellVisualKit.dbc``.
