.. _file-formats-dbc-animationdata:

=================
AnimationData.dbc
=================

The *animation data* table contains definitions for the different
animations models can have.

Table structure
---------------

+------+---------------+--------------------+-----------+----------------------------------------------------------------+
| ID   | Name          | Type               | Default   | Description                                                    |
+======+===============+====================+===========+================================================================+
| 1    | ID            | Integer (signed)   | -         | Unique ID                                                      |
+------+---------------+--------------------+-----------+----------------------------------------------------------------+
| 2    | name          | String             | -         | The name of the animation.                                     |
+------+---------------+--------------------+-----------+----------------------------------------------------------------+
| 3    | weaponFlags   | Integer            | 0         | See below.                                                     |
+------+---------------+--------------------+-----------+----------------------------------------------------------------+
| 4    | bodyFlags     | Integer            | 0         | See below.                                                     |
+------+---------------+--------------------+-----------+----------------------------------------------------------------+
| 5    | flags         | Integer            | 0         | See below.                                                     |
+------+---------------+--------------------+-----------+----------------------------------------------------------------+
| 6    | fallbackID    | Integer (signed)   | 0         | The animation to return to after this animation is finished.   |
+------+---------------+--------------------+-----------+----------------------------------------------------------------+
| 7    | behaviourID   | Integer (signed)   | 0         | The preceding animation.                                       |
+------+---------------+--------------------+-----------+----------------------------------------------------------------+

Fields
------

weaponFlags
-----------

Weapon flags describe if an animation should modify the weapon(s) state
worn by a character. Animations can ignore weapons and sheathe/unsheathe
them.

-  ``0``: weapon not affected by animation,
-  ``4``: sheathe weapons automatically,
-  ``16``: sheathe weapons automatically,
-  ``32``: unsheathe weapons.

Relations
---------

-  ``fallbackID`` references the primary key of ``AnimationData.dbc``.
-  ``behaviourID`` references the primary key of ``AnimationData.dbc``.

