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
| 1    | ID                 | Integer            | -         | Unique ID                                         |
+------+--------------------+--------------------+-----------+---------------------------------------------------+
| 2    | enum               | Integer (signed)   | 0         | References an ID as defined in the game client.   |
+------+--------------------+--------------------+-----------+---------------------------------------------------+
| 3    | spellVisualKit     | Integer            | 0         | The spell visual to display.                      |
+------+--------------------+--------------------+-----------+---------------------------------------------------+

Relations
---------

-  ``spellVisualKit`` references the primary key of ``SpellVisualKit.dbc``.
