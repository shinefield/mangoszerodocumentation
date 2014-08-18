.. _file-formats-dbc-animationdata:

=================
AnimationData.dbc
=================

The *animation data* table contains the basic definitions for available animation types
that can be used in models.

Table structure
---------------

+------+---------------+--------------------+-----------+----------------------------------------------------------------+
| ID   | Name          | Type               | Default   | Description                                                    |
+======+===============+====================+===========+================================================================+
| 1    | ID            | Integer            | -         | Unique ID                                                      |
+------+---------------+--------------------+-----------+----------------------------------------------------------------+
| 2    | name          | String             | -         | The name of the animation.                                     |
+------+---------------+--------------------+-----------+----------------------------------------------------------------+
| 3    | weaponFlags   | Integer (signed)   | 0         | See below.                                                     |
+------+---------------+--------------------+-----------+----------------------------------------------------------------+
| 4    | bodyFlags     | Integer (signed)   | 0         | See below.                                                     |
+------+---------------+--------------------+-----------+----------------------------------------------------------------+
| 5    | flags         | Integer (signed)   | 0         | See below.                                                     |
+------+---------------+--------------------+-----------+----------------------------------------------------------------+
| 6    | fallback      | Integer            | 0         | The animation to return to after this animation is finished.   |
+------+---------------+--------------------+-----------+----------------------------------------------------------------+
| 7    | behavior      | Integer            | 0         | The preceding animation.                                       |
+------+---------------+--------------------+-----------+----------------------------------------------------------------+

Fields
------

weaponFlags
~~~~~~~~~~~

Weapon flags describe if an animation should modify the weapon(s) state
worn by a character. Animations can ignore weapons and sheathe/unsheathe
them.

-  ``0``: weapon not affected by animation,
-  ``4``: sheathe weapons automatically,
-  ``16``: sheathe weapons automatically,
-  ``32``: unsheathe weapons.

bodyFlags
~~~~~~~~~
**TODO**

Flags
~~~~~
**TODO**

Relations
---------

-  ``fallback`` references the primary key of :doc:`animationdata`.
-  ``behavior`` references the primary key of :doc:`animationdata`.
