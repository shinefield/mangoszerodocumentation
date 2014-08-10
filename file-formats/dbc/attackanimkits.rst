.. _file-formats-dbc-attackanimkits:

==================
AttackAnimKits.dbc
==================

The *attack animation kits* table contains definitions for attack
animation groups.

Table structure
---------------

+------+--------------------+--------------------+-----------+-------------------------------------------------------------+
| ID   | Name               | Type               | Default   | Description                                                 |
+======+====================+====================+===========+=============================================================+
| 1    | ID                 | Integer            | -         | Unique ID                                                   |
+------+--------------------+--------------------+-----------+-------------------------------------------------------------+
| 2    | animationData      | Integer            | 0         | The ID of the animation to play.                            |
+------+--------------------+--------------------+-----------+-------------------------------------------------------------+
| 3    | attackAnimType     | Integer            | 0         | The ID of the attack animation type.                        |
+------+--------------------+--------------------+-----------+-------------------------------------------------------------+
| 4    | flags              | Integer (signed)   | 0         | See below.                                                  |
+------+--------------------+--------------------+-----------+-------------------------------------------------------------+
| 5    | field5             | Integer (signed)   | 0         | **TODO**. seems to be a flag for OffHand attack animation   |
+------+--------------------+--------------------+-----------+-------------------------------------------------------------+

Fields
------

flags
~~~~~

Determines what kind of weapon animation this is.

-  ``0``: Main hand,
-  ``1``: Off hand.

Relations
---------

-  ``animationData`` references the primary key of :doc:`animationdata`.
-  ``attackAnimType`` references the primary key of :doc:`attackanimtypes`.
