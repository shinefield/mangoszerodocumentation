.. _file-formats-dbc-lfgdungeons:

===============
LFGDungeons.dbc
===============

The *looking for dungeon* group table contains definitions for areas in
which characters can group up via in-game LFG.

Table structure
---------------

+------+----------------+----------------------+-----------+--------------------------------------------------+
| ID   | Name           | Type                 | Default   | Description                                      |
+======+================+======================+===========+==================================================+
| 1    | ID             | Integer (signed)     | -         | Unique ID                                        |
+------+----------------+----------------------+-----------+--------------------------------------------------+
| 2    | name           | String (localized)   | -         | The name of the area.                            |
+------+----------------+----------------------+-----------+--------------------------------------------------+
| 3    | hardLevelMin   | Integer              | 0         | Minimum level required to group for this area.   |
+------+----------------+----------------------+-----------+--------------------------------------------------+
| 4    | hardLevelMax   | Integer              | 0         | Maximum level allowed to group for this area.    |
+------+----------------+----------------------+-----------+--------------------------------------------------+
| 5    | instanceType   | Integer              | 0         | See below.                                       |
+------+----------------+----------------------+-----------+--------------------------------------------------+
| 6    | faction        | Integer              | 0         | See below.                                       |
+------+----------------+----------------------+-----------+--------------------------------------------------+

Fields
------

instanceType
~~~~~~~~~~~~

-  ``1``: group instance,
-  ``2``: raid group instance,
-  ``4``: world zone,
-  ``5``: battleground.

.. note::

    only zones listed as *group instance* could be accessed via meeting stones or
    innkeepers for the Looking For Group feature.

faction
~~~~~~~

-  ``-1``: faction independent,
-  ``0``: Horde faction,
-  ``1``: Alliance faction.
