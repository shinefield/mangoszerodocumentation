.. _file-formats-dbc-creaturespelldata:

=====================
CreatureSpellData.dbc
=====================

The *creature spell data* table contains definitions for the spells a
creature has access to. This table specifically targets creatures which
can be tamed.

Table structure
---------------

+------+-----------------+--------------------+-----------+--------------------------------------------------+
| ID   | Name            | Type               | Default   | Description                                      |
+======+=================+====================+===========+==================================================+
| 1    | ID              | Integer            | -         | Unique ID                                        |
+------+-----------------+--------------------+-----------+--------------------------------------------------+
| 2    | spell1          | Integer            | 0         | References a spell the creature has access to.   |
+------+-----------------+--------------------+-----------+--------------------------------------------------+
| 3    | spell2          | Integer            | 0         | References a spell the creature has access to.   |
+------+-----------------+--------------------+-----------+--------------------------------------------------+
| 4    | spell3          | Integer            | 0         | References a spell the creature has access to.   |
+------+-----------------+--------------------+-----------+--------------------------------------------------+
| 5    | spell4          | Integer            | 0         | References a spell the creature has access to.   |
+------+-----------------+--------------------+-----------+--------------------------------------------------+
| 6    | cooldownTime1   | Integer (signed)   | 0         | Cool-down for spell1.                            |
+------+-----------------+--------------------+-----------+--------------------------------------------------+
| 7    | cooldownTime2   | Integer (signed)   | 0         | Cool-down for spell2.                            |
+------+-----------------+--------------------+-----------+--------------------------------------------------+
| 8    | cooldownTime3   | Integer (signed)   | 0         | Cool-down for spell3.                            |
+------+-----------------+--------------------+-----------+--------------------------------------------------+
| 9    | cooldownTime4   | Integer (signed)   | 0         | Cool-down for spell4.                            |
+------+-----------------+--------------------+-----------+--------------------------------------------------+

Relations
---------

-  ``spell[1-4]`` references the primary key of ``Spell.dbc``.

Notes
-----

To calculate the actual cool-down time in human readable form, divide
``cooldownTime`` by 10 to get time in seconds.
